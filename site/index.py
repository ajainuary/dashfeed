from flask import Flask
from flask import render_template, redirect
from flask import request
import tagsearch
import contentsearch
import registration
import sqlite3
import loginUtil
from flask import session
from flask import make_response
from flask.ext.uploads import UploadSet, configure_uploads, IMAGES
app = Flask(__name__)
photos = UploadSet('photos', IMAGES)
app.config['UPLOADED_PHOTOS_DEST'] = 'static'
configure_uploads(app, photos)
app.config['SECRET_KEY'] = 'D@SHF33D'
@app.route('/article/<int:id>', methods=['GET', 'POST'])
def article(id):
	info = sqlite3.connect('../news.db')
	cursor = info.cursor()
	cursor.execute("SELECT * FROM NEWS WHERE id = %d" % id)
	cont = cursor.fetchone()
	img = cont[7].split(',')
	if request.method == 'POST':
		comment = request.form['comment']
		cursor.execute('INSERT INTO comment VALUES (?, ?, ?);', (comment, id, session['id'],))
	cursor.execute("SELECT comment.content, user.email FROM comment JOIN user ON comment.user_id = user.id WHERE comment.article_id = %d" % id)
	comments = cursor.fetchall()
	info.commit()
	return render_template('article.html', title=cont[1], content=cont[3], image=img[0], id=id,tag=cont[6], url=cont[5],comments = comments)
@app.route('/')
def home():
	info = sqlite3.connect('../news.db')
	cursor = info.cursor()
	cursor.execute("SELECT * FROM NEWS")
	cont = reversed(cursor.fetchall())
	try:
		print(session['id'])
		return render_template('index.html', info=cont, login=True)
	except:
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
@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		username = request.form['email']
		password = request.form['password']
		completion = loginUtil.validate(username, password)
		print(username, password, completion)
		if completion is None:
			return render_template('login.html', badPrompt=1)
		else:
			session['id'] = completion
			return redirect('')
	else:
		return render_template('login.html')
@app.route('/publish', methods=['GET', 'POST'])
def publish():
	if request.method == 'POST':
		title = request.form['title']
		subtitle = request.form['subtitle']
		content = request.form['editordata']
		tag = request.form['tag']
		filename = photos.save(request.files['file'])
		info = sqlite3.connect('../news.db')
		cursor = info.cursor()
		cursor.execute("SELECT * FROM news ORDER BY id DESC;")
		last = cursor.fetchone()
		cursor.execute('''INSERT INTO NEWS( title, subject, content,rating,link,tags,img)VALUES(?,?,?,?,?,?,?)''', ( title, subtitle, content,0,"dashfeed.com/" + str(last[0]),tag,filename))
		info.commit()
	return render_template('publish.html')
if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, port=80)

