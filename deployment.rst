Deployment in Linode
====================

::

    sudo su
    apt-get install --no-install-recommends git libapache2-mod-wsgi-py3 python3-venv python3-pip
    cd /data
    git clone https://github.com/mzdaniel/pybay_front_end
    cd pybay_front_end
    python3 -m venv venv
    source venv/bin/activate
    pip3 install -r requirements.txt
    ./manage.py migrate
    ./manage.py loaddata fixtures/*
    cp apache2.conf /etc/apache2/sites-available/000-default.conf
    chown -R www-data.www-data /data/pybay_front_end
    /etc/init.d/apache2 restart
