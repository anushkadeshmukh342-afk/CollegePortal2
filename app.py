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
    from models import Event, AartiSchedule, Club, Faculty, Timetable, PastPaper, Company, Book
    from datetime import datetime, date, timedelta
    import random
    
    print("Adding sample data...")
    
    # Sample Events (including OneDrive events)
    today = date.today()
    events = [
    
        # Events with OneDrive PDF links
        Event(title='Techloans 2025', description='Annual technical symposium showcasing innovative projects and latest technology trends', date=date(2025, 1, 20), time='11:00 AM', venue='College Campus', organizer='Technical Committee', file_path='https://1drv.ms/b/c/ADA7036725D1B12A/EZryKikeNmdKkC7xfAbsdbQBTWihCgdU8NxwwhLV53RQwg?e=e7wWyV'),
        Event(title='Ganesh Utsav 2025', description='Grand celebration of Lord Ganesha festival with cultural programs and community participation', date=date(2025, 8, 29), time='11:00 AM', venue='College Campus', organizer='Cultural Committee', file_path='https://1drv.ms/b/c/ADA7036725D1B12A/EW2QfhDjW3RNik6ypI3yuCUB9wtV_8fYB4L7XoIUYTW1yg?e=xZaxIv'),
        Event(title='DJ Night 2025', description='Electrifying DJ night with music, dance and entertainment for all students', date=date(2025, 1, 26), time='7:00 PM', venue='Open Ground', organizer='Cultural Committee', file_path='https://1drv.ms/b/c/ADA7036725D1B12A/Ef5jDnU5BotJqtcWeKK0M-YBMevaDWfJuUNp3qcNqgpImA?e=rzMAqQ'),
        Event(title='Dindi Procession 2025', description='Traditional Dindi procession celebrating cultural heritage and community spirit', date=date(2025, 1, 23), time='9:00 AM', venue='Gajanana Maharaj Panchvati Mandir, Pote Township', organizer='Cultural Committee', file_path='https://1drv.ms/b/c/ADA7036725D1B12A/EfnLwM5prPtJrqDw3xqMlY8BskAHuh6xIlIKWWOayNgR3w?e=0h4us7'),
        Event(title='Dahi Handi Festival 2025', description='Exciting Dahi Handi celebration with teams competing and traditional festivities', date=date(2025, 9, 2), time='11:00 AM', venue='Sports Ground', organizer='Cultural Committee', file_path='https://1drv.ms/b/c/ADA7036725D1B12A/Ed-Sl0HSkZpPkOCVbEYW43sBbWbJLwU0okd3y4hhuOXeyQ?e=IPzzYo')
    ]
    db.session.add_all(events)
    
    # Sample Past Papers (with OneDrive PDF links)
    past_papers = [
        PastPaper(
            subject='Previous Year Questions',
            course='Civil & Mechanical Engineering',
            semester='1st & 2nd',
            year=2024,
            exam_type='Previous Year Papers',
            file_path='https://1drv.ms/b/c/ADA7036725D1B12A/ERdRFwjLSYJAt_0wbSWVHywB89ZZX9TRSioW7yIGK7oO9A?e=S8OOIu'
        ),
        PastPaper(
            subject='Computer Science & Engineering',
            course='CSE, AIML, AIDS',
            semester='1st Semester',
            year=2024,
            exam_type='Previous Year Papers',
            file_path='https://1drv.ms/b/c/ADA7036725D1B12A/EdE_G7qJcIFKj4A3-ygXm4QBrayr2iIs1WVT408FwTBACA?e=yV9PAJ'
        ),
        PastPaper(
            subject='Computer Science & Engineering',
            course='CSE, AIML, AIDS',
            semester='2nd Semester',
            year=2024,
            exam_type='Previous Year Papers',
            file_path='https://1drv.ms/b/c/ADA7036725D1B12A/EeTM_7qqUIpFqN5B2TYR0cIBu5fEvfIGQ9kcacA59qaDbA?e=Yop1XP'
        ),
        PastPaper(
            subject='Previous Year Questions',
            course='Electrical Engineering',
            semester='1st & 2nd',
            year=2024,
            exam_type='Previous Year Papers',
            file_path='https://1drv.ms/b/c/ADA7036725D1B12A/EXLLcl17hiBJtljouBb8jd0BiuO1tnqXZSAkTi9FmCxDIg?e=Gczz3n'
        ),
        PastPaper(
            subject='Previous Year Questions',
            course='Electronics Engineering',
            semester='1st & 2nd',
            year=2024,
            exam_type='Previous Year Papers',
            file_path='https://1drv.ms/b/c/ADA7036725D1B12A/EV9yikp-acVLnPsad7bqUK0BvAhWTwXnxF19bBNV4mxc4Q?e=lQdXUf'
        )
    ]
    db.session.add_all(past_papers)
    
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
        Club(name='GDG on Campus - PRPCEM', description='Learn Google technologies, join hackathons, and collaborate on innovative projects with peers.', contact_person='Arjun Patel', contact_email='codingclub@prpcem.ac.in', meeting_day='Friday', meeting_time='4:00 PM', whatsapp_link='https://chat.whatsapp.com/CEPUgOpnSuoJDZwJjgdQLa?mode=ac_t'),
        Club(name='THE ORATORY CLUB 📣✨', description='Build confidence, master public speaking, and express your voice with impact.', contact_person='Sneha Sharma', contact_email='robotics@prpcem.ac.in', meeting_day='Wednesday', meeting_time='3:30 PM', whatsapp_link='https://chat.whatsapp.com/EnmmHYdn2tsFCM037Vzp89'),
        Club(name='E Cell General Assembly', description='Ignite your entrepreneurial spirit, share ideas, and shape future innovations.', contact_person='Priya Singh', contact_email='photography@prpcem.ac.in', meeting_day='Saturday', meeting_time='2:00 PM', whatsapp_link='https://chat.whatsapp.com/C4tqoBVQam330Glszl7mnA'),
        Club(name='ANTARNAAD CLUB', description='Celebrate music, rhythm, and the art of soulful performances.', contact_person='Dr. Anil Sharma', contact_email='innovation@prpcem.ac.in', meeting_day='Wednesday', meeting_time='2:00 PM', whatsapp_link='https://chat.whatsapp.com/DgTiWKJQxuIJsVy1ZsEJH9?mode=ac_t'),
        Club(name='CODING_CLUB_PRPCEM', description='Sharpen coding skills, solve challenges, and innovate with peers.', contact_person='Coach Rajesh', contact_email='sports@prpcem.ac.in', meeting_day='Daily', meeting_time='6:00 AM', whatsapp_link='https://chat.whatsapp.com/KV3qaOcuRbfBYeGDUgJEvO'),
        Club(name='🚨TECHELONS’25🚨', description='Annual technical fest celebrating innovation, talent, and futuristic ideas.', contact_person='Amit Gupta', contact_email='music@prpcem.ac.in', meeting_day='Thursday', meeting_time='4:30 PM', whatsapp_link='https://chat.whatsapp.com/K2k50ehzu2YGjFpzsXm4XU')
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
    
    # Sample Books
    books = [
            Book(title='Data Structures and Algorithms', author='Cormen, Leiserson, Rivest', isbn='978-0262033848', subject='Computer Science', available_copies=15, total_copies=20),
            Book(title='Database System Concepts', author='Silberschatz, Galvin, Gagne', isbn='978-0073523323', subject='Database Management', available_copies=12, total_copies=18),
            Book(title='Computer Networks', author='Andrew Tanenbaum', isbn='978-0132126953', subject='Networking', available_copies=8, total_copies=15),
            Book(title='Operating System Concepts', author='Galvin, Gagne, Silberschatz', isbn='978-1118063330', subject='Operating Systems', available_copies=10, total_copies=16),
            Book(title='Engineering Mathematics', author='B.S. Grewal', isbn='978-8174091451', subject='Mathematics', available_copies=25, total_copies=30),
            Book(title='Thermodynamics', author='Cengel & Boles', isbn='978-0073398174', subject='Mechanical Engineering', available_copies=14, total_copies=20),
            Book(title='Digital Electronics', author='Morris Mano', isbn='978-0132145398', subject='Electronics', available_copies=11, total_copies=18),
            Book(title='Structural Analysis', author='R.C. Hibbeler', isbn='978-0134610672', subject='Civil Engineering', available_copies=9, total_copies=15),
            Book(title='Programming in C', author='Dennis Ritchie', isbn='978-0131103627', subject='Programming', available_copies=20, total_copies=25),
            Book(title='Engineering Physics', author='Gaur & Gupta', isbn='978-8173714498', subject='Physics', available_copies=18, total_copies=22)
        ]
    db.session.add_all(books)

    # Sample Faculty
    faculty_list = [
            Faculty(name='Dr. Rajesh Sharma', department='Computer Engineering', designation='Professor & HOD', email='rajesh.sharma@prpcem.ac.in', phone='+91 7212 234567', cabin_number='A-201'),
            Faculty(name='Prof. Priya Patel', department='Information Technology', designation='Associate Professor', email='priya.patel@prpcem.ac.in', phone='+91 7212 234568', cabin_number='B-105'),
            Faculty(name='Dr. Anil Kumar', department='Electronics Engineering', designation='Professor', email='anil.kumar@prpcem.ac.in', phone='+91 7212 234569', cabin_number='C-301'),
            Faculty(name='Prof. Sunita Joshi', department='Mechanical Engineering', designation='Assistant Professor', email='sunita.joshi@prpcem.ac.in', phone='+91 7212 234570', cabin_number='D-202'),
            Faculty(name='Dr. Rahul Mehta', department='Civil Engineering', designation='Professor & Dean', email='rahul.mehta@prpcem.ac.in', phone='+91 7212 234571', cabin_number='Admin-301'),
            Faculty(name='Prof. Kavita Singh', department='Computer Engineering', designation='Associate Professor', email='kavita.singh@prpcem.ac.in', phone='+91 7212 234572', cabin_number='A-205'),
            Faculty(name='Dr. Suresh Gupta', department='Information Technology', designation='Professor', email='suresh.gupta@prpcem.ac.in', phone='+91 7212 234573', cabin_number='B-108'),
            Faculty(name='Prof. Anjali Desai', department='Electronics Engineering', designation='Assistant Professor', email='anjali.desai@prpcem.ac.in', phone='+91 7212 234574', cabin_number='C-205'),
            Faculty(name='Dr. Vikram Shah', department='Mechanical Engineering', designation='Professor', email='vikram.shah@prpcem.ac.in', phone='+91 7212 234575', cabin_number='D-301'),
            Faculty(name='Prof. Ritu Agarwal', department='Civil Engineering', designation='Associate Professor', email='ritu.agarwal@prpcem.ac.in', phone='+91 7212 234576', cabin_number='E-102')
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
