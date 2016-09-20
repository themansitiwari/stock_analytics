

* Fork this repository.
* `$ git clone git@github.com:<your username>/stock_analytics.git`
* `$ virtualenv stock_analytics_venv`
* `$ source stock_analytics_venv/bin/activate`
* `$ cd stock_analytics/`
* `$ pip install -r requirements.txt`
* `$ npm install -g bower`
* `$ npm install`
* `$ bower install`
* `$ python manage.py migrate`
* `$ python manage.py runserver`
* To set up the database -
* Login to the database
* `$ mysql -uusername -p`
* `CREATE DATABASE stock_analytics;`
* `USE stock_analytics;`
* `exit`
* Use the file stock_analytics_dump.sql to load the database
* `mysql -u username -p stock_analytics < stock_analytics_dump.sql`
* You might have to restart your server to see the data