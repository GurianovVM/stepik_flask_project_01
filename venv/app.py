from flask import Flask, render_template
from data import tours
app = Flask(__name__)

@app.route('/')
def render_index_html():
    return render_template('index.html')

@app.route('/departure/<departure>')
def render_departure(departure):
    return render_template('departure.html')

@app.route('/tour/<id>/')
def render_tour(id):
    return render_template('tour.html')

app.run()
