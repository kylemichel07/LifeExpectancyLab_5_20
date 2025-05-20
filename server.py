# flask --app data_server run
from flask import Flask
from flask import render_template
from flask import request
import json


app = Flask(__name__, static_url_path='', static_folder='static')

x_list_canada = []
x_list_mexico = []
x_list_usa = []

@app.route('/')
def index():
    the_dict = open("data/life_expectancy.json", "r")
    my_data = json.load(the_dict)


    for i in range(1960,2020): #2019, 61 years
        x_list_canada.append(i)

    for i in range(1960,2021): #2020, 62 years
        x_list_mexico.append(i)

    for i in range(1960,2020): #2019, 61 years
        x_list_usa.append(i)

    Canada_y_list = list(my_data["Canada"].values())
    Mexico_y_list = list(my_data["Mexico"].values())
    USA_y_list = list(my_data["United States"].values())

    """line_endpoints =[]
    for i in range(len(years)-1): # make it easy to dynamically generate a line graph
        start_x = years[i] #generate endpoints for each line segment
        stop_x = years[i+1]
        line_endpoints.append([requested_data[start_x],requested_data[stop_x]])"""
    
    print(len(x_list_canada))
    print(len(Canada_y_list))
    print(len(USA_y_list))
    print(len(Mexico_y_list))
    return render_template('index.html', canada_data = Canada_y_list, mexico_data = Mexico_y_list, usa_data = USA_y_list)



@app.route('/year')
def year():
    requested_year = request.args.get('year')
    return render_template('year.html')

app.run(debug=True)
