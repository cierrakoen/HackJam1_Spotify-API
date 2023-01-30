import flask
import requests

app = flask.Flask(__name__)

#our client id
Client_ID = 'yourClientID'
Secret_ID = 'yourSecretClientID'

#api link
APItok_Url = 'https://accounts.spotify.com/api/token'

#post sets up the qualifications for our api calls
auth_response = requests.post(APItok_Url, {
    'grant_type': 'client_credentials',
    'client_id': Client_ID,
    'client_secret': Secret_ID,
})

#puts data into a json file to find token
auth_data = auth_response.json()

#accesses specific token
Key = auth_data['access_token']

#creating authorization for specific token in Spotify format
headers = {
    'Authorization': 'Bearer {token}'.format(token='yourGeneratedToken')
}

#starter for API end points
API_Url = 'https://api.spotify.com/v1/'

artist_id = 'yourArtistID'

#now we can get the data that we need
#lets look at an artist's album
mainLink = requests.get(API_Url + 'artists/' + artist_id +'/albums', 
                 headers=headers, 
                 params={'market': 'ES', 'limit': 10, 'offset': 5})

data = mainLink.json()


@app.route('/')
def index():
    return  flask.render_template("index.html",data)

app.run(use_reloader = True, debug = True)
