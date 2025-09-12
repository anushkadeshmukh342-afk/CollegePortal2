from flask import render_template, request, redirect, url_for, flash, session, send_from_directory, make_response
from app import app, db
from models import *
from datetime import datetime, date
from werkzeug.security import generate_password_hash, check_password_hash
import os
import pytz
ist = pytz.timezone("Asia/Kolkata")

@app.template_filter("ist_time")
def ist_time_filter(value):
    if not value:
        return ""
    utc_time = value.replace(tzinfo=pytz.utc)
    ist_time = utc_time.astimezone(ist)
    return ist_time.strftime("%d-%m-%Y %I:%M %p")

# Enhanced static file route for VSCode and cross-platform compatibility
@app.route('/static/<path:filename>')
def serve_static_files(filename):
    """Custom static file serving route for VSCode and cross-device compatibility"""
    try:
        # Check if file exists in static folder
        file_path = os.path.join('static', filename)
        if not os.path.exists(file_path):
            return f"File not found: {filename}", 404
            
        response = make_response(send_from_directory('static', filename))
        
        # Add proper headers based on file type
        if filename.endswith('.pdf'):
            response.headers['Content-Type'] = 'application/pdf'
            response.headers['Content-Disposition'] = f'inline; filename={os.path.basename(filename)}'
            # Enhanced PDF headers for cross-device compatibility
            response.headers['Accept-Ranges'] = 'bytes'
            response.headers['X-Content-Type-Options'] = 'nosniff'
        elif filename.endswith(('.png', '.jpg', '.jpeg')):
            ext = filename.split(".")[-1].lower()
            response.headers['Content-Type'] = f'image/{"jpeg" if ext == "jpg" else ext}'
        elif filename.endswith('.css'):
            response.headers['Content-Type'] = 'text/css; charset=utf-8'
        elif filename.endswith('.js'):
            response.headers['Content-Type'] = 'application/javascript; charset=utf-8'
            
        # Enhanced caching and security headers for VSCode and development
        response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '0'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, HEAD, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Accept, Accept-Encoding, Authorization, Content-Type'
        
        return response
        
    except Exception as e:
        app.logger.error(f"Error serving static file {filename}: {str(e)}")
        return f"Error loading file: {filename}", 500

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/timetable')
def timetable():
    timetables = Timetable.query.all()
    courses = [c[0] for c in db.session.query(Timetable.course).distinct().all()]
    semesters = [s[0] for s in db.session.query(Timetable.semester).distinct().all()]
    return render_template('timetable.html', timetables=timetables, courses=courses, semesters=semesters)

@app.route('/aarti')
def aarti():
    schedules = AartiSchedule.query.all()
    return render_template('aarti.html', schedules=schedules)

@app.route('/past-papers')
def past_papers():
    papers = PastPaper.query.all()
    courses = [c[0] for c in db.session.query(PastPaper.course).distinct().all()]
    subjects = [s[0] for s in db.session.query(PastPaper.subject).distinct().all()]
    return render_template('past_papers.html', papers=papers, courses=courses, subjects=subjects)

@app.route('/bus-timing')
def bus_timing():
    timings = BusTiming.query.all()
    return render_template('bus_timing.html', timings=timings)

@app.route('/uniform')
def uniform():
    return render_template('uniform.html')

@app.route('/clubs')
def clubs():
    club_list = Club.query.all()
    return render_template('clubs.html', clubs=club_list)

@app.route('/canteen')
def canteen():
    menu_items = CanteenMenu.query.all()
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return render_template('canteen.html', menu_items=menu_items, days=days)

@app.route('/library')
def library():
    books = Book.query.all()
    return render_template('library.html', books=books)

@app.route('/emergency')
def emergency():
    return render_template('emergency.html')

@app.route('/hostel')
def hostel():
    return render_template('hostel.html')

@app.route('/activities')
def activities():
    today = date.today()
    events = Event.query.filter(Event.date >= today).all()
    return render_template('activities.html', events=events, today=today)

@app.route('/auditorium')
def auditorium():
    today = date.today()
    bookings = AuditoriumBooking.query.filter(AuditoriumBooking.date >= today).all()
    return render_template('auditorium.html', bookings=bookings, today=today)

@app.route('/faculty')
def faculty():
    faculty_list = Faculty.query.all()
    departments = [d[0] for d in db.session.query(Faculty.department).distinct().all()]
    return render_template('faculty.html', faculty=faculty_list, departments=departments)

@app.route('/events')
def events():
    event_list = Event.query.all()
    today = date.today()
    return render_template('events.html', events=event_list, today=today)

@app.route('/companies')
def companies():
    company_list = Company.query.all()
    today = date.today()
    return render_template('companies.html', companies=company_list, today=today)

