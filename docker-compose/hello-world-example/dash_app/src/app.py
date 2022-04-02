import os

import requests
import folium
from dash import Dash, html


URL = os.getenv("REQUESTS_URL")

app = Dash(__name__)

server = app.server
app.config.suppress_callback_exceptions = True
app.title = 'Points'


def dash_layout():
    """
    Create dashboard layout. Get data from API and plot on
    Folium map.
    """

    response = requests.get(URL)
    if response.status_code != 200:
        raise Exception(response.json())

    data = response.json()

    points_map = folium.Map()
    points_map.add_child(folium.LatLngPopup())

    for record in data:
        folium.Marker((record["lat"], record["lon"])).add_to(points_map)


    layout = html.Div(
        [
            html.Iframe(
                srcDoc=points_map.get_root().render(), 
                width="70%", 
                height="600",
            ),
        ],
        style={'textAlign': 'center'},
    )

    return layout


app.layout = dash_layout