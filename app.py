from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-change-this-in-production'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///careconnect.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'signin'

# Database Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    password = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(50), nullable=False)  # donor, senior, special, admin
    registered_date = db.Column(db.DateTime, default=datetime.utcnow)
    donations = db.relationship('Donation', backref='donor', lazy=True)

class SeniorCitizen(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    contact = db.Column(db.String(20), nullable=False)
    role_type = db.Column(db.String(50), default='Senior Citizen')
    added_date = db.Column(db.DateTime, default=datetime.utcnow)

class SpecialPerson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    contact = db.Column(db.String(20), nullable=False)
    role_type = db.Column(db.String(50), default='Special Person')
    added_date = db.Column(db.DateTime, default=datetime.utcnow)

class Donor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    contact = db.Column(db.String(20), nullable=False)
    address = db.Column(db.Text, nullable=False)
    donation_type = db.Column(db.String(50), nullable=False)  # Monthly/One Time
    amount = db.Column(db.Float, nullable=False)
    preferred_time = db.Column(db.String(100), nullable=False)
    added_date = db.Column(db.DateTime, default=datetime.utcnow)

class Donation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    donor_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    cnic = db.Column(db.String(20), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    payment_method = db.Column(db.String(50), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='Completed')

class ReceivedDonation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipient_id = db.Column(db.Integer, nullable=False)  # User ID of senior/special person
    recipient_name = db.Column(db.String(100), nullable=False)
    recipient_email = db.Column(db.String(100), nullable=False)
    recipient_type = db.Column(db.String(50), nullable=False)  # 'senior' or 'special'
    amount = db.Column(db.Float, nullable=False)
    purpose = db.Column(db.String(200), nullable=False)  # Medical, Food, Education, etc.
    notes = db.Column(db.Text)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    given_by = db.Column(db.String(100), default='Admin')
    status = db.Column(db.String(20), default='Completed')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard_redirect'))
    
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('dashboard_redirect'))
        else:
            flash('Invalid email or password', 'error')
    
    return render_template('signin.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard_redirect'))
    
    if request.method == 'POST':
        full_name = request.form.get('full_name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        password = request.form.get('password')
        category = request.form.get('category')
        
        # Check if user exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already registered', 'error')
            return redirect(url_for('signup'))
        
        # Create new user
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User(
            full_name=full_name,
            email=email,
            phone=phone,
            password=hashed_password,
            category=category
        )
        
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful! Please sign in.', 'success')
        return redirect(url_for('signin'))
    
    return render_template('signup.html')

@app.route('/dashboard-redirect')
@login_required
def dashboard_redirect():
    if current_user.category == 'donor':
        return redirect(url_for('donor_dashboard'))
    elif current_user.category in ['senior', 'special']:
        return redirect(url_for('senior_dashboard'))
    elif current_user.category == 'admin':
        return redirect(url_for('admin_dashboard'))
    else:
        return redirect(url_for('index'))

@app.route('/donor-dashboard')
@login_required
def donor_dashboard():
    if current_user.category != 'donor':
        return redirect(url_for('dashboard_redirect'))
    
    donations = Donation.query.filter_by(user_id=current_user.id).all()
    total_amount = sum(d.amount for d in donations)
    
    return render_template('donor_dashboard.html', 
                         donations=donations, 
                         total_amount=total_amount)

@app.route('/submit-donation', methods=['POST'])
@login_required
def submit_donation():
    if current_user.category != 'donor':
        return jsonify({'success': False, 'message': 'Unauthorized'}), 403
    
    donation = Donation(
        user_id=current_user.id,
        donor_name=request.form.get('donor_name'),
        email=request.form.get('email'),
        phone=request.form.get('phone'),
        cnic=request.form.get('cnic'),
        amount=float(request.form.get('amount')),
        payment_method=request.form.get('payment_method')
    )
    
    db.session.add(donation)
    db.session.commit()
    
    return jsonify({'success': True, 'message': 'Donation submitted successfully'})

@app.route('/senior-dashboard')
@login_required
def senior_dashboard():
    if current_user.category not in ['senior', 'special']:
        return redirect(url_for('dashboard_redirect'))
    
    # Get received donations for this user
    received_donations = ReceivedDonation.query.filter_by(recipient_id=current_user.id).order_by(ReceivedDonation.date.desc()).all()
    total_received = sum(d.amount for d in received_donations)
    
    return render_template('senior_dashboard.html', 
                         received_donations=received_donations,
                         total_received=total_received)

@app.route('/admin-dashboard')
@login_required
def admin_dashboard():
    if current_user.category != 'admin':
        flash('Unauthorized access', 'error')
        return redirect(url_for('index'))
    
    # Get all users
    all_users = User.query.all()
    
    # Get admin-added senior citizens and special people
    admin_senior_citizens = SeniorCitizen.query.all()
    admin_special_people = SpecialPerson.query.all()
    admin_donors = Donor.query.all()
    
    # Get self-registered users by category
    registered_seniors = User.query.filter_by(category='senior').all()
    registered_special = User.query.filter_by(category='special').all()
    registered_donors = User.query.filter_by(category='donor').all()
    
    # Combine admin-added and self-registered for display
    # Convert User objects to dictionary format matching admin-added structure
    combined_seniors = []
    combined_special = []
    combined_donors = []
    
    # Add admin-added seniors
    for senior in admin_senior_citizens:
        combined_seniors.append({
            'id': senior.id,
            'name': senior.name,
            'email': senior.email,
            'age': senior.age,
            'contact': senior.contact,
            'added_date': senior.added_date,
            'source': 'admin',
            'role_type': 'Senior Citizen'
        })
    
    # Add self-registered seniors
    for user in registered_seniors:
        combined_seniors.append({
            'id': user.id,
            'name': user.full_name,
            'email': user.email,
            'age': 'N/A',
            'contact': user.phone if user.phone else 'N/A',
            'added_date': user.registered_date,
            'source': 'self',
            'role_type': 'Senior Citizen'
        })
    
    # Add admin-added special people
    for special in admin_special_people:
        combined_special.append({
            'id': special.id,
            'name': special.name,
            'email': special.email,
            'age': special.age,
            'contact': special.contact,
            'added_date': special.added_date,
            'source': 'admin',
            'role_type': 'Special Person'
        })
    
    # Add self-registered special people
    for user in registered_special:
        combined_special.append({
            'id': user.id,
            'name': user.full_name,
            'email': user.email,
            'age': 'N/A',
            'contact': user.phone if user.phone else 'N/A',
            'added_date': user.registered_date,
            'source': 'self',
            'role_type': 'Special Person'
        })
    
    # Add admin-added donors
    for donor in admin_donors:
        combined_donors.append({
            'id': donor.id,
            'name': donor.name,
            'age': donor.age,
            'gender': donor.gender,
            'contact': donor.contact,
            'address': donor.address,
            'donation_type': donor.donation_type,
            'amount': donor.amount,
            'preferred_time': donor.preferred_time,
            'added_date': donor.added_date,
            'source': 'admin'
        })
    
    # Add self-registered donors
    for user in registered_donors:
        combined_donors.append({
            'id': user.id,
            'name': user.full_name,
            'age': 'N/A',
            'gender': 'N/A',
            'contact': user.phone if user.phone else 'N/A',
            'address': 'N/A',
            'donation_type': 'Self Registered',
            'amount': 0,
            'preferred_time': 'N/A',
            'added_date': user.registered_date,
            'source': 'self'
        })
    
    # Get all donations
    all_donations = Donation.query.all()
    
    # Get all received donations
    all_received_donations = ReceivedDonation.query.order_by(ReceivedDonation.date.desc()).all()
    
    # Calculate statistics
    total_users = len(all_users)
    total_donations_received = sum(d.amount for d in all_donations)
    total_donations_given = sum(d.amount for d in all_received_donations)
    remaining_balance = total_donations_received - total_donations_given
    total_seniors = len(combined_seniors)
    total_donors = len(combined_donors)
    
    return render_template('admin_dashboard.html',
                         total_users=total_users,
                         total_donations_received=total_donations_received,
                         total_donations_given=total_donations_given,
                         remaining_balance=remaining_balance,
                         total_seniors=total_seniors,
                         total_donors=total_donors,
                         senior_citizens=combined_seniors,
                         special_people=combined_special,
                         donors=combined_donors,
                         all_donations=all_donations,
                         all_received_donations=all_received_donations)

@app.route('/admin/add-senior', methods=['POST'])
@login_required
def add_senior():
    if current_user.category != 'admin':
        return jsonify({'success': False, 'message': 'Unauthorized'}), 403
    
    senior = SeniorCitizen(
        name=request.form.get('name'),
        email=request.form.get('email'),
        age=int(request.form.get('age')),
        contact=request.form.get('contact')
    )
    
    db.session.add(senior)
    db.session.commit()
    
    return jsonify({'success': True, 'message': 'Senior citizen added successfully'})

@app.route('/admin/add-special', methods=['POST'])
@login_required
def add_special():
    if current_user.category != 'admin':
        return jsonify({'success': False, 'message': 'Unauthorized'}), 403
    
    special = SpecialPerson(
        name=request.form.get('name'),
        email=request.form.get('email'),
        age=int(request.form.get('age')),
        contact=request.form.get('contact')
    )
    
    db.session.add(special)
    db.session.commit()
    
    return jsonify({'success': True, 'message': 'Special person added successfully'})

@app.route('/admin/add-donor', methods=['POST'])
@login_required
def add_donor():
    if current_user.category != 'admin':
        return jsonify({'success': False, 'message': 'Unauthorized'}), 403
    
    donor = Donor(
        name=request.form.get('name'),
        age=int(request.form.get('age')),
        gender=request.form.get('gender'),
        contact=request.form.get('contact'),
        address=request.form.get('address'),
        donation_type=request.form.get('donation_type'),
        amount=float(request.form.get('amount')),
        preferred_time=request.form.get('preferred_time')
    )
    
    db.session.add(donor)
    db.session.commit()
    
    return jsonify({'success': True, 'message': 'Donor added successfully'})

@app.route('/admin/delete-senior/<int:id>', methods=['DELETE'])
@login_required
def delete_senior(id):
    if current_user.category != 'admin':
        return jsonify({'success': False, 'message': 'Unauthorized'}), 403
    
    senior = SeniorCitizen.query.get_or_404(id)
    db.session.delete(senior)
    db.session.commit()
    
    return jsonify({'success': True, 'message': 'Senior citizen deleted'})

@app.route('/admin/delete-special/<int:id>', methods=['DELETE'])
@login_required
def delete_special(id):
    if current_user.category != 'admin':
        return jsonify({'success': False, 'message': 'Unauthorized'}), 403
    
    special = SpecialPerson.query.get_or_404(id)
    db.session.delete(special)
    db.session.commit()
    
    return jsonify({'success': True, 'message': 'Special person deleted'})

@app.route('/admin/delete-donor/<int:id>', methods=['DELETE'])
@login_required
def delete_donor(id):
    if current_user.category != 'admin':
        return jsonify({'success': False, 'message': 'Unauthorized'}), 403
    
    donor = Donor.query.get_or_404(id)
    db.session.delete(donor)
    db.session.commit()
    
    return jsonify({'success': True, 'message': 'Donor deleted'})

@app.route('/admin/give-donation', methods=['POST'])
@login_required
def give_donation():
    if current_user.category != 'admin':
        return jsonify({'success': False, 'message': 'Unauthorized'}), 403
    
    received_donation = ReceivedDonation(
        recipient_id=int(request.form.get('recipient_id')),
        recipient_name=request.form.get('recipient_name'),
        recipient_email=request.form.get('recipient_email'),
        recipient_type=request.form.get('recipient_type'),
        amount=float(request.form.get('amount')),
        purpose=request.form.get('purpose'),
        notes=request.form.get('notes', ''),
        given_by='Admin - ' + current_user.full_name
    )
    
    db.session.add(received_donation)
    db.session.commit()
    
    return jsonify({'success': True, 'message': 'Donation given successfully'})

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out successfully', 'success')
    return redirect(url_for('index'))

# Initialize database
def init_db():
    with app.app_context():
        db.create_all()
        
        # Create admin user if not exists
        admin = User.query.filter_by(email='admin@careconnect.org').first()
        if not admin:
            admin_user = User(
                full_name='Admin',
                email='admin@careconnect.org',
                phone='03001234567',
                password=generate_password_hash('admin123', method='pbkdf2:sha256'),
                category='admin'
            )
            db.session.add(admin_user)
            db.session.commit()
            print("Admin user created: admin@careconnect.org / admin123")

if __name__ == '__main__':
    init_db()
    app.run(debug=True)