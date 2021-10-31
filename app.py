import flask
from flask import Flask
from flask import request
from src.kpi_report import KpiReport

app = Flask(__name__)


@app.route("/")
def index():
    return flask.render_template('index.html')


@app.route("/sales")
def sales_report():
    return flask.render_template('report.html')


@app.route("/area")
def area_report():
    return flask.render_template('report.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        path = '/tmp/csv/1.csv'
        f = request.files['the_csv']
        f.save(path)

        report = KpiReport(path)

        t = request.args['type']

        if t == '0':
            return str(report.for_saler())
        elif t == '1':
            return str(report.for_area())
        else:
            return 'Unknown Type ' + t
