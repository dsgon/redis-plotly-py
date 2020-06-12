from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
import dash_daq as daq
import dash

from datetime import datetime
from flask import Flask
import redis
import json
import time

#Globals Variables
TOTAL = 0
A_VALUE = 0
B_VALUE = 0
TIMESTAMP = 0

ENCODING = 'utf-8'

CHANNEL = 'my_channel'

VISUALIZATION_HOST='localhost'
VISUALIZATION_PORT='8050'


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

topic = redis.Redis(host='localhost', port=6379)
topicSub = topic.pubsub()
topicSub.subscribe(CHANNEL)
# Plotly Layout
app.layout = html.Div(
        [
            
            html.Div([
                daq.LEDDisplay(id='operator-led-time',color='#92e0d3',backgroundColor='#1e2130',size=40)
            ]),

            html.Table([
                html.Thead([
                    html.Th('Total '),
                    html.Th('A Value'),
                    html.Th('B Value'),
                ]),
                html.Tbody([
                    html.Th([
                        html.Div([
                            daq.LEDDisplay(id='operator-led-total',color='#92e0d3',backgroundColor='#1e2130',size=40)
                        ])
                    ]),
                    html.Th([
                        html.Div([
                            daq.LEDDisplay(id='operator-led-a_value',color='#92e0d3',backgroundColor='#1e2130',size=40)
                        ])
                    ]),
                    html.Th([
                        html.Div([
                            daq.LEDDisplay(id='operator-led-b_value',color='#92e0d3',backgroundColor='#1e2130',size=40)
                        ])
                    ])
                ])
            ]),
            
            dcc.Interval(id='graph-update', interval=1000),
        ])
    
#Method to draw dash components. This method is updated via callback
@app.callback(
    [
        Output('operator-led-total','value'),
        Output('operator-led-a_value', 'value'),
        Output('operator-led-b_value', 'value'),
        Output('operator-led-time', 'value'),
    ],
    [
        Input('graph-update', 'n_intervals'),
    ],
)
def update_graph(graph_update):
    global TOTAL, A_VALUE, B_VALUE, TIMESTAMP, topicSub
    
    try:
        
        # print(redis_sub)
        # sub = redis_sub.pubsub()
        # print(sub)
        # #Subcribe to Topic
        # sub = sub.subscribe(CHANNEL)
        # print(sub)
        #get message from topic and decode
        byte_data = topicSub.get_message()['data']
        print(byte_data)
        json_data = byte_data.decode(ENCODING).replace("'", '"')
        data = json.loads(json_data)
        #extract data from Json
        timestamp = data['timestamp']
        timestamp = datetime.utcfromtimestamp(timestamp).strftime('%H%M%S')
        if timestamp != TIMESTAMP:
            TIMESTAMP = timestamp
        
        metrics = data['metrics']
        TOTAL = str(metrics['total']).zfill(2)
        A_VALUE = str(metrics['a']).zfill(2)
        B_VALUE = str(metrics['b']).zfill(2)
        print('Message Proccesed: TimeStamp = {}'.format(TIMESTAMP))
        
    except Exception as e:
        print('No message to show')
        pass
 
    return TOTAL, A_VALUE, B_VALUE, TIMESTAMP 


if __name__ == "__main__":
    app.run_server(host=VISUALIZATION_HOST, port=VISUALIZATION_PORT,threaded=True)