Call for Proposals website
==========================

::

    git clone
    cd pybay_front_end
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

    # Create project, app and consolidate cfg with django-admin and mv commands
    ./manage.py migrate
    ./manage.py loaddata fixtures/*
    ./manage.py runserver

    # For testing purposes use the admin interface with user: test and password: test
