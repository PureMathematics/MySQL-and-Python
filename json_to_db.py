import json
import os
import glob
import requests
import csv

import datetime

def data_from_json_text(filename, of, pl):
	count = 0
	with open(filename) as f:
		filecity = filename.split('/')[-1]
		filecity1 = filecity.split('_',1)[0]
		main_tag = filecity1
		print("City: " + filecity1)
		data = json.load(f)
		for i in range(0, len(data['GraphImages'])):
			print(i)
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
			if (tags == None):
				tags = ""
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
				acc_cap = data1['graphql']['shortcode_media']['accessibility_caption']
			except:
				username = ''
				profile_pic = ''
				acc_cap = ''

			if (post_id not in pl):
				of.write("Index: " + str(i) + "\n")
				of.write("city: " + main_tag + "\n")
				of.write("username: " + username + "\n")
				of.write("profile_pic: " + profile_pic + "\n")
				of.write("display_url: " + display_url + "\n")
				of.write("likes: " + str(likes) + "\n")
				of.write("caption: " + caption + "\n")
				of.write("comments: " + str(comments) + "\n")
				of.write("post_id: " + post_id + "\n")
				of.write("is_video: " + str(is_video) + "\n")
				of.write("owner_id: " + owner_id + "\n")
				of.write("shortcode: " + shortcode + "\n")
				of.write("locations: " + location + "\n")
				if (tags == None):
					of.write("tags: \n")
				else:
					of.write("tags: " + ', '.join((tags)) + "\n")

				time_conv = datetime.datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')
				of.write("timestamp: " + time_conv + "\n")

				try:
					contains = acc_cap.split("contain:",1)[1]
				except:
					contains = ""
				of.write("accessibility_caption: " + contains + "\n")

				of.write("im_640: " + im_640 + "\n")
				of.write("\n")

				pl.append(post_id)
				count = count + 1
			else:
				print("Blocked duplicate: PostID = " + str(post_id))

	return count


def data_from_json(filename, jsonwriter):
	with open(filename) as f:
		filecity = filename.split('/')[-1][:-5]
		main_tag = filecity[:-2]
		print("City: " + filecity)
		data = json.load(f)
		for i in range(0, len(data['GraphImages'])):
			print(i)
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
			if (tags == None):
				tags = ""
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

			tags_str = ', '.join((tags))

			jsonwriter.writerow([main_tag, username, profile_pic, str(likes), caption, str(comments), post_id, str(is_video), owner_id, shortcode, location, str(timestamp), im_640, str(tags_str)])

def json_prep(json_path, of, of_csv):
	all_jsons = glob.glob(json_path + "*.json")
	jsonwriter = csv.writer(of_csv, delimiter='|')
	jsonwriter.writerow(['main_tag', 'username', 'profile_pic', 'likes', 'caption', 'comments', 'post_id', 'is_video', 'owner_id', 'shortcode', 'locations', 'timestamp', 'im_640', 'tags'])
	
	count = 0
	post_lists =[]
	for filename in all_jsons:
		#data_from_json(filename, jsonwriter)
		json_count = data_from_json_text(filename, of, post_lists)
		count = count + json_count

	return count, post_lists

if __name__ == "__main__":
	json_path = os.getcwd() + "/jsons/"

	if os.path.exists("temp_db.txt"):
  		os.remove("temp_db.txt")
	of = open("temp_db.txt", "w")
	# filename = json_path + "tokyo_3.json"
	# data_from_json_text(filename, of)
	if os.path.exists("temp_db.csv"):
  		os.remove("temp_db.csv")
	of_csv = open('temp_db.csv', 'a')
	
	count, post_lists = json_prep(json_path, of, of_csv)

	print("Posts Scraped: " + str(count))
	print(len(post_lists))
