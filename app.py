import requests
from flask import Flask,render_template,request

app = Flask(__name__)

api_key = "YOUR API KEY"
 


@app.route('/',methods=('GET','POST'))
def index():
    response = ' '
    if request.method == 'POST':
        location = request.form['location']
        
        if location !=' ':
           try:
            if location.isnumeric() or location.isalnum:
               raise ValueError
            
            response = get_weather_data(location)

           except ValueError:
              print(response)
           except Exception as e:
              print(response)
               
    return render_template('index.html',response=response)


def get_weather_data(location):
    api_url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(location,api_key)
    response = requests.get(api_url)
    print(response.json())
    return response.json()