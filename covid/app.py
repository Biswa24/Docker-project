import json
import os
from flask import Flask, render_template, json, current_app as app
from covid_data import timer,data_generaion,generator
from apscheduler.schedulers.background  import BackgroundScheduler

app = Flask(__name__)

# For debuging
app.debug = True


def sensor():
    generator()

sched = BackgroundScheduler(daemon=True)
sched.add_job(sensor,'interval',minutes=20)
sched.start()


@app.route('/')
def home():
    generator()
    lastupdated = timer()
    time_data = data_generaion('time_series.json')
    state_data = data_generaion('statewise.json')
    global_data = data_generaion('global_data.json')
    return render_template('index.html', lastupdated = lastupdated,time_data = time_data, state_data = state_data, global_data = global_data)


@app.route('/helpline')
def helpline():
    return render_template('helpline.html')


@app.route('/sources')
def sources():
    return render_template('./sources.html')

# Test
# @app.route('/graph')
# def graph():
#     timer()
#     time_data = data_generaion('time_series.json')
#     state_data = data_generaion('statewise.json')
#     global_data = data_generaion('global_data.json')
#     return render_template('graph.html',time_data = time_data, state_data = state_data, global_data = global_data)


if __name__ == '__main__':
    # app.run(debug=True)
    app.run()
