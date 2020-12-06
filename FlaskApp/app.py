from flask import Flask, request, Response, render_template, redirect
from database.models import Posting
from mongoengine import connect
import json

app = Flask(__name__)
# #local host port 27017
connect('Post', port=27017)


#JSON PARSING and Saving into DB
with open('../json_db_lite.json') as json_file:
	data = json.load(json_file)
	for p in data['post']:
		posting = Posting(post_id = p['post_id'],likes = p['likes'], main_tag = p['main_tag'], contains = p['contains'], timestamp = p['timestamp'], locations = p['locations'], username = p['username'], im_640 = p['im_640'])

def get_query_main_tag_likes_comments(input1,input2, input3):
	myquery = {"main_tag": input1, "likes":{ "$gt": input2 }, "comments":{ "$gt": input3 }}
	return mycol.find(myquery,{"im_640":1, "username":1, "main_tag":1, "likes":0, "comments":0, "locations":0, "contains":0, "post_id":0, "timestamp":0})

def get_query_main_tag_likes_comments(input1,input2, input3):
	myquery = {"main_tag": input1, "likes":{ "$gt": input2 }, "comments":{ "$gt": input3 }}
	return mycol.find(myquery,{"im_640":1, "username":1, "main_tag":1, "likes":0, "comments":0, "locations":0, "contains":0, "post_id":0, "timestamp":0})

def get_query_main_tag_likes(input1, input2):
	myquery = {"main_tag": input1, "likes":{ "$gt": input2 }}
	return mycol.find(myquery,{"im_640":1, "username":1, "main_tag":1, "likes":0, "comments":0, "locations":0, "contains":0, "post_id":0, "timestamp":0})

def get_query_main_tag_comments(input1):
	myquery = {"main_tag": input1, "comments":{ "$gt": input1 }}
	return mycol.find(myquery,{"im_640":1, "username":1, "main_tag":1, "likes":0, "comments":0, "locations":0, "contains":0, "post_id":0, "timestamp":0})

def get_query_comments_likes(input1, input2):
	myquery = {"likes": { "$gt": input2 }, "comments":{ "$gt": input2 }}
	return mycol.find(myquery,{"im_640":1, "username":1, "main_tag":1, "likes":0, "comments":0, "locations":0, "contains":0, "post_id":0, "timestamp":0})

def get_query_main_tag(input1):
	myquery = {"main_tag": input1}
	return mycol.find(myquery,{"im_640":1, "username":1, "main_tag":1, "likes":0, "comments":0, "locations":0, "contains":0, "post_id":0, "timestamp":0})

def get_query_comments(input1):
	myquery = {"comments" : { "$gt": input1 }}
	return mycol.find(myquery,{"im_640":1, "username":1, "main_tag":1, "likes":0, "comments":0, "locations":0, "contains":0, "post_id":0, "timestamp":0})

def get_query_likes(input1):
	myquery = {"likes" : { "$gt": input1 }}
	return mycol.find(myquery,{"im_640":1, "username":1, "main_tag":1, "likes":0, "comments":0, "locations":0, "contains":0, "post_id":0, "timestamp":0})

def get_query_contains(input1):
	myquery = {"contains" : input1}
	return mycol.find(myquery,{"im_640":1, "username":1, "main_tag":1, "likes":0, "comments":0, "locations":0, "contains":0, "post_id":0, "timestamp":0})

def get_query_main_tag_contains(input1, input2):
	myquery = {"contains": input1, "main_tag": input2}
	return mycol.find(myquery,{"im_640":1, "username":1, "main_tag":1, "likes":0, "comments":0, "locations":0, "contains":0, "post_id":0, "timestamp":0})

main_tag_list = []
image_list = []
contains_list = []
username_list = []
likes_list = []
comments_list = []
locations_list = []

#https://mongoengine-odm.readthedocs.io/guide/querying.html
#for query operators
#taiwan_users = Posting.objects(location='taiwan')

# TESTING
with open('../json_db_lite.json') as json_file:
	data = json.load(json_file)
	for p in data['post']:
		main_tag_list.append(p['main_tag'])
		image_list.append(p['im_640'])
		username_list.append(p['username'])
		likes_list.append(p['likes'])
		comments_list.append(p['comments'])
		locations_list.append(p['locations'])
		if p['contains']:
			contains_list.append(p['contains'])
		else:
			contains_list.append("")

