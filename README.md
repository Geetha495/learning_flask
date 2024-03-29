### HOW I CREATED 
- First created virtual environment ( an isolated environment)
  - Installed using : ``` pip install virtualenv ```
  - created using : ``` virtualenv venv ```
  - To activate : ``` source venv/bin/activate/ ```
  - Install Flask in it : ``` pip install Flask ```
  - To deactivate : ``` deactivate ```

- To deploy 
  - create account in heroku.com
  - install local toolbelt from heroku website
  - login using : ```heroku login```

  
- Firstly created folders:

		|_static
			|_ css
				|_ main.css
			|_ img
			|_ js
		|_templates
			|_ layout.html
			|_ index.html
		|_routes.py
		|_README.md

- Run app 
	- type : ``` python3 routes.py ```

- Version Control
	- Create empty repository ```git init ```
	- add all files using ``` git add  ```
	- commit using ``` git commit -m "msg" ```
	- Now create a repos in github.com
	- Use the commands in "or push an existing repository from the command line" category in github" to push of our repos to github
 
- Deploying to heroku
	- First install gunicorn server : ``` pip install gunicorn``` (in venv)
	- create a file named requirements.txt that has all python libraries we install
		- type : ``` pip freeze > requirements.txt ```
	- Create a Procfile ( ``` touch Procfile ```) that tells heroku to run Flask using gunicorn
	- type inside Procfile : ```web: gunicorn routes:app```
	- Create new heroku app : ``` heroku create ```
	- commit the new files (Procfile, requirements.txt)
	- Deploy using : ```git push heroku HEAD:master```
	- To open app : ```heroku open```

- Connecting to Database
  - Install Postgresql (pgAdmin4)
  - Create a database (learningflask) and  create a table(users) ( using querytool)
  - To connect to this database from flask
	- First install flask_sqlalchemy using : ``` pip install flask-sqlalchemy ``` (in venv)
	- Next, we configure the flask app to use learningflask database by (in routes.py) 
	```
		app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:<your_password>@localhost:5432/learningflask'
	```
	- Now we make a new file called models.py , this has a datastructure which helps flask read/ write data from users table. This datastructure is called model.
	- Create a instance of 	``SQLAlchemy()`` call it ``db``, and create a new class which has base class db.Model
	- To store password in encrypted form, we use a hash function.
		- Install werkzeug : ``` pip install Werkzeug ```
		- Import it and use the functions in it like generate_password_hash
	- Now, to intialse the app using database setup : ``` db.init_app(app) ```

- Creating forms 
	- To create forms, we can use python extension WebTestFroms ``Flask-WTF``
	- Install it : ``` pip install flask-wtf ```
	- Now we make a new file called forms.py,import ``Form`` and create Class SignupForm whose base class is ``Form``, in which we can declare validators,...
	- Create a instance of 	``SQLAlchemy()`` call it ``db``, and create a new class which has base class db.Model
	- We create method : POST for forms, so, in routes.py, we check validation and return success or error accordingly.

- Storing to database 
	- First create an Users instance by intialised it with request data
	- Now use ``` db.session.add(user)``` to add, ``` db.session.commit()``` to commit.
	- Here we may get an error that ``` module : psycopg2 ot found ```, then install it by ``` pip install psycopg2-binary```

- Creating session
	- what is a session?
		- After user signs in, app needs to identify page request to serve the user.
		- The app sets a cookie in the browser containing an ID
		- For each subsequent request, the id is passed on the app.
		- App checks if this ID matches the user credentials, If does, then app responds with relevant info
		- This process is called session.
	- Import session from flask. And do ```session['email']=newuser.email```
	- When user logins/signups then new session is created.
	- When user logouts then the session is deleted.	

- Authorization :
	- when a user enters url for home, without logging in, we should redirect user to login page
	- When a user enters url for login/signup after logging in, then user should be redirected to home page
	- This can be done with help of session dictionary, by checking whether email is already present or not.
	
- About my code 
	- In routes.py, flask app is created using ```Flask(__name__)```
	- In layout.html, just layout is written , and for index.html code block, we wrote
		```
			{% block content %}
			{% endblock %}
		```
	- In index.html, we wrote 
		- at start :
			```
				{% extends "layout.html" %}
				{% block content %}
			```
		
		- and at end :
			```
				{% endblock %}
			```
	- To integrate this, we wrote in routes.py the below code:
		```
			def index():
        			return render_template("index.html")
		```
	- Add about page :
		- write code for about page and add layout by the previous commands
		- In routes.py, add below code
			```
				@app.route("/about")
				def about():
					return render_template("about.html")
			```
		- To link this to learn more button :
			```
				<a href="{{ url_for('about')}}" class="btn-secondary">LEARN MORE</a>
			```
		- push all changes to github
		- To deploy these changes to heroku, type : ``` git push heroku HEAD:master  ```

	
		

