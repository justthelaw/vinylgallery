# https://itunes.apple.com/search?term=Wes+Montgomery+Down+Here+On+The+Ground&country=us&entity=album&limit=25&callback=jQuery111205972574157269097_1707577928955&_=1707577928957
# url = "https://itunes.apple.com/search?term=" + artist+name + album+name + "&country=us&entity=album&limit=25"
# 
# 
# 
# 
# 
import requests
import json
from requests.exceptions import HTTPError

hires_prefix= "https://a5.mzstatic.com/us/r1000/0/"

def get_album_art (query):
    str(query[0]).replace(' ', '+')
    str(query[0]).replace("'", '%27')
    str(query[1]).replace(' ', '+')
    str(query[1]).replace("'", '%27')
    search_term = "https://itunes.apple.com/search?term=" + str(query[0]) + '+' + str(query[1]) + "&country=us&entity=album&limit=1"
    jsonResponse = 0

    try:
        response = requests.get(search_term)
        response.raise_for_status()
        # access JSOn content
        jsonResponse = response.json()

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')

    if(type(jsonResponse) != dict):
        print("returning")
        return

    if (int(jsonResponse['resultCount']) > 0 ):
        albumURL = jsonResponse['results'][0]['artworkUrl60']
        albumURL = albumURL.replace("https://is1-ssl.mzstatic.com/image/thumb/", "")
        albumURL = albumURL.replace("/60x60bb.jpg", "")
        albumURL = hires_prefix + albumURL
        return albumURL
    
    # return_json = requests.get(search_term)
    # # response = return_json.json()
    # for key, value in return_json.items():
    #     print(key, ":", value)
    # img_data = requests.get(return_json.content.index('artworkUrl60')).content
    # with open('image_name.jpg', 'wb') as handler:
    #     handler.write(img_data)
    return

def main():
    
    return

main()