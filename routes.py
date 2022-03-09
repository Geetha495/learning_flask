from flask import Flask, render_template, request
from models import db, User
from forms import SignupForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:dbpassword@localhost:5432/learningflask'
db.init_app(app)

app.secret_key = 'development-key'

@app.route("/")
def index():
        return render_template("index.html")

@app.route("/about")
def about():
        return render_template("about.html")


@app.route("/signup",methods=['GET','POST'])
def signup():        
        if request.method == 'POST':
                form = SignupForm(request.form)
                if form.validate() == False:
                        return render_template('signup.html',form=form)
                else:
                        newuser = User(form.first_name.data,form.last_name.data,form.email.data,form.password.data)
                        db.session.add(newuser)
                        db.session.commit()
                        return "SUCCESS!!"
                
        elif request.method=='GET':
                form = SignupForm()
                return render_template('signup.html',form=form)
       


if __name__ == "__main__":
        app.run(debug=True)