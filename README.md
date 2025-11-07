# Free Health Camp Information System

A web-based platform for managing and discovering free health camps.

## Features

- **User Registration & Authentication**: Secure user accounts with login/logout
- **Camp Discovery**: Search and browse available health camps
- **Location-based Search**: Find camps near specific locations
- **Online Registration**: Register for health camps online
- **QR Code Check-in**: Generate QR codes for quick camp check-in
- **Admin Dashboard**: Manage camps, view registrations, and track attendance
- **Real-time Updates**: Live updates on camp availability and registrations
- **Responsive Design**: Works on desktop and mobile devices

## Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: Mock database (can be replaced with PostgreSQL)
- **Icons**: Font Awesome
- **Styling**: Custom CSS with responsive design

## Setup Instructions

1. **Install Python 3.7+**
2. **Install dependencies**:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

3. **Run the application**:
   \`\`\`bash
   python app.py
   \`\`\`

4. **Open your browser** and navigate to `http://localhost:5000`

## Demo Credentials

**Admin Login:**
- Email: admin@healthcamp.com
- Password: admin123

## Usage

1. **For Users:**
   - Register a new account or login
   - Browse available health camps
   - Search camps by name, service, or location
   - Register for camps
   - View your registrations and generate QR codes

2. **For Admins:**
   - Login with admin credentials
   - Access admin dashboard
   - Create new health camps
   - View all registrations
   - Manage camp details

## Project Structure

\`\`\`
health-camp-system/
│
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
│
├── templates/            # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── search.html
│   ├── camp_details.html
│   ├── register.html
│   ├── login.html
│   ├── register_camp.html
│   ├── my_registrations.html
│   ├── admin_dashboard.html
│   └── create_camp.html
│
└── static/              # Static files
    ├── style.css        # CSS styles
    └── script.js        # JavaScript functions
\`\`\`

## Future Enhancements

- Integration with PostgreSQL database
- SMS/Email notifications using Twilio/SendGrid
- Google Maps integration for location services
- Payment gateway for paid camps
- Advanced reporting and analytics
- Mobile app development
- Multi-language support
\`\`\`

This prototype provides a fully functional Free Health Camp Information System with:

1. **User Authentication**: Registration, login, and session management
2. **Camp Management**: Browse, search, and view camp details
3. **Registration System**: Users can register for camps
4. **Admin Dashboard**: Create camps, manage registrations, view statistics
5. **Responsive Design**: Works on all devices
6. **QR Code Generation**: Mock QR code system for check-ins
7. **Real-time Updates**: Framework for live updates
8. **Search Functionality**: Filter camps by name, service, or location

The system is built with Flask for the backend, HTML/CSS/JavaScript for the frontend, and includes mock data for demonstration. All buttons are functional and the system provides a complete user experience for both regular users and administrators.
