import random, os

list_images = os.listdir("/home/sameer/Pictures")

absolute_path = 'gsettings set org.gnome.desktop.background picture-uri file:/home/sameer/Pictures/'

particular_image = random.choice(list_images)

joining = os.path.join(absolute_path, particular_image)

print(joining)

os.system(joining)