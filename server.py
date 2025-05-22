# flask --app data_server run
from flask import Flask
from flask import render_template
from flask import request
import json


app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def index():
    f = open("data/life_expectancy.json", "r")
    data = json.load(f)
    f.close()
    avg = []

    print(len(data["Canada"]))

    for i in data["Mexico"].keys():
        avg.append((float(data["Mexico"][i]) + float(data["United States"][i]) + float(data["Canada"][i]))/3)

    
    return render_template('index.html', data = data, years = data["Mexico"].keys(), mexico_data = data["Mexico"].values(), usa_data = data["United States"].values(), canada_data = data["Canada"].values(), average = avg)

@app.route('/year')
def year(): 
    f = open("data/life_expectancy.json", "r")
    data = json.load(f)
    f.close()
    my_year = request.args.get('year')
    mexico_val = float(data["Mexico"][my_year])
    usa_val = float(data["United States"][my_year])
    canada_val = float(data["Canada"][my_year])
    every_val = [mexico_val, usa_val, canada_val]

    legend = [(x, 81.92 - x / 16.73) for x in range(0, 500, 50)]
    country_values = []

    for i in every_val:
        closest = min(legend, key=lambda pair: abs(i - pair[1]))
        country_values.append(closest[0])  

    return render_template('year.html', me_x = mexico_val, us_a = usa_val, can_ada = canada_val, mexicoVal = country_values[0], usaVal = country_values[1], canadaVal = country_values[2], year = my_year, data = data, years = data["Mexico"].keys())

app.run(debug=True)
