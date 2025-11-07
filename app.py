from flask import Flask, render_template, request, redirect, url_for, flash, session
from datetime import datetime
import json

app = Flask(__name__)
app.secret_key = 'health-camp-demo-key'

# Sample data for the preview
camps_data = [
    {
        'id': 1,
        'name': 'Free Eye Care Camp',
        'hospital': 'City General Hospital',
        'date': '2024-08-15',
        'time': '9:00 AM - 5:00 PM',
        'location': 'Community Center, Downtown',
        'services': ['Eye Examination', 'Vision Testing', 'Glaucoma Screening'],
        'capacity': 100,
        'registered': 45,
        'available': True
    },
    {
        'id': 2,
        'name': 'Diabetes Screening Camp',
        'hospital': 'Metro Health Center',
        'date': '2024-08-20',
        'time': '8:00 AM - 4:00 PM',
        'location': 'Park Community Hall',
        'services': ['Blood Sugar Test', 'HbA1c Test', 'Diet Consultation'],
        'capacity': 80,
        'registered': 32,
        'available': True
    },
    {
        'id': 3,
        'name': 'General Health Checkup',
        'hospital': 'Regional Medical Center',
        'date': '2024-08-25',
        'time': '10:00 AM - 6:00 PM',
        'location': 'School Auditorium',
        'services': ['General Checkup', 'Blood Pressure', 'BMI Assessment'],
        'capacity': 150,
        'registered': 78,
        'available': True
    }
]

users_data = [
    {'email': 'admin@demo.com', 'password': 'admin', 'name': 'Admin User', 'role': 'admin'},
    {'email': 'user@demo.com', 'password': 'user', 'name': 'Demo User', 'role': 'user'}
]

registrations_data = []

@app.route('/')
def home():
    return render_template('home.html', camps=camps_data)

@app.route('/camps')
def camps():
    search = request.args.get('search', '')
    filtered_camps = camps_data
    if search:
        filtered_camps = [camp for camp in camps_data if search.lower() in camp['name'].lower()]
    return render_template('camps.html', camps=filtered_camps, search=search)

@app.route('/camp/<int:camp_id>')
def camp_detail(camp_id):
    camp = next((c for c in camps_data if c['id'] == camp_id), None)
    if not camp:
        flash('Camp not found!', 'error')
        return redirect(url_for('camps'))
    return render_template('camp_detail.html', camp=camp)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        user = next((u for u in users_data if u['email'] == email and u['password'] == password), None)
        if user:
            session['user'] = user
            flash(f'Welcome {user["name"]}!', 'success')
            return redirect(url_for('dashboard' if user['role'] == 'admin' else 'home'))
        else:
            flash('Invalid credentials!', 'error')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        
        if any(u['email'] == email for u in users_data):
            flash('Email already exists!', 'error')
        else:
            users_data.append({
                'email': email,
                'password': password,
                'name': name,
                'role': 'user'
            })
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('Logged out successfully!', 'success')
    return redirect(url_for('home'))

@app.route('/book/<int:camp_id>')
def book_camp(camp_id):
    if 'user' not in session:
        flash('Please login to book a camp!', 'error')
        return redirect(url_for('login'))
    
    camp = next((c for c in camps_data if c['id'] == camp_id), None)
    if camp and camp['registered'] < camp['capacity']:
        registration = {
            'user_email': session['user']['email'],
            'camp_id': camp_id,
            'camp_name': camp['name'],
            'booking_date': datetime.now().strftime('%Y-%m-%d %H:%M')
        }
        registrations_data.append(registration)
        camp['registered'] += 1
        flash('Successfully registered for the camp!', 'success')
    else:
        flash('Camp is full or not available!', 'error')
    
    return redirect(url_for('camp_detail', camp_id=camp_id))

@app.route('/my-bookings')
def my_bookings():
    if 'user' not in session:
        flash('Please login to view bookings!', 'error')
        return redirect(url_for('login'))
    
    user_bookings = [r for r in registrations_data if r['user_email'] == session['user']['email']]
    return render_template('my_bookings.html', bookings=user_bookings)

@app.route('/dashboard')
def dashboard():
    if 'user' not in session or session['user']['role'] != 'admin':
        flash('Admin access required!', 'error')
        return redirect(url_for('login'))
    
    stats = {
        'total_camps': len(camps_data),
        'total_registrations': len(registrations_data),
        'total_capacity': sum(c['capacity'] for c in camps_data),
        'total_registered': sum(c['registered'] for c in camps_data)
    }
    
    return render_template('dashboard.html', camps=camps_data, registrations=registrations_data, stats=stats)

@app.route('/add-camp', methods=['GET', 'POST'])
def add_camp():
    if 'user' not in session or session['user']['role'] != 'admin':
        flash('Admin access required!', 'error')
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        new_camp = {
            'id': len(camps_data) + 1,
            'name': request.form['name'],
            'hospital': request.form['hospital'],
            'date': request.form['date'],
            'time': request.form['time'],
            'location': request.form['location'],
            'services': request.form['services'].split(','),
            'capacity': int(request.form['capacity']),
            'registered': 0,
            'available': True
        }
        camps_data.append(new_camp)
        flash('Camp added successfully!', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('add_camp.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
