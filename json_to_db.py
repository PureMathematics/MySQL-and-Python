import json
import os
import glob
import requests
import csv
import time
import simplejson


import datetime

def data_from_json_text(filename, of, pl, data_dict):
	count = 0
	with open(filename) as f:
		filecity = filename.split('/')[-1]
		filecity1 = filecity.split('_')
		filecity1.pop()
		main_tag = ' '.join(filecity1)
		print("City: " + str(main_tag))
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
					of.write("tags: " + ','.join((tags)) + "\n")

				time_conv = datetime.datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')
				of.write("timestamp: " + time_conv + "\n")

				try:
					contains = acc_cap.split("contain: ",1)[1] #Removes caption before "Image may contain: "
				except:
					contains = ""
				if contains != "":
					cl = []
					contains = contains.split(".")[0] #Removes everything after the period -> rest of caption
					contains = contains.split(", ")
					temp = contains[-1].split(" and ")
					if len(temp) > 1:
						contains.pop()
						contains.append(temp[0])
						contains.append(temp[1])

				of.write("contains: " + ','.join((contains)) + "\n")

				of.write("im_640: " + im_640 + "\n")
				of.write("\n")

				data_dict['post'].append({
					'post_id':post_id,
					'main_tag':main_tag,
					#'shortcode':shortcode,
					'likes':likes,
					'comments':comments,
					#'caption':caption,
					#'owner_id':owner_id,
					'username':username,
					'contains':contains,
					'timestamp':time_conv,
					'locations':location,
					#'tags':tags,
					#'profile_pic':profile_pic,
					'im_640':im_640
				})

				pl.append(post_id)
				count = count + 1
			else:
				print("Blocked duplicate: PostID = " + str(post_id))

	return count

def json_prep(json_path, of, data_dict):


	return count, post_lists

if __name__ == "__main__":

	json_path = os.getcwd() + "/jsons/"

	if os.path.exists("temp_db.txt"):
  		os.remove("temp_db.txt")
	of = open("temp_db.txt", "w")


	post_lists = []

	data_dict = {}
	data_dict['post'] = []
	all_jsons = glob.glob(json_path + "*.json")
	count = 0
	post_lists =[]

	start_time = time.time()
	#filename = json_path + "san_diego_1.json"
	#count = data_from_json_text(filename, of, post_lists, data_dict)

	for filename in all_jsons:
		json_count = data_from_json_text(filename, of, post_lists, data_dict)
		count = count + json_count

	# print("Posts Scraped: " + str(count))
	# print(len(post_lists))
	# print("--- %s seconds ---" % (time.time() - start_time))


	with open('json_db_lite.json', 'w') as outfile:
		json.dump(data_dict, outfile, indent = 4)

	# with open('temp_json.json','r') as infile:
	# 	mydata = json.loads(infile)

	# print json.dumps(mydata, indent=4)

	# outfile = open("data.json", "w")
	# # magic happens here to make it pretty-printed
	# outfile.write(simplejson.dumps(simplejson.loads(data_dict), indent=4, sort_keys=True))
	# outfile.close()

	# if os.path.exists("temp_json.json"):
 #  		os.remove("temp_json.json")


	# if os.path.exists("temp_db.csv"):
	# os.remove("temp_db.csv")
	# of_csv = open('temp_db.csv', 'a')



# def data_from_json(filename, jsonwriter):
# 	with open(filename) as f:
# 		filecity = filename.split('/')[-1][:-5]
# 		main_tag = filecity[:-2]
# 		print("City: " + filecity)
# 		data = json.load(f)
# 		for i in range(0, len(data['GraphImages'])):
# 			print(i)
# 			display_url = data['GraphImages'][i]['display_url']
# 			likes = int(data['GraphImages'][i]['edge_liked_by']['count'])
# 			if data['GraphImages'][i]['edge_media_to_caption']['edges']:
# 				caption = data['GraphImages'][i]['edge_media_to_caption']['edges'][0]['node']['text']
# 			comments = int(data['GraphImages'][i]['edge_media_to_comment']['count'])
# 			post_id = data['GraphImages'][i]['id']
# 			is_video = data['GraphImages'][i]['is_video']
# 			owner_id = data['GraphImages'][i]['owner']['id']
# 			shortcode = data['GraphImages'][i]['shortcode']
# 			tags = data['GraphImages'][i].get('tags')
# 			if (tags == None):
# 				tags = ""
# 			timestamp = data['GraphImages'][i]['taken_at_timestamp']
# 			im_640 = data['GraphImages'][i]['thumbnail_resources'][4]['src']

# 			# Get locations
# 			url = "https://www.instagram.com/p/{0}/?__a=1".format(shortcode)
# 			r = requests.get(url)
# 			data1 = json.loads(r.text)
# 			try:
# 				location = data1['graphql']['shortcode_media']['location']['name'] # get location for a post
# 			except:
# 				location = '' # if location is NULL
# 			try:
# 				username = data1['graphql']['shortcode_media']['owner']['username']
# 				profile_pic = data1['graphql']['shortcode_media']['owner']['profile_pic_url']
# 			except:
# 				username = ''
# 				profile_pic = ''

# 			tags_str = ', '.join((tags))

# 			jsonwriter.writerow([main_tag, username, profile_pic, str(likes), caption, str(comments), post_id, str(is_video), owner_id, shortcode, location, str(timestamp), im_640, str(tags_str)])

