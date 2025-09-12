
from app import app, db
from models import *
from datetime import datetime, date, timedelta
import random

def init_sample_data():
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()
        
        print("Adding sample data...")
        
        # Sample Timetable Data
        courses = ['Computer Engineering', 'Information Technology', 'Electronics Engineering', 'Mechanical Engineering', 'Civil Engineering']
        semesters = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th']
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        time_slots = ['9:00-10:00', '10:00-11:00', '11:15-12:15', '12:15-1:15', '2:00-3:00', '3:00-4:00', '4:15-5:15']
        
        subjects = {
            'Computer Engineering': ['Data Structures', 'Database Management', 'Computer Networks', 'Software Engineering', 'Operating Systems', 'Web Development'],
            'Information Technology': ['Programming', 'System Analysis', 'IT Project Management', 'Cybersecurity', 'Cloud Computing', 'Mobile App Development'],
            'Electronics Engineering': ['Digital Electronics', 'Microprocessors', 'VLSI Design', 'Communication Systems', 'Control Systems', 'Signal Processing'],
            'Mechanical Engineering': ['Thermodynamics', 'Fluid Mechanics', 'Machine Design', 'Manufacturing Technology', 'CAD/CAM', 'Automobile Engineering'],
            'Civil Engineering': ['Structural Analysis', 'Transportation Engineering', 'Environmental Engineering', 'Construction Management', 'Surveying', 'Geotechnical Engineering']
        }
        
        faculty_names = ['Dr. Rajesh Sharma', 'Prof. Priya Patel', 'Dr. Anil Kumar', 'Prof. Sunita Joshi', 'Dr. Rahul Mehta', 'Prof. Kavita Singh', 'Dr. Suresh Gupta', 'Prof. Anjali Desai']
        rooms = ['A-101', 'A-102', 'B-201', 'B-202', 'C-301', 'C-302', 'Lab-1', 'Lab-2', 'Lab-3']
        
        timetable_entries = []
        for course in courses[:3]:  # First 3 courses
            for semester in semesters[:4]:  # First 4 semesters
                for day in days:
                    for i, time_slot in enumerate(time_slots[:4]):  # 4 classes per day
                        if random.choice([True, True, True, False]):  # 75% chance of having class
                            subject = random.choice(subjects[course])
                            faculty = random.choice(faculty_names)
                            room = random.choice(rooms)
                            
                            timetable_entries.append(Timetable(
                                course=course,
                                semester=semester,
                                subject=subject,
                                day=day,
                                time_slot=time_slot,
                                faculty=faculty,
                                room=room
                            ))
        
        db.session.add_all(timetable_entries)
        
        # Sample Aarti Schedule
        aarti_schedules = [
            AartiSchedule(day='Monday', time='7:00 AM', location='College Temple', description='Morning Aarti - Peaceful start to the week'),
            AartiSchedule(day='Tuesday', time='7:00 AM', location='College Temple', description='Morning Aarti - Seeking blessings for studies'),
            AartiSchedule(day='Wednesday', time='7:00 AM', location='College Temple', description='Morning Aarti - Spiritual guidance'),
            AartiSchedule(day='Thursday', time='7:00 AM', location='College Temple', description='Morning Aarti - Divine wisdom'),
            AartiSchedule(day='Friday', time='7:00 AM', location='College Temple', description='Morning Aarti - Week completion prayers'),
            AartiSchedule(day='Saturday', time='7:00 AM', location='College Temple', description='Morning Aarti - Special weekend prayers'),
            AartiSchedule(day='Sunday', time='8:00 AM', location='College Temple', description='Extended Sunday Aarti with community gathering')
        ]
        db.session.add_all(aarti_schedules)
        
        # Sample Past Papers
        exam_types = ['Mid Semester', 'End Semester', 'Internal Assessment', 'Practical Exam']
        years = [2023, 2022, 2021, 2020, 2019]
        
        past_papers = []
        for course in courses:
            for subject in subjects[course]:
                for year in years[:3]:  # Last 3 years
                    for exam_type in exam_types[:2]:  # 2 exam types
                        past_papers.append(PastPaper(
                            subject=subject,
                            course=course,
                            semester=random.choice(semesters[:6]),
                            year=year,
                            exam_type=exam_type,
                            file_path=f'/papers/{course.replace(" ", "_")}_{subject.replace(" ", "_")}_{year}_{exam_type.replace(" ", "_")}.pdf'
                        ))
        
        db.session.add_all(past_papers[:50])  # Add first 50 papers
        
        # Sample Bus Timings
        bus_timings = [
            BusTiming(route_name='Amravati Station - College', departure_time='7:30 AM', departure_location='Amravati Railway Station', arrival_time='8:00 AM', arrival_location='College Main Gate', bus_number='AP-101'),
            BusTiming(route_name='City Center - College', departure_time='8:00 AM', departure_location='City Center Bus Stand', arrival_time='8:25 AM', arrival_location='College Main Gate', bus_number='AP-102'),
            BusTiming(route_name='Rajkamal - College', departure_time='7:45 AM', departure_location='Rajkamal Square', arrival_time='8:15 AM', arrival_location='College Main Gate', bus_number='AP-103'),
            BusTiming(route_name='College - Amravati Station', departure_time='5:30 PM', departure_location='College Main Gate', arrival_time='6:00 PM', arrival_location='Amravati Railway Station', bus_number='AP-101'),
            BusTiming(route_name='College - City Center', departure_time='5:45 PM', departure_location='College Main Gate', arrival_time='6:10 PM', arrival_location='City Center Bus Stand', bus_number='AP-102'),
            BusTiming(route_name='College - Rajkamal', departure_time='5:15 PM', departure_location='College Main Gate', arrival_time='5:45 PM', arrival_location='Rajkamal Square', bus_number='AP-103'),
        ]
        db.session.add_all(bus_timings)
        
        # Sample Clubs with WhatsApp Group Links
        clubs = [
            Club(name='Coding Club', description='Learn programming, participate in hackathons, and build amazing projects together.', contact_person='Arjun Patel', contact_email='codingclub@prpcem.ac.in', meeting_day='Friday', meeting_time='4:00 PM', whatsapp_link='https://chat.whatsapp.com/CEPUgOpnSuoJDZwJjgdQLa?mode=ac_t'),
            Club(name='Robotics Club', description='Design, build, and program robots. Participate in national level competitions.', contact_person='Sneha Sharma', contact_email='robotics@prpcem.ac.in', meeting_day='Wednesday', meeting_time='3:30 PM', whatsapp_link='https://chat.whatsapp.com/EnmmHYdn2tsFCM037Vzp89'),
            Club(name='Drama Society', description='Express creativity through theater, participate in cultural events and competitions.', contact_person='Rahul Joshi', contact_email='drama@prpcem.ac.in', meeting_day='Tuesday', meeting_time='5:00 PM'),
            Club(name='Photography Club', description='Capture moments, learn photography techniques, and document college events.', contact_person='Priya Singh', contact_email='photography@prpcem.ac.in', meeting_day='Saturday', meeting_time='2:00 PM', whatsapp_link='https://chat.whatsapp.com/C4tqoBVQam330Glszl7mnA'),
            Club(name='Music Club', description='Sing, play instruments, and perform at college events and festivals.', contact_person='Amit Gupta', contact_email='music@prpcem.ac.in', meeting_day='Thursday', meeting_time='4:30 PM', whatsapp_link='https://chat.whatsapp.com/K2k50ehzu2YGjFpzsXm4XU'),
            Club(name='Dance Club', description='Learn various dance forms and showcase talent at cultural programs.', contact_person='Kavita Desai', contact_email='dance@prpcem.ac.in', meeting_day='Monday', meeting_time='5:30 PM'),
            Club(name='Literary Society', description='Enhance writing skills, organize debates, and publish college magazine.', contact_person='Dr. Sunita Mehta', contact_email='literary@prpcem.ac.in', meeting_day='Friday', meeting_time='3:00 PM'),
            Club(name='Environment Club', description='Promote sustainability, organize tree plantation drives, and environmental awareness.', contact_person='Ravi Kumar', contact_email='environment@prpcem.ac.in', meeting_day='Saturday', meeting_time='10:00 AM'),
            Club(name='Sports Club', description='Organize sports events, tournaments, and promote fitness among students.', contact_person='Coach Rajesh', contact_email='sports@prpcem.ac.in', meeting_day='Daily', meeting_time='6:00 AM', whatsapp_link='https://chat.whatsapp.com/KV3qaOcuRbfBYeGDUgJEvO'),
            Club(name='E-Cell (Innovation Club)', description='Foster entrepreneurship, startup ideas, and innovation projects. Join our entrepreneurship community!', contact_person='Dr. Anil Sharma', contact_email='innovation@prpcem.ac.in', meeting_day='Wednesday', meeting_time='2:00 PM', whatsapp_link='https://chat.whatsapp.com/DgTiWKJQxuIJsVy1ZsEJH9?mode=ac_t')
        ]
        db.session.add_all(clubs)
        
        # Sample Canteen Menu
        menu_items = [
            # Monday
            CanteenMenu(day='Monday', meal_type='breakfast', item_name='Poha', price=25.0),
            CanteenMenu(day='Monday', meal_type='breakfast', item_name='Tea/Coffee', price=10.0),
            CanteenMenu(day='Monday', meal_type='lunch', item_name='Dal Rice', price=60.0),
            CanteenMenu(day='Monday', meal_type='lunch', item_name='Chapati Sabji', price=50.0),
            CanteenMenu(day='Monday', meal_type='dinner', item_name='Rajma Rice', price=70.0),
            
            # Tuesday
            CanteenMenu(day='Tuesday', meal_type='breakfast', item_name='Upma', price=30.0),
            CanteenMenu(day='Tuesday', meal_type='breakfast', item_name='Tea/Coffee', price=10.0),
            CanteenMenu(day='Tuesday', meal_type='lunch', item_name='Chole Bhature', price=80.0),
            CanteenMenu(day='Tuesday', meal_type='lunch', item_name='Salad', price=20.0),
            CanteenMenu(day='Tuesday', meal_type='dinner', item_name='Paneer Curry', price=90.0),
            
            # Wednesday
            CanteenMenu(day='Wednesday', meal_type='breakfast', item_name='Paratha', price=35.0),
            CanteenMenu(day='Wednesday', meal_type='breakfast', item_name='Curd', price=15.0),
            CanteenMenu(day='Wednesday', meal_type='lunch', item_name='Biryani', price=120.0),
            CanteenMenu(day='Wednesday', meal_type='lunch', item_name='Raita', price=25.0),
            CanteenMenu(day='Wednesday', meal_type='dinner', item_name='Mixed Vegetable', price=65.0),
            
            # Thursday
            CanteenMenu(day='Thursday', meal_type='breakfast', item_name='Idli Sambar', price=40.0),
            CanteenMenu(day='Thursday', meal_type='breakfast', item_name='Coconut Chutney', price=15.0),
            CanteenMenu(day='Thursday', meal_type='lunch', item_name='South Indian Thali', price=100.0),
            CanteenMenu(day='Thursday', meal_type='lunch', item_name='Pickle', price=10.0),
            CanteenMenu(day='Thursday', meal_type='dinner', item_name='Sambar Rice', price=55.0),
            
            # Friday
            CanteenMenu(day='Friday', meal_type='breakfast', item_name='Sandwich', price=45.0),
            CanteenMenu(day='Friday', meal_type='breakfast', item_name='Fresh Juice', price=30.0),
            CanteenMenu(day='Friday', meal_type='lunch', item_name='Special Thali', price=110.0),
            CanteenMenu(day='Friday', meal_type='lunch', item_name='Sweet Dish', price=35.0),
            CanteenMenu(day='Friday', meal_type='dinner', item_name='Fried Rice', price=75.0),
            
            # Saturday
            CanteenMenu(day='Saturday', meal_type='breakfast', item_name='Dosa', price=50.0),
            CanteenMenu(day='Saturday', meal_type='breakfast', item_name='Tea/Coffee', price=10.0),
            CanteenMenu(day='Saturday', meal_type='lunch', item_name='Gujarati Thali', price=95.0),
            CanteenMenu(day='Saturday', meal_type='lunch', item_name='Buttermilk', price=20.0),
            CanteenMenu(day='Saturday', meal_type='dinner', item_name='Pasta', price=85.0),
            
            # Sunday
            CanteenMenu(day='Sunday', meal_type='breakfast', item_name='Puri Bhaji', price=55.0),
            CanteenMenu(day='Sunday', meal_type='breakfast', item_name='Lassi', price=25.0),
            CanteenMenu(day='Sunday', meal_type='lunch', item_name='Special Sunday Meal', price=130.0),
            CanteenMenu(day='Sunday', meal_type='lunch', item_name='Ice Cream', price=40.0),
            CanteenMenu(day='Sunday', meal_type='dinner', item_name='Chinese Combo', price=100.0),
        ]
        db.session.add_all(menu_items)
        
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
        
        # Sample Events
        today = date.today()
        events = [
            Event(title='Annual Technical Fest - TechnoVision 2024', description='Three-day technical festival featuring competitions, workshops, and exhibitions from leading tech companies.', date=today + timedelta(days=15), time='9:00 AM', venue='College Auditorium & Campus', organizer='Technical Committee'),
            Event(title='Industry Expert Lecture on AI/ML', description='Renowned AI researcher from IIT Bombay will discuss latest trends in machine learning and career opportunities.', date=today + timedelta(days=7), time='2:00 PM', venue='Seminar Hall A', organizer='Computer Engineering Department'),
            Event(title='Cultural Night - Rang Bhoomi', description='Showcase of student talents in music, dance, drama, and literary arts. Open to all students and faculty.', date=today + timedelta(days=22), time='6:00 PM', venue='Main Auditorium', organizer='Cultural Committee'),
            Event(title='Sports Championship 2024', description='Inter-branch sports competition including cricket, football, basketball, volleyball, and athletics.', date=today + timedelta(days=30), time='8:00 AM', venue='Sports Complex', organizer='Sports Committee'),
            Event(title='Entrepreneurship Workshop', description='Learn about startup ecosystem, funding opportunities, and how to convert ideas into successful businesses.', date=today + timedelta(days=10), time='10:00 AM', venue='Innovation Hub', organizer='E-Cell & Innovation Club'),
            Event(title='Blood Donation Camp', description='Annual blood donation drive in association with Red Cross Society. Help save lives by donating blood.', date=today + timedelta(days=5), time='9:00 AM', venue='College Hospital', organizer='NSS & Red Cross'),
            Event(title='Green Campus Initiative Launch', description='Launch of environmental sustainability program including solar energy, waste management, and tree plantation.', date=today + timedelta(days=12), time='11:00 AM', venue='Central Lawn', organizer='Environment Club'),
            Event(title='Alumni Meet 2024', description='Annual gathering of alumni to share experiences, network, and celebrate achievements. Guest lecture by successful entrepreneurs.', date=today + timedelta(days=45), time='10:00 AM', venue='Convention Center', organizer='Alumni Association')
        ]
        db.session.add_all(events)
        
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
        
        # Sample Auditorium Bookings
        auditorium_bookings = [
            AuditoriumBooking(event_name='Department Seminar - Latest Trends in AI', date=today + timedelta(days=3), start_time='10:00 AM', end_time='12:00 PM', organizer='Computer Engineering Dept', contact='+91 7212 234567'),
            AuditoriumBooking(event_name='Student Orientation Program', date=today + timedelta(days=8), start_time='9:00 AM', end_time='4:00 PM', organizer='Dean Student Affairs', contact='+91 7212 234568'),
            AuditoriumBooking(event_name='Cultural Program Practice', date=today + timedelta(days=12), start_time='5:00 PM', end_time='8:00 PM', organizer='Cultural Committee', contact='+91 7212 234569'),
            AuditoriumBooking(event_name='Guest Lecture by Industry Expert', date=today + timedelta(days=16), start_time='2:00 PM', end_time='4:00 PM', organizer='Training & Placement Cell', contact='+91 7212 234570'),
            AuditoriumBooking(event_name='Annual Prize Distribution', date=today + timedelta(days=25), start_time='10:00 AM', end_time='1:00 PM', organizer='Principal Office', contact='+91 7212 234571'),
            AuditoriumBooking(event_name='Research Paper Presentation', date=today + timedelta(days=19), start_time='1:00 PM', end_time='5:00 PM', organizer='Research Committee', contact='+91 7212 234572')
        ]
        db.session.add_all(auditorium_bookings)
        
        # Sample Comments
        comments = [
            Comment(name='Arjun Patel', email='arjun.patel@student.prpcem.ac.in', content='Great initiative! The QR code system makes accessing information so much easier. Love the new campus portal!', ip_address='192.168.1.100'),
            Comment(name='Sneha Sharma', email='sneha.sharma@student.prpcem.ac.in', content='The timetable feature is incredibly helpful. No more confusion about class schedules. Thank you for this!', ip_address='192.168.1.101'),
            Comment(name='Rahul Joshi', email='rahul.joshi@student.prpcem.ac.in', content='Amazing work on the website. The canteen menu feature helps me plan my meals better. Keep it up!', ip_address='192.168.1.102'),
            Comment(name='Priya Singh', email='priya.singh@student.prpcem.ac.in', content='The bus timing information is very accurate and helpful for daily commute. Great job by the development team!', ip_address='192.168.1.103'),
            Comment(name='Amit Gupta', email='amit.gupta@student.prpcem.ac.in', content='Love the clean design and easy navigation. The club information section helped me join the coding club!', ip_address='192.168.1.104')
        ]
        db.session.add_all(comments)
        
        # Commit all changes
        db.session.commit()
        print("Sample data added successfully!")
        
        # Print summary
        print(f"\nData Summary:")
        print(f"- Timetable entries: {len(timetable_entries)}")
        print(f"- Aarti schedules: {len(aarti_schedules)}")
        print(f"- Past papers: 50")
        print(f"- Bus timings: {len(bus_timings)}")
        print(f"- Clubs: {len(clubs)}")
        print(f"- Menu items: {len(menu_items)}")
        print(f"- Books: {len(books)}")
        print(f"- Faculty: {len(faculty_list)}")
        print(f"- Events: {len(events)}")
        print(f"- Companies: {len(companies)}")
        print(f"- Auditorium bookings: {len(auditorium_bookings)}")
        print(f"- Comments: {len(comments)}")

if __name__ == '__main__':
    init_sample_data()
