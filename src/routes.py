from flasgger import swag_from
from flask import request

from src.app import app
from src.controller import DriverAdaptor, make_json_response, make_xml_response


@app.route('/', methods=['GET'])
@app.route('/report', methods=['GET'])
@swag_from('swagger/report.yml')
def show_report():
    instance = DriverAdaptor()
    sorted_data = instance.sort_data(request.args.get('order') == "desc")
    if request.args.get('format') == "json":
        return make_json_response(sorted_data)
    elif request.args.get('format') == "xml":
        return make_xml_response(sorted_data)


@app.route('/report/drivers', methods=['GET'])
@swag_from('swagger/drivers.yml')
def show_drivers():
    instance = DriverAdaptor()
    if request.args.get('format') == "json":
        return make_json_response(instance.list_drivers)
    elif request.args.get('format') == "xml":
        return make_xml_response(instance.list_drivers)


@app.route('/report/drivers/<driver_code>', methods=['GET'])
@swag_from('swagger/driver.yml')
def get_info(driver_code):
    instance = DriverAdaptor()
    driver = instance.get_driver('abbreviation', driver_code)
    if request.args.get('format') == "json":
        return make_json_response(driver)
    elif request.args.get('format') == "xml":
        return make_xml_response([driver])
