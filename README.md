# UBC FLow
UBC Flow is a webapp based off of https://uwflow.com/.
It allows users to easily view, rate, and comment on courses at UBC. The purpose of this application is to provide students with information about the courses that are being offered at UBC.

### Set up
1. Clone the repo and step into it
     https://github.com/karenhong/ubcFlow.git
2. Create a virtual environment and install packages
    `virtualenv venv`
    `source venv/bin/activate`
    `pip install -r requirements.txt`
3. Set up the MySQL database (see below)
5. Start the application
    `python ubcFlow.py`
    The application will run on http://localhost:5000/.

If `ModuleNotFoundError: No module named 'MySQLdb'`:
* Try `pip install mysql-python`
* Run using python2 instead of python3
### Setting up the MySQL database
1. In terminal, connect to MySQL by running the command `mysql -u user -p`
2. Create the database `CREATE DATABASE database_name;`
3. `Use database_name`
4. Set the SQLALCHEMY_DATABASE_URI configuration in ubcFlow.py to `mysql://user:password@localhost/database_name`
5. After running the program/creating the tables, run setup.sql to populate the database with some fake data. In the MySQL run, `mysql> \. setup.sql`.

Current database schema:
* User(**email**, first_name, last_name, password)
* Course(**code**, name, description, year)
* Review(**id**, rating, title, message, user_email, course_code)

