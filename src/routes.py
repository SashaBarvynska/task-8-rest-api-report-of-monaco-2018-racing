from flasgger import swag_from
from flask import request, wrappers

from src.app import app
from src.controller import DriverAdaptor, make_json_response, make_xml_response


@app.route('/report', methods=['GET'])
@swag_from('swagger/report.yml')
def show_report() -> wrappers.Response:
    instance = DriverAdaptor()
    sorted_data = instance.sort_data(request.args.get('order') == "desc")
    if request.args.get('format') == "json":
        return make_json_response(sorted_data, 200)
    elif request.args.get('format') == "xml":
        return make_xml_response(sorted_data, 200)


@app.route('/report/drivers', methods=['GET'])
@swag_from('swagger/drivers.yml')
def show_drivers() -> wrappers.Response:
    instance = DriverAdaptor()
    if request.args.get('format') == "json":
        return make_json_response(instance.list_drivers, 200)
    elif request.args.get('format') == "xml":
        return make_xml_response(instance.list_drivers, 200)


@app.route('/report/drivers/<driver_code>', methods=['GET'])
@swag_from('swagger/driver.yml')
def get_info(driver_code: str) -> wrappers.Response:
    instance = DriverAdaptor()
    driver = instance.get_driver('abbreviation', driver_code)
    if request.args.get('format') == "json":
        return make_json_response(driver, 200)
    elif request.args.get('format') == "xml":
        print("make_xml_response([driver], 200): ", make_xml_response([driver], 200))
        return make_xml_response([driver], 200)