@app.route('/innovation_hub')
def innovation_hub():
    # Redirect to clubs for now, can be customized later
    return redirect(url_for('clubs'))

@app.route('/search')
def search():
    query = request.args.get('q', '')
    if not query:
        return redirect(url_for('index'))
    
    # Search across multiple models with enhanced search
    search_term = f'%{query}%'
    results = {
        'books': Book.query.filter(
            (Book.title.like(search_term)) | 
            (Book.author.like(search_term)) | 
            (Book.subject.like(search_term))
        ).all(),
        'faculty': Faculty.query.filter(
            (Faculty.name.like(search_term)) | 
            (Faculty.department.like(search_term)) | 
            (Faculty.designation.like(search_term))
        ).all(),
        'events': Event.query.filter(
            (Event.title.like(search_term)) | 
            (Event.description.like(search_term)) | 
            (Event.organizer.like(search_term))
        ).all(),
        'clubs': Club.query.filter(
            (Club.name.like(search_term)) | 
            (Club.description.like(search_term))
        ).all(),
        'timetable': Timetable.query.filter(
            (Timetable.subject.like(search_term)) | 
            (Timetable.faculty.like(search_term)) | 
            (Timetable.course.like(search_term))
        ).all(),
        'papers': PastPaper.query.filter(
            (PastPaper.subject.like(search_term)) | 
            (PastPaper.course.like(search_term))
        ).all(),
        'companies': Company.query.filter(
            (Company.name.like(search_term)) | 
            (Company.job_roles.like(search_term))
        ).all()
    }
    
    return render_template('search_results.html', results=results, query=query)
# Comment System Routes
@app.route('/comments')
def comments():
    page = request.args.get('page', 1, type=int)
    per_page = 10
    comments = Comment.query.filter_by(is_visible=True).order_by(Comment.created_at.desc()).paginate(
        page=page, per_page=per_page, error_out=False
    )
    return render_template('comments.html', comments=comments)
@app.route('/add_comment', methods=['POST'])
def add_comment():
    name = request.form.get('name', '').strip()
    email = request.form.get('email', '').strip()
    content = request.form.get('content', '').strip()
    
    if not all([name, email, content]):
        flash('All fields are required.', 'error')
        return redirect(url_for('comments'))
    
    # Basic validation
    if len(name) < 2 or len(name) > 100:
        flash('Name must be between 2 and 100 characters.', 'error')
        return redirect(url_for('comments'))
    
    if len(content) < 10 or len(content) > 1000:
        flash('Comment must be between 10 and 1000 characters.', 'error')
        return redirect(url_for('comments'))
    
    # Create new comment
    comment = Comment(
        name=name,
        email=email,
        content=content,
        ip_address=request.remote_addr
    )
    
    try:
        db.session.add(comment)
        db.session.commit()
        flash('Your comment has been submitted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Error submitting comment. Please try again.', 'error')
    
    return redirect(url_for('comments'))
# Admin Routes
@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # For demo purposes, using simple authentication
        # In production, use proper password hashing
        if username == 'admin' and password == 'admin123':
            session['admin_logged_in'] = True
            flash('Admin login successful!', 'success')
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Invalid credentials!', 'error')
    
    return render_template('admin_login.html')
@app.route('/admin/dashboard')
def admin_dashboard():
    if not session.get('admin_logged_in'):
        flash('Please login to access admin panel.', 'error')
        return redirect(url_for('admin_login'))
    
    # Get all comments for admin review
    comments = Comment.query.order_by(Comment.created_at.desc()).all()
    comment_stats = {
        'total': Comment.query.count(),
        'visible': Comment.query.filter_by(is_visible=True).count(),
        'hidden': Comment.query.filter_by(is_visible=False).count()
    }
    
    return render_template('admin_dashboard.html', comments=comments, stats=comment_stats)
@app.route('/admin/toggle_comment/<int:comment_id>')
def admin_toggle_comment(comment_id):
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    comment = Comment.query.get_or_404(comment_id)
    comment.is_visible = not comment.is_visible
    
    try:
        db.session.commit()
        action = 'shown' if comment.is_visible else 'hidden'
        flash(f'Comment has been {action}.', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Error updating comment.', 'error')
    
    return redirect(url_for('admin_dashboard'))
@app.route('/admin/delete_comment/<int:comment_id>')
def admin_delete_comment(comment_id):
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    comment = Comment.query.get_or_404(comment_id)
    
    try:
        db.session.delete(comment)
        db.session.commit()
        flash('Comment has been deleted.', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Error deleting comment.', 'error')
    
    return redirect(url_for('admin_dashboard'))
@app.route('/admin/logout')
def admin_logout():
    session.pop('admin_logged_in', None)
    flash('Admin logout successful.', 'success')
    return redirect(url_for('index'))

