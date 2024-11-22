import streamlit as st
import requests
from datetime import datetime

'''
## TaxiFareModel front
'''

date = st.date_input('date of ride')
time = st.time_input('time of ride')
place = st.text_input('1st adress')
arrival = st.text_input('arrival adress')

url1 = 'https://api.opencagedata.com/geocode/v1/json'
params = {'key' : 'c634615b656f40fb93f7fa5aed8b25ff',
          'q' : place}
response = requests.get(url1, params)
test = (response.json())
lat1 = test.get('results')[0].get('geometry').get('lat')
long1 = test.get('results')[0].get('geometry').get('lng')

params2 = {'key' : 'c634615b656f40fb93f7fa5aed8b25ff',
          'q' : arrival}
response2 = requests.get(url1, params2)
lat2 = response2.json().get('results')[0].get('geometry').get('lat')
long2 = response2.json().get('results')[0].get('geometry').get('lng')

st.write(f'you are at {lat1}, {long1}, {lat2}, {long2}')

count = st.slider('nb passengers ?', 1, 10, 3)
st.write(count)

url = 'https://taxifare.lewagon.ai/predict'

# if url == 'https://taxifare.lewagon.ai/predict':

#     st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

datetimee = f'{date} {time}'
params_user = {'pickup_datetime' : datetimee,
               'pickup_longitude' : long1,
               'pickup_latitude' : lat1,
               'dropoff_longitude' : long2,
               'dropoff_latitude' : lat2,
               'passenger_count' : count}
pred_response = requests.get(url, params_user)
prediction_fare = pred_response.json().get('fare')
st.write(f'YAAAAAAAAAY {round(prediction_fare,2)}$')
# http://127.0.0.1:8000/predict?pickup_datetime=2014-07-06+19:18:00
# &pickup_longitude=-73.950655&pickup_latitude=40.783282&dropoff_longitude=-73.984365&dropoff_latitude=40.769802&passenger_count=2
