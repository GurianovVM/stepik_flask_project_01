from flask import Flask, render_template
from data import title, departures, tours, subtitle, description

app = Flask(__name__)

@app.route('/')
def render_index_html():
    tour = []
    for i in range(1, 7):
        tour.append(tours[i])
    return render_template('index.html', title_page=title, nav=departures, sub_title=subtitle, des=description, tour=tour)

@app.route('/departure/<departure>')
def render_departure(departure):
    return render_template('departure.html', title_page=title, nav=departures)

@app.route('/tour/<id>/')
def render_tour(id):
    return render_template('tour.html', title_page=title, nav=departures, tour=tours[int(id)])

app.run()
