import geojson
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Load the GeoJSON data file
filename = 'data/eq_data_1_day_m1.geojson'
with open(filename, encoding='utf-8') as f:
    all_eq_data = geojson.load(f)

# Save a readable version of the data to a new file
readable_file = 'data/readable_eq_data.geojson'
with open(readable_file, 'w') as f:
    geojson.dump(all_eq_data, f, indent=4)

# Extract earthquake data
all_eq_dicts = all_eq_data['features']
mags, lons, lats, hover_texts = [], [], [], []

for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)

# Create a Scattergeo plot of the earthquake data
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5 * mag for mag in mags],  # Size of marker based on magnitude
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'}
    },
}]

my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')

# Print sample data for verification
# print(mags[:10])
# print(lons[:5])
# print(lats[:5])
