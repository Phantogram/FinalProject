import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

cid = ''
secret = ''

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
def find_track(name):
    song = sp.search(name, limit=1, offset=0, type='track', market=None)


    track_id = song['tracks']['items'][0]["id"]
    track = sp.audio_features(track_id)

    features = {}
    features["acousticness"]=(track[0]["acousticness"])
    features["danceability"]=(track[0]["danceability"])
    features["energy"]=(track[0]["energy"])
    features["instrumentalness"]=(track[0]["instrumentalness"])
    features["loudness"]=(track[0]["loudness"])
    features["speechiness"]=(track[0]["speechiness"])
    features["valence"]=(track[0]["valence"])
    features["tempo"]=(track[0]["tempo"])
    features["duration_ms"] = (track[0]["duration_ms"])
    features["key"] = (track[0]["key"])
    features["liveness"] = (track[0]["liveness"])
    features["mode"] = (track[0]["mode"])
    features["time_signature"] = (track[0]["time_signature"])
    
    detail = {
        "info":{
        "name":song['tracks']['items'][0]["name"],
        'uri':song['tracks']['items'][0]["uri"],
        "img":song['tracks']['items'][0]["album"]["images"][2]["url"],
        "artists":song['tracks']['items'][0]["artists"][0]["name"]
        },
        "features":features
    }


    # print(features)
    # print(track_id[0]["id"])
    return(detail)