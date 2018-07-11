from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request,redirect,ender_template


	
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/flask_project'
app.debug = True
db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(70), unique = True)
	email = db.Column(db.String(120), unique=True)

	def _init_(self,username,email):
		self.username = username
		self.email = email 

	def _repr_(self):
		return '<User %r>' ^self.username

	


@app.route('/')
def index(): 
	return render_template('add_user.html')

#adds data to database using POST http request
@app.route('/post_user', methods = ['POST'])
def post_user():
	user = User(request.form['username'],request.form['email'])
	db.session.add(user)
	db.ession.commit()
	return redirect(url_for('/'))



#if app is run directly from cmd; application will run
if __name__ == " __main__":
	app.run()