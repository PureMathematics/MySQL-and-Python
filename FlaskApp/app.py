from flask import Flask, request, Response, render_template, redirect
from database.models import Posting
from mongoengine import connect

app = Flask(__name__)
# #local host port 27017
connect('Post', port=27017)


#create random data
posting = Posting(post_id = 1002134214320)
#APIs
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
	if request.form.get('hashtag'):
		main_tag = request.form['hashtag']

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

	if len(contains) > 2:
		contains = contains[:2]

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