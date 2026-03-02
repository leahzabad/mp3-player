import requests
from PIL import Image

client_id =  "96ac319a187a4f87a93d3ecb3f1a7076"
client_secret = "72f00aabfc5044b5afc03f74f0fdb34d"


token_url = "https://accounts.spotify.com/api/token"
token_data = {"grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret}
token_headers = {"Content-Type": "application/x-www-form-urlencoded"}

key = requests.post(token_url, token_data, token_headers)
access_dict = key.json()
#print(access_dict)

album_url_b = "https://api.spotify.com/v1/albums/"
album_ID = input("Album token: ")
album_url = album_url_b + album_ID
tempstr = access_dict['token_type'] + " " + access_dict['access_token']
album_header = {"Authorization": tempstr}

album_data = requests.get(album_url, headers=album_header)
album_dict = album_data.json()
print(album_dict['name'])
print((album_dict['artists'][0])['name'])
tracks_nb = album_dict['tracks']['total']
for i in range(0, tracks_nb):
        print((album_dict['tracks']['items'][i])['name'])
img = Image.open("skzdoit.jpg")
newsize = (100,100)
fimg = img.resize(newsize)

fimg.save("skz.bmp")
bitmap_data = fimg.tobytes()
width, height = fimg.size
print(bitmap_data)




#https://open.spotify.com/album/4lkJ6i3LDK8HvcU2tPWX9k?si=Ac3H9qA_SZyK2SlBEliDCw