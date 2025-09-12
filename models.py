from app import db
from datetime import datetime

class Timetable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.String(100), nullable=False)
    semester = db.Column(db.String(20), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    day = db.Column(db.String(20), nullable=False)
    time_slot = db.Column(db.String(50), nullable=False)
    faculty = db.Column(db.String(100), nullable=False)
    room = db.Column(db.String(50), nullable=False)

class AartiSchedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.String(20), nullable=False)
    time = db.Column(db.String(20), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)

class PastPaper(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(100), nullable=False)
    course = db.Column(db.String(100), nullable=False)
    semester = db.Column(db.String(20), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    exam_type = db.Column(db.String(50), nullable=False)
    file_path = db.Column(db.String(200))

class BusTiming(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    route_name = db.Column(db.String(100), nullable=False)
    departure_time = db.Column(db.String(20), nullable=False)
    departure_location = db.Column(db.String(100), nullable=False)
    arrival_time = db.Column(db.String(20), nullable=False)
    arrival_location = db.Column(db.String(100), nullable=False)
    bus_number = db.Column(db.String(20))

class Club(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    contact_person = db.Column(db.String(100))
    contact_email = db.Column(db.String(100))
    meeting_day = db.Column(db.String(20))
    meeting_time = db.Column(db.String(20))
    whatsapp_link = db.Column(db.String(500))

class CanteenMenu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.String(20), nullable=False)
    meal_type = db.Column(db.String(20), nullable=False)  # breakfast, lunch, dinner
    item_name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    isbn = db.Column(db.String(20))
    subject = db.Column(db.String(100))
    available_copies = db.Column(db.Integer, default=0)
    total_copies = db.Column(db.Integer, default=0)

class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    designation = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    cabin_number = db.Column(db.String(20))

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.String(20))
    venue = db.Column(db.String(100))
    organizer = db.Column(db.String(100))
    file_path = db.Column(db.String(200))  # Path to event PDF

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    visit_date = db.Column(db.Date, nullable=False)
    job_roles = db.Column(db.Text)
    package_offered = db.Column(db.String(50))
    students_placed = db.Column(db.Integer, default=0)

class AuditoriumBooking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(200), nullable=False)
    date = db.Column(db.Date, nullable=False)
    start_time = db.Column(db.String(20), nullable=False)
    end_time = db.Column(db.String(20), nullable=False)
    organizer = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(20))

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_visible = db.Column(db.Boolean, default=True)
    ip_address = db.Column(db.String(45))  # For tracking purposes   
class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    is_active = db.Column(db.Boolean, default=True)