from flask import jsonify, make_response
from simplexml import dumps
from task_Barvynska import Driver, Drivers, Files, FormatFile




from config import Config


def get_drivers() -> list[Driver]:
    file_start, file_end, abbreviations_file = Files.find_files(Config.FOLDER_FILES)
    list_drivers = Drivers.build_report(
        FormatFile.format_file_abbreviation_data(Files.open_files(abbreviations_file)),
        FormatFile.format_file_time(Files.open_files(file_start)),
        FormatFile.format_file_time(Files.open_files(file_end)),
        )
    return list_drivers


class DriverAdaptor:
    def __init__(self):
        self.list_drivers = get_drivers()

    def sort_data(self, order: bool) -> list[Driver]:
        return Drivers.sort_data(self.list_drivers, order)

    def get_driver(self, key: str, value) -> Driver:
        return [driver_object for driver_object in self.list_drivers if getattr(driver_object, key) == value][0]


def make_xml_response(list_drivers: list[Driver]):
    column_names = ["abbreviation", "driver", "car", "start_time", "end_time", 'speed']
    dict_of_lists = [dict(zip(column_names, (u.abbreviation, u.driver, u.car, u.start_time, u.end_time, u.speed))) for u in list_drivers]
    response = make_response(dumps({'response': dict_of_lists}), 200)
    response.mimetype = 'application/xml'
    return response


def make_json_response(list_drivers: list[Driver]):
    response = make_response(jsonify(list_drivers), 200)
    response.mimetype = 'application/json'
    return response
