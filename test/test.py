
from flask import Flask, render_template, request,redirect
import ML

app = Flask(__name__)
track_result = 'empty'
@app.route('/')
def index(track_result = None):
    
    return render_template('test.html',result=track_result)

@app.route('/hello', methods=['POST'])
def hello():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    return 'Hello %s %s have fun learning python <br/> <a href="/">Back Home</a>' % (first_name, last_name)

@app.route("/ML",methods=['POST'])
def scrape():
    acousticness = request.form["acousticness"]
    danceability = request.form["danceability"]
    duration_ms = request.form["duration_ms"]
    energy = request.form["energy"]
    instrumentalness = request.form["instrumentalness"]
    key = request.form["key"]
    liveness = request.form["liveness"]
    loudness = request.form["loudness"]
    mode = request.form["mode"]
    speechiness = request.form["speechiness"]
    tempo = request.form["tempo"]
    time_signature = request.form["time_signature"]
    valence = request.form["valence"]

    feature_values = [ "value", "value", "value", "value", acousticness, danceability, duration_ms, energy, instrumentalness, key, liveness, loudness, mode, speechiness, tempo, time_signature, valence, "value", "0" ]
    track_result = ML.ML_Pro(feature_values)
    # return 'Result is %s <br/> <a href="/">Back Home</a>' % (track_result)
    return index(track_result)

if __name__ == '__main__':
    app.run()