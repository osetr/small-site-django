Task
====
This small site provides the ability to add posts to the database and view them. All services are containerized, so you have the ability to quickly deploy this site anywhere. Follow instructions below.

After cloning this repository locally, be sure to add yourself .env file with important keys for the database and for the app server itself inside current folder. In the following formats:


* SECRET_KEY = 'ffd3fccf1...eca3d111' (can be genereted by `$openssl rand -hex 32`)
* PASSWORD = 'password' (mysql_db password for root user)

Check http://127.0.0.1:8000/cv/add/

All in all, tjis site has only 2 endpoints:

/cv/add/ - add post;

/cv/show/ - show al posts;
