import os
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

# Configure logging for debugging
logging.basicConfig(level=logging.DEBUG)

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

# Create the Flask app with enhanced static file configuration for VSCode compatibility
app = Flask(__name__, 
            static_folder='static', 
            static_url_path='/static')
app.secret_key = os.environ.get("SESSION_SECRET", "dev_secret_key_change_in_production")

# Configure database
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///college.db")
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_recycle": 300,
    "pool_pre_ping": True,
}

# Initialize the app with the extension
db.init_app(app)

# Import routes after app creation
from routes import *

def init_sample_data():
    """Initialize database with sample data including events with OneDrive links"""
    from models import Event, AartiSchedule, Club, Faculty, Timetable
    from datetime import datetime, date, timedelta
    import random
    
    print("Adding sample data...")
    
    # Sample Events (including OneDrive events)
    today = date.today()
    events = [
    
        # Events with OneDrive PDF links
        Event(title='TechnoLean 2024', description='Annual technical symposium showcasing innovative projects and latest technology trends', date=date(2025, 10, 15), time='9:00 AM', venue='Main Auditorium', organizer='Technical Committee', file_path='https://1drv.ms/b/c/ADA7036725D1B12A/EZryKikeNmdKkC7xfAbsdbQBTWihCgdU8NxwwhLV53RQwg?e=e7wWyV'),
        Event(title='Ganpati Bappa Celebration', description='Grand celebration of Lord Ganesha festival with cultural programs and community participation', date=date(2025, 9, 29), time='10:00 AM', venue='College Campus', organizer='Cultural Committee', file_path='https://1drv.ms/b/c/ADA7036725D1B12A/EW2QfhDjW3RNik6ypI3yuCUB9wtV_8fYB4L7XoIUYTW1yg?e=xZaxIv'),
        Event(title='DJ Night 2024', description='Electrifying DJ night with music, dance and entertainment for all students', date=date(2025, 10, 25), time='7:00 PM', venue='Open Ground', organizer='Cultural Committee', file_path='https://1drv.ms/b/c/ADA7036725D1B12A/Ef5jDnU5BotJqtcWeKK0M-YBMevaDWfJuUNp3qcNqgpImA?e=rzMAqQ'),
        Event(title='Dindi Procession', description='Traditional Dindi procession celebrating cultural heritage and community spirit', date=date(2025, 10, 5), time='6:00 AM', venue='College to Temple Route', organizer='Cultural Committee', file_path='https://1drv.ms/b/c/ADA7036725D1B12A/EfnLwM5prPtJrqDw3xqMlY8BskAHuh6xIlIKWWOayNgR3w?e=0h4us7'),
        Event(title='Dahi Handi Festival', description='Exciting Dahi Handi celebration with teams competing and traditional festivities', date=date(2025, 8, 30), time='11:00 AM', venue='Sports Ground', organizer='Cultural Committee', file_path='https://1drv.ms/b/c/ADA7036725D1B12A/Ed-Sl0HSkZpPkOCVbEYW43sBbWbJLwU0okd3y4hhuOXeyQ?e=IPzzYo')
    ]
    db.session.add_all(events)
    
    # Add essential sample data for other modules
    # Sample Aarti Schedule
    aarti_schedules = [
        AartiSchedule(day='Monday', time='11:00 AM', location='College Main Building', description='Morning Aarti - Peaceful start to the week'),
        AartiSchedule(day='Tuesday', time='11:00 AM', location='College Main Building', description='Morning Aarti - Seeking blessings for studies'),
        AartiSchedule(day='Wednesday', time='11:00 AM', location='College Main Building', description='Morning Aarti - Spiritual guidance'),
        AartiSchedule(day='Thursday', time='11:00 AM', location='College Main Buildinge', description='Morning Aarti - Divine wisdom'),
        AartiSchedule(day='Friday', time='11:00 AM', location='College Main Building', description='Morning Aarti - Week completion prayers'),
        AartiSchedule(day='Saturday', time='11:00 AM', location='College Main Building', description='Morning Aarti - Special weekend prayers')
    ]
    db.session.add_all(aarti_schedules)
    
    # Sample Clubs
    clubs = [
        Club(name='Coding Club', description='Learn programming, participate in hackathons, and build amazing projects together.', contact_person='Arjun Patel', contact_email='codingclub@prpcem.ac.in', meeting_day='Friday', meeting_time='4:00 PM', whatsapp_link='https://chat.whatsapp.com/CEPUgOpnSuoJDZwJjgdQLa?mode=ac_t'),
        Club(name='Robotics Club', description='Design, build, and program robots. Participate in national level competitions.', contact_person='Sneha Sharma', contact_email='robotics@prpcem.ac.in', meeting_day='Wednesday', meeting_time='3:30 PM', whatsapp_link='https://chat.whatsapp.com/EnmmHYdn2tsFCM037Vzp89'),
        Club(name='Photography Club', description='Capture moments, learn photography techniques, and document college events.', contact_person='Priya Singh', contact_email='photography@prpcem.ac.in', meeting_day='Saturday', meeting_time='2:00 PM', whatsapp_link='https://chat.whatsapp.com/C4tqoBVQam330Glszl7mnA'),
        Club(name='E-Cell (Innovation Club)', description='Foster entrepreneurship, startup ideas, and innovation projects. Join our entrepreneurship community!', contact_person='Dr. Anil Sharma', contact_email='innovation@prpcem.ac.in', meeting_day='Wednesday', meeting_time='2:00 PM', whatsapp_link='https://chat.whatsapp.com/DgTiWKJQxuIJsVy1ZsEJH9?mode=ac_t'),
        Club(name='Sports Club', description='Organize sports events, tournaments, and promote fitness among students.', contact_person='Coach Rajesh', contact_email='sports@prpcem.ac.in', meeting_day='Daily', meeting_time='6:00 AM', whatsapp_link='https://chat.whatsapp.com/KV3qaOcuRbfBYeGDUgJEvO'),
        Club(name='Music Club', description='Sing, play instruments, and perform at college events and festivals.', contact_person='Amit Gupta', contact_email='music@prpcem.ac.in', meeting_day='Thursday', meeting_time='4:30 PM', whatsapp_link='https://chat.whatsapp.com/K2k50ehzu2YGjFpzsXm4XU')
    ]
    db.session.add_all(clubs)
    
    # Sample Companies
    companies = [
            Company(name='Tata Consultancy Services (TCS)', visit_date=today + timedelta(days=20), job_roles='Software Developer, System Analyst, Consultant', package_offered='3.5-6.0 LPA', students_placed=45),
            Company(name='Infosys Limited', visit_date=today + timedelta(days=25), job_roles='Software Engineer, Technology Analyst', package_offered='4.0-7.0 LPA', students_placed=38),
            Company(name='Wipro Technologies', visit_date=today + timedelta(days=18), job_roles='Project Engineer, Software Developer', package_offered='3.8-6.5 LPA', students_placed=32),
            Company(name='Mahindra & Mahindra', visit_date=today + timedelta(days=35), job_roles='Design Engineer, Manufacturing Engineer', package_offered='4.5-8.0 LPA', students_placed=28),
            Company(name='L&T Technology Services', visit_date=today + timedelta(days=28), job_roles='Software Engineer, Embedded Engineer', package_offered='4.2-7.5 LPA', students_placed=22),
            Company(name='Tech Mahindra', visit_date=today + timedelta(days=40), job_roles='Associate Software Engineer, Network Engineer', package_offered='3.6-6.2 LPA', students_placed=35),
            Company(name='Capgemini', visit_date=today + timedelta(days=32), job_roles='Analyst Programmer, Senior Analyst', package_offered='4.8-8.5 LPA', students_placed=25),
            Company(name='Accenture', visit_date=today + timedelta(days=22), job_roles='Application Development Analyst, Technology Consultant', package_offered='5.0-9.0 LPA', students_placed=30),
            Company(name='Cognizant Technology Solutions', visit_date=today + timedelta(days=15), job_roles='Programmer Analyst, Associate Developer', package_offered='4.1-7.2 LPA', students_placed=42),
            Company(name='HCL Technologies', visit_date=today + timedelta(days=38), job_roles='Software Engineer, Technical Lead', package_offered='3.9-6.8 LPA', students_placed=33)
        ]
    db.session.add_all(companies)

    # Sample Faculty
    faculty_list = [
        Faculty(name='Dr. Rajesh Sharma', department='Computer Engineering', designation='Professor & HOD', email='rajesh.sharma@prpcem.ac.in', phone='+91 7212 234567', cabin_number='A-201'),
        Faculty(name='Prof. Priya Patel', department='Computer Engineering', designation='Associate Professor', email='priya.patel@prpcem.ac.in', phone='+91 7212 234568', cabin_number='B-105'),
        Faculty(name='Dr. Anil Kumar', department='Electronics Engineering', designation='Professor', email='anil.kumar@prpcem.ac.in', phone='+91 7212 234569', cabin_number='C-301')
    ]
    db.session.add_all(faculty_list)
    
    
    # Commit all changes
    db.session.commit()
    print("Sample data added successfully!")

with app.app_context():
    # Import models to ensure tables are created
    import models
    db.create_all()
    
    # Initialize sample data if database is empty
    from models import Event
    if Event.query.count() == 0:
        print("Database is empty, initializing with sample data...")
        init_sample_data()
        print("Sample data initialized successfully!")

if __name__ == '__main__':
    # Enhanced configuration for Replit compatibility
    app.run(host='0.0.0.0', port=5001, debug=True, threaded=True)
