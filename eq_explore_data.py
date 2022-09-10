import json
from plotly.graph_objects import Scattergeo, Layout
from plotly import offline

filename = 'eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

mags = []
lons = []
lats = []
hover_texts = []

for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    text = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(text)
    
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Greens',
        'reversescale': False,
        'colorbar': {'title': "Strengh"},
    }
}]
may_layout = Layout(title = 'Earthquakes in World')

fig = {'data': data, 'layout': may_layout}
offline.plot(fig, filename='global_earthquakes.html')