def get_main_tag_likes_comments_query(input1, input2, input3):
	indices = []
	for i, data in enumerate(likes_list):
		if int(data) >= int(input2):
			indices.append(i)
	iml1 = [image_list[i] for i in indices]
	usl1 = [username_list[i] for i in indices]
	mlt1 = [main_tag_list[i] for i in indices]
	cl1 = [comments_list[i] for i in indices]

	indices2 = []
	for i, data in enumerate(cl1):
		if int(data) >= int(input3):
			indices2.append(i)
	iml2 = [iml1[i] for i in indices2]
	usl2 = [usl1[i] for i in indices2]
	mlt2 = [mlt1[i] for i in indices2]

	indices3 = []
	for i, data in enumerate(mlt2):
		for k in input1:
			if data == k:
				indices3.append(i)
	iml = [iml2[i] for i in indices3]
	usl = [usl2[i] for i in indices3]
	mlt = [mlt2[i] for i in indices3]
	return mlt, usl, iml

def get_comments_likes_query(input1, input2):
	print(input1)
	print(input2)
	indices = []
	print("LENGTH IMG LIST")
	print(len(image_list))
	for i, data in enumerate(likes_list):
		if int(data) >= int(input1):
			indices.append(i)
	iml1 = [image_list[i] for i in indices]
	usl1 = [username_list[i] for i in indices]
	mlt1 = [main_tag_list[i] for i in indices]
	cl1 = [comments_list[i] for i in indices]

	indices2 = []
	for i, data in enumerate(cl1):
		if int(data) >= int(input2):
			indices2.append(i)

	iml2 = [iml1[i] for i in indices2]
	usl2 = [usl1[i] for i in indices2]
	mlt2 = [mlt1[i] for i in indices2]
	return mlt2, usl2, iml2

def get_main_tag_comments_query(input1, input2):
	indices = []
	for i, data in enumerate(comments_list):
		if int(data) >= int(input2):
			indices.append(i)
	iml1 = [image_list[i] for i in indices]
	usl1 = [username_list[i] for i in indices]
	mlt1 = [main_tag_list[i] for i in indices]

	indices2 = []
	for i, data in enumerate(mlt1):
		for k in input1:
			if data == k:
				indices2.append(i)
	iml = [iml1[i] for i in indices2]
	usl = [usl1[i] for i in indices2]
	mlt = [mlt1[i] for i in indices2]
	return mlt, usl, iml

def get_main_tag_likes_query(input1, input2):
	indices = []
	for i, data in enumerate(likes_list):
		if int(data) >= int(input2):
			indices.append(i)
	iml1 = [image_list[i] for i in indices]
	usl1 = [username_list[i] for i in indices]
	mlt1 = [main_tag_list[i] for i in indices]
	indices2 = []
	for i, data in enumerate(mlt1):
		for k in input1:
			if data == k:
				indices2.append(i)
	iml = [iml1[i] for i in indices2]
	usl = [usl1[i] for i in indices2]
	mlt = [mlt1[i] for i in indices2]
	return mlt, usl, iml

def get_comments_query(input):
	indices = []
	for i, data in enumerate(comments_list):
		if int(data) >= int(input):
			indices.append(i)

	iml = [image_list[i] for i in indices]
	usl = [username_list[i] for i in indices]
	mlt = [main_tag_list[i] for i in indices]
	return mlt, usl, iml

def get_likes_query(input):
	indices = []
	for i, data in enumerate(likes_list):
		if int(data) >= int(input):
			indices.append(i)

	iml = [image_list[i] for i in indices]
	usl = [username_list[i] for i in indices]
	mlt = [main_tag_list[i] for i in indices]
	return mlt, usl, iml

def get_main_tag_query(input):
	indices = []
	for i, data in enumerate(main_tag_list):
		for k in input:
			if data == k:
				indices.append(i)

	iml = [image_list[i] for i in indices]
	usl = [username_list[i] for i in indices]
	mlt = [main_tag_list[i] for i in indices]
	return mlt, usl, iml

def get_contains_query(input):
	indices = []
	for i, data in enumerate(contains_list):
		# print(data)
		for j in range(0, len(data)):
			if data[j] == input[0]:
				indices.append(i)

	iml = [image_list[i] for i in indices]
	usl = [username_list[i] for i in indices]
	mlt = [main_tag_list[i] for i in indices]
	return mlt, usl, iml

def get_main_tag_contains_query(input, ml, us, im):
	indices = []
	for i, data in enumerate(ml):
		for k in input:
			if data == k:
				indices.append(i)

	iml1 = [im[i] for i in indices]
	usl1 = [us[i] for i in indices]
	mlt1 = [ml[i] for i in indices]
	return mlt1, usl1, iml1

with open('../json_db_lite.json') as json_file:
	data = json.load(json_file)
#https://mongoengine-odm.readthedocs.io/guide/querying.html
#for query operators
#taiwan_users = Posting.objects(location='taiwan')

@app.route("/", methods=['GET'])
def main():
	return render_template('index.html')

