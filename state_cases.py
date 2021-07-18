import plotly
from plotly.graph_objs import Scatter, Layout
import plotly.graph_objs as go

import csv

def valid_state(state):
    # https://gist.githubusercontent.com/norcal82/e4c7e8113f377db184bb/raw/87558bb70c5c149f357663061bc1b1ab96c90b7e/state_names.py
    state_list = [
        "Alaska",
        "Alabama",
        "Arkansas",
        "American Samoa",
        "Arizona",
        "California",
        "Colorado",
        "Connecticut",
        "District of Columbia",
        "Delaware",
        "Florida",
        "Georgia",
        "Guam",
        "Hawaii",
        "Iowa",
        "Idaho",
        "Illinois",
        "Indiana",
        "Kansas",
        "Kentucky",
        "Louisiana",
        "Massachusetts",
        "Maryland",
        "Maine",
        "Michigan",
        "Minnesota",
        "Missouri",
        "Mississippi",
        "Montana",
        "North Carolina",
        "North Dakota",
        "Nebraska",
        "New Hampshire",
        "New Jersey",
        "New Mexico",
        "Nevada",
        "New York",
        "Ohio",
        "Oklahoma",
        "Oregon",
        "Pennsylvania",
        "Puerto Rico",
        "Rhode Island",
        "South Carolina",
        "South Dakota",
        "Tennessee",
        "Texas",
        "Utah",
        "Virginia",
        "Virgin Islands",
        "Vermont",
        "Washington",
        "Wisconsin",
        "West Virginia",
        "Wyoming"
        ]
    for state_name in state_list:
        if state_name == state:
            return True
    return False


f = open("us-states.csv")
reader = csv.DictReader(f)

while True:
    state = input("State: ")
    if valid_state(state):
        break

x = []
y = []

previous_total = 0

for row in reader:
    if row["state"] == state:
        x.append(row["date"])
        y.append(int(row["cases"]) - previous_total)
        previous_total = int(row["cases"])

trace0 = go.Scatter(x=x, y=y, name=state)

graph = {
    "data": [trace0],
    "layout": Layout(title=state + " Covid Cases")
}

plotly.offline.plot(graph, filename=state + 'Cases.html')
