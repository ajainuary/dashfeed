from flask import Flask
from flask import render_template
from flask import request
import tagsearch
import contentsearch
import sqlite3
app = Flask(__name__)
@app.route('/article/<int:id>')
def article(id):
	info = sqlite3.connect('../news.db')
	cursor = info.cursor()
	cursor.execute("SELECT * FROM NEWS WHERE id = %d" % id)
	cont = cursor.fetchone()
	img = cont[7].split(',')
	return render_template('article.html', title=cont[1], content=cont[3], image=img[0], id=id)
@app.route('/')
def home():
	info = sqlite3.connect('../news.db')
	cursor = info.cursor()
	cursor.execute("SELECT * FROM NEWS")
	cont = cursor.fetchall()
	return render_template('index.html', info=cont)
@app.route('/tag/<string:tag>')
def tagView(tag):
	return render_template('index.html', info=tagsearch.searchfunc(tag))
@app.route('/search', methods=['GET'])
def search():
	print(request.args)
	query = request.args['search']
	return render_template('index.html', info=contentsearch.searchbar(query), query=query)
