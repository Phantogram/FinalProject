# import urllib
import urllib.request
import ast
import json 

def ML_Pro(fv):
    api_key = ''
    url = ''
    
    track_values = [ "value", "value", "value", "value", fv["acousticness"], fv["danceability"], fv["duration_ms"], fv["energy"], fv["instrumentalness"], fv["key"], fv["liveness"], fv["loudness"], fv["mode"], fv["speechiness"], fv["tempo"], fv["time_signature"], fv["valence"], "value", "0" ]
    
    data =  {

            "Inputs": {

                    "input1":
                    {
                        "ColumnNames": ["id", "name", "uri", "artist", "acousticness", "danceability", "duration_ms", "energy", "instrumentalness", "key", "liveness", "loudness", "mode", "speechiness", "tempo", "time_signature", "valence", "Group", "group_n"],
                        "Values": [ track_values ]
                    },        },
                "GlobalParameters": {
    }
        }

    body = str.encode(json.dumps(data))

    # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}
    req = urllib.request.Request(url, body, headers) 
    try:
        response = urllib.request.urlopen(req)

        # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
        # req = urllib.request.Request(url, body, headers) 
        # response = urllib.request.urlopen(req)

        result = response.read()
        # result = result.decode('ASCII')
        # print(result.Results.output1.ColumnNames) 
    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())

        print(json.loads(error.read()))     

    decode_result = result.decode('UTF-8')
    mydata = ast.literal_eval(decode_result)
    final_result = mydata["Results"]["output1"]["value"]["Values"][0][-1]
    return final_result            