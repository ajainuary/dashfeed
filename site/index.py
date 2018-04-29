from flask import Flask
from flask import render_template
from flask import request
import tagsearch
import contentsearch
import registration
import sqlite3
import login
app = Flask(__name__)
@app.route('/article/<int:id>')
def article(id):
	info = sqlite3.connect('../news.db')
	cursor = info.cursor()
	cursor.execute("SELECT * FROM NEWS WHERE id = %d" % id)
	cont = cursor.fetchone()
	img = cont[7].split(',')
	print(cont[5])
	return render_template('article.html', title=cont[1], content=cont[3], image=img[0], id=id,tag=cont[6], url=cont[5])
@app.route('/')
def home():
	info = sqlite3.connect('../news.db')
	cursor = info.cursor()
	cursor.execute("SELECT * FROM NEWS")
	cont = reversed(cursor.fetchall())
	return render_template('index.html', info=cont)
@app.route('/tag/<string:tag>')
def tagView(tag):
	return render_template('index.html', info=tagsearch.searchfunc(tag))
@app.route('/search', methods=['GET'])
def search():
	query = request.args['search']
	return render_template('index.html', info=contentsearch.searchbar(query), query=query)
@app.route('/signup')
def signup():
	return render_template('register.html')
@app.route('/new_user', methods=['POST'])
def newUser():
	email = request.form['email']
	registration.register(email)
	return render_template('login.html',goodPrompt=1)
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     error = None
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         completion = login.validate(username, password)
#         if completion ==False:
#             error = 'Invalid Credentials. Please try again.'
#         else:
#             return redirect(url_for('secret'))
#     return render_template('login.html', error=error)
# @app.route('/secret')
# def secret():
#     return "You have successfully logged in"
if __name__ == '__main__':
    app.run(debug=True)
@app.route('/publish')
def publish():
	return render_template('publish.html')
