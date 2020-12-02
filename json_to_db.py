import json
import os
import glob
import requests
import csv

def data_from_json(filename, tf):
	with open(filename) as f:
		filecity = filename.split('/')
		cityname = filecity[-1][:-4]
		tf.write("City: " + filename + "\n")
		print("City: " + filename + "\n")
		data = json.load(f)
		for i in range(0, len(data['GraphImages'])):
			print(i)
			tf.write("Index: " + str(i) + "\n")
			display_url = data['GraphImages'][i]['display_url']
			likes = int(data['GraphImages'][i]['edge_liked_by']['count'])
			if data['GraphImages'][i]['edge_media_to_caption']['edges']:
				caption = data['GraphImages'][i]['edge_media_to_caption']['edges'][0]['node']['text']
			comments = int(data['GraphImages'][i]['edge_media_to_comment']['count'])
			post_id = data['GraphImages'][i]['id']
			is_video = data['GraphImages'][i]['is_video']
			owner_id = data['GraphImages'][i]['owner']['id']
			shortcode = data['GraphImages'][i]['shortcode']
			tags = data['GraphImages'][i].get('tags')
			timestamp = data['GraphImages'][i]['taken_at_timestamp']
			im_640 = data['GraphImages'][i]['thumbnail_resources'][4]['src']

			# Get locations
			url = "https://www.instagram.com/p/{0}/?__a=1".format(shortcode)
			r = requests.get(url)
			data1 = json.loads(r.text)
			try:
				location = data1['graphql']['shortcode_media']['location']['name'] # get location for a post
			except:
				location = '' # if location is NULL
			try:
				username = data1['graphql']['shortcode_media']['owner']['username']
				profile_pic = data1['graphql']['shortcode_media']['owner']['profile_pic_url']
			except:
				username = ''
				profile_pic = ''
				
			tf.write("username: " + username + "\n")
			tf.write("profile_pic: " + profile_pic + "\n")
			tf.write("display_url: " + display_url + "\n")
			tf.write("likes: " + str(likes) + "\n")
			tf.write("caption: " + caption + "\n")
			tf.write("comments: " + str(comments) + "\n")
			tf.write("post_id: " + post_id + "\n")
			tf.write("is_video: " + str(is_video) + "\n")
			tf.write("owner_id: " + owner_id + "\n")
			tf.write("shortcode: " + shortcode + "\n")
			tf.write("locations: " + location + "\n")
			if (tags == None):
				tf.write("tags: \n")
			else:
				tf.write("tags: " + ', '.join((tags)) + "\n")
			tf.write("timestamp: " + str(timestamp) + "\n")
			tf.write("im_640: " + im_640 + "\n")
			tf.write("\n")

def json_to_txt(json_path, tf):
	all_jsons = glob.glob(json_path + "*.json")
	for filename in all_jsons:
		data_from_json(filename, tf)

if __name__ == "__main__":
	json_path = os.getcwd() + "/jsons/"

	tf = open("temp_db.txt", "w+")
	json_to_txt(json_path, tf)

	# tokyopath = json_path + "/tokyo.json"
	# data_from_json(tokyopath, tf)
