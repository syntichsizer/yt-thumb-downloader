import requests, json, sys, re

#reading file
with open('list.txt') as file:
    urls = file.readlines()

counter = 0

#iterating through urls
for video_url in urls:

	#loading json from YouTube
	json_url = "https://www.youtube.com/oembed?url=" + video_url + "&format=json"
	request = requests.get(json_url)
	json_data = json.loads(request.text)

	#parsing data
	video_title = json_data["title"]
	thumbnail_url_hq = json_data["thumbnail_url"]

	#we need mq instead of hq
	thumbnail_url_mq = thumbnail_url_hq.replace("hqdefault", "mqdefault")

	#using regex to delete unsupported characters in windows file names
	video_title = re.sub('[<>:"/\|?*]', '', video_title)

	#downloading thumbnail
	img_data = requests.get(thumbnail_url_mq).content
	with open(video_title + ".jpg", 'wb') as handler:
	    handler.write(img_data)
	    counter += 1
	    print("[" + str(counter) + "/" + str(len(urls)) + "] " + video_title + ".jpg downloaded.")
	    
input("All thumbnails are downloaded!\Press any key to exit....")

