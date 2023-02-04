from flask import render_template, request

from src.app import app
from src.controller import DriverAdaptor


@app.route('/', methods=['GET'])
@app.route('/report', methods=['GET'])
def show_report():
    instance = DriverAdaptor()
    sorted_data = instance.sort_data(request.args.get('order') == "desc")
    return render_template('report.html', data=sorted_data)


@app.route('/report/drivers', methods=['GET'])
def show_drivers():
    instance = DriverAdaptor()
    return render_template('drivers.html', data=instance.list_drivers)


@app.route('/report/drivers/<driver_code>', methods=['GET'])
def get_info(driver_code):
    instance = DriverAdaptor()
    driver = instance.get_driver('abbreviation', driver_code)
    return render_template('driver_info.html', data=driver)
