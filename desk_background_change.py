import os, random
import time

while True:
	try: 
		images = os.listdir("/home/sameer/Pictures/")
		image = random.choice(images)
		absolute_path = 'gsettings set org.gnome.desktop.background picture-uri file:/home/sameer/Pictures/'
		joining = os.path.join(absolute_path,image)
		os.system(joining)
		time.sleep(10)
	except KeyboardInterrupt:
		exit("Exiting")
