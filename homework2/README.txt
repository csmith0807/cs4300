Movie Theater Booking Application

This is a RESTful Movie Theater Booking Application built using Django and Django REST Framework.

The application allows users to:
    View available movies
    Book seats for movies
    View their booking history

The application follows Django's MVT (Model-View-Template) architecture and is deployed on Render.

Features: 
    Movie listing page
    Seat booking page
    Booking history page
    Responsive design using Bootstrap
    View seat availability
    Create bookings and view booking history

Project Structure:

/homework2
    /bookings
        /templates
            /bookings
                base.html
                booking_history.html
                login.html
                movie_list.html
                seat_booking.html
            /registration
                login.html
    __init__.py
    admin.py
    apps.py
    models.py 
    serializers.py
    tests.py
    urls.py
    views.py    
    /features
        /steps 
            steps.py 
        booking.feature
        environment.py
        history.feature 
        login.feature 
    /movie_theater_booking
        __init__.py
        asgi.py 
        settings.py 
        urls.py 
        wsgi.py 
    /myenv
    .gitignore
    build.sh
    db.sqlite3
    manage.py 
    Procfile
    README.txt
    render.yaml
    requirements.txt

Local Development Setup Instructions
1. Clone repository
    git clone https://github.com/csmith0807/cs4300.git
    cd homework2
2. Create virtual environment
    python3 -m venv myenv --system-site-packages
    source myenv/bin/activate 
3. Install dependencies 
    pip install -r requirements.txt
4. Apply migrations
    python manage.py migrate
5. Create superuser
    python manage.py createsuperuser
6. Run server
    python manage.py runserver 0.0.0.0:3000
    visit: http://localhost/proxy/3000/
Tests:
    Unit tests:
        python manage.py test
    BDD tests:
        behave

Deployment:
    The application is deployed on Render.
    Live URL:
        https://movie-theater-booking-i818.onrender.com/ 

        Login:
            Username: grader
            Password: graderpass123

AI Usage Disclosure:
    This project used AI assistance (ChatGPT, Claude) for:
        Debugging deployment issues on Render
        Debugging behave test case errors
        Designing UI components/html 