@app.route('/querying', methods=['GET', 'POST'])
def querying():
	contains = []
	images = False
	users = False
	numbers = False
	min_likes = 0
	min_comments = 0
	main_tag = ""

	if request.form.get('images'):
		images = request.form['images']
	if request.form.get('users'):
		users = request.form['users']
	if request.form.get('numbers'):
		numbers = request.form['numbers']
	if request.form.get('min_likes'):
		min_likes = request.form['min_likes']
	if request.form.get('min_comments'):
		min_comments = request.form['min_comments']
		print(min_comments)
	if request.form.get('hashtag'):
		main_tag = request.form['hashtag']
		main_tag = main_tag.split(',')

	if request.form.get('c_oneperson'):
		contains.append(request.form['c_oneperson'])
	if request.form.get('c_onemoreperson'):
		contains.append(request.form['c_onemoreperson'])
	if request.form.get('c_twopeople'):
		contains.append(request.form['c_twopeople'])

	if request.form.get('c_peoplestanding'):
		contains.append('standing')
		contains.append(request.form['c_peoplestanding'])

	if request.form.get('c_outdoor'):
		contains.append(request.form['c_outdoor'])
	if request.form.get('c_indoor'):
		contains.append(request.form['c_indoor'])
	if request.form.get('c_sky'):
		contains.append(request.form['c_sky'])
	if request.form.get('c_night'):
		contains.append(request.form['c_night'])
	if request.form.get('c_water'):
		contains.append(request.form['c_water'])

	if request.form.get('c_peoplesitting'):
		contains.append('sitting')
		contains.append(request.form['c_peoplesitting'])

	if request.form.get('c_food'):
		contains.append(request.form['c_food'])
	if request.form.get('c_drink'):
		contains.append(request.form['c_drink'])
	if request.form.get('c_closeup'):
		contains.append(request.form['c_closeup'])

	if request.form.get('c_hat'):
		contains.append(request.form['c_hat'])
	if request.form.get('c_nature'):
		contains.append(request.form['c_nature'])
	if request.form.get('c_plant'):
		contains.append(request.form['c_plant'])
	if request.form.get('c_bridge'):
		contains.append(request.form['c_bridge'])
	if request.form.get('c_beard'):
		contains.append(request.form['c_beard'])
	if request.form.get('c_sunglasses'):
		contains.append(request.form['c_sunglasses'])

	if request.form.get('cycle'):
		cycle = request.form['cycle']

	if request.form.get('season'):
		season = request.form['season']

	if len(contains) > 1:
		contains = contains[0]

	if main_tag != "" and min_likes != 0 and min_comments != 0:
		ml, us, im = get_main_tag_likes_comments_query(main_tag, min_likes, min_comments)
		return render_template('displaying.html', ml = ml, us = us, im = im, main_tag = main_tag, min_likes = min_likes, min_comments = min_comments)

	elif contains:
		print(contains)
		ml, us, im = get_contains_query(contains)
		if main_tag != "":
			ml, us, im = get_main_tag_contains_query(main_tag, ml, us, im)
		return render_template('displaying.html', ml = ml, us = us, im = im, main_tag = main_tag, contains = contains)

	elif main_tag == "" and min_likes != 0 and min_comments != 0:
		ml, us, im = get_comments_likes_query(min_likes, min_comments)
		return render_template('displaying.html', ml = ml, us = us, im = im, min_likes = min_likes, min_comments = min_comments, contains = contains)	
	
	elif main_tag != "" and min_likes == 0 and min_comments != 0:
		ml, us, im = get_main_tag_comments_query(main_tag, min_comments)
		return render_template('displaying.html', ml = ml, us = us, im = im, main_tag = main_tag, min_comments = min_comments, contains = contains)		

	elif main_tag != "" and min_likes != 0 and min_comments == 0:
		ml, us, im = get_main_tag_likes_query(main_tag, min_likes)
		return render_template('displaying.html', ml = ml, us = us, im = im, main_tag = main_tag, min_comments = min_comments, contains = contains)

	elif main_tag != "" and min_likes == 0 and min_comments == 0:
		ml, us, im = get_main_tag_query(main_tag)
		return render_template('displaying.html', ml = ml, us = us, im = im, main_tag = main_tag, contains = contains)

	elif main_tag == "" and min_likes == 0 and min_comments != 0:
		ml, us, im = get_comments_query(min_comments)
		return render_template('displaying.html', ml = ml, us = us, im = im, min_comments = min_comments, contains = contains)

	elif main_tag == "" and min_likes != 0 and min_comments == 0:
		ml, us, im = get_likes_query(min_likes)
		return render_template('displaying.html', ml = ml, us = us, im = im, min_likes = min_likes, contains = contains)

	# images = False
	# users = False
	# numbers = False
	# min_likes = 0
	# min_comments = 0
	# main_tag = ""
	# contains

	return render_template('displaying.html')
	# return render_template('greeting.html', say=request.form['say'], to=request.form['to'])

if __name__ == "__main__":
	app.run(port=5002,debug=True)