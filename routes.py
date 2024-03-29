from flask import Flask, render_template, request, session, redirect, url_for
from models import db, User
from forms import SignupForm, LoginForm, AddressForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:dbpassword@localhost:5432/learningflask'
db.init_app(app)

app.secret_key = 'development-key'

@app.route("/")
def index():
        return render_template("index.html")

@app.route("/home",methods=['GET','POST'])
def home():
        if 'email' not in session:
                return redirect(url_for('login'))
        if request.method == 'GET':
                form = AddressForm()
                return render_template("home.html",form=form)
        if request.method == 'POST':
                form = AddressForm(request.form)
                if form.validate() == False:
                        return render_template('home.html',form=form)
                


@app.route("/about")
def about():
        return render_template("about.html")


@app.route("/signup",methods=['GET','POST'])
def signup(): 
        if 'email' in session:
                return redirect(url_for('home'))       
        if request.method == 'POST':
                form = SignupForm(request.form)
                if form.validate() == False:
                        return render_template('signup.html',form=form)
                else:
                        newuser = User(form.first_name.data,form.last_name.data,form.email.data,form.password.data)
                        db.session.add(newuser)
                        db.session.commit()
                        session['email']=newuser.email
                        return redirect(url_for('home'))                
        elif request.method=='GET':
                form = SignupForm()
                return render_template('signup.html',form=form)
       
@app.route('/login', methods=['GET','POST'])
def login():
        if 'email' in session:
                return redirect(url_for('home'))  
        if request.method == 'GET':
                form = LoginForm()
                return render_template('login.html',form=form)
        elif request.method=='POST':
                form = LoginForm(request.form)
                if form.validate() == False:
                        return render_template('login.html',form=form)
                else:
                        email = form.email.data
                        password = form.password.data
                        user = User.query.filter_by(email=email).first()
                        if user is not None and user.check_password(password):
                                session['email']=email
                                return redirect(url_for('home'))
                        else:
                                return redirect(url_for('login'))


@app.route('/logout')
def logout():
        session.pop('email',None)
        return redirect(url_for('index'))
                                 

if __name__ == "__main__":
        app.run(debug=False)