from config import KEY
from termcolor import cprint
import urllib.request as url
import json



def get_data(origins, destinations):
    path = 'https://maps.googleapis.com/maps/api/distancematrix/json?origins={}&destinations={}&key={}'.format(origins, destinations, KEY)
    html = url.urlopen(path)
    text = html.read()
    return json.loads(text)

def get_times(data):
    times_matrix = []
    for row in data['rows']:
        times_row = []
        for element in row["elements"]:
            cprint("[E-STATUS] " + element['status'], "cyan")
            time_seg = element["duration"]["value"]
            time_min = time_seg / 60
            times_row.append(time_min)
        times_matrix.append(times_row)
    return times_matrix

def get_distances(data):
    distances_matrix = []
    for row in data['rows']:
        distances_row = []
        for element in row["elements"]:
            distance_m = element["distance"]["value"]
            distance_km = distance_m / 1000
            distances_row.append(distance_km)
        distances_matrix.append(distances_row)
    return distances_matrix


if __name__ == "__main__":

    origin = "Jose+Miguel+Balmaceda+899%2C+Buin"
    destination = "Manuel+Rodriguez+270%2C+Buin"

    data = get_data(origin, destination)
    print(data['status'])
