import json
import random
from dataclasses import dataclass

from simplexml import dumps
from task_Barvynska import Driver


def create_driver(number):
    @dataclass
    class Driver:
        abbreviation: str
        driver: str
        car: str
        start_time: str
        end_time: str
        speed: str

        def __repr__(self):
            return str(
                (
                    self.abbreviation,
                    self.car,
                    self.driver,
                    self.end_time,
                    self.speed,
                    self.start_time,
                )
            )
    Drivers_list = []
    for _ in range(number):
        abbreviation = random.choice(["DRR", "AAA"])
        driver = random.choice(["Sasha Barvynska", "Andrew Holenkov"])
        car = random.choice(["RED BULL RACING TAG HEUER", "MERCEDES"])
        start_time = random.choice(["12:02:58.917", "12:00:00.000"])
        end_time = random.choice(["12:04:03.332", "12:01:12.434"])
        speed = random.choice(["1:04.415", "1:12.434", "1:04.000", "1:12.123", "1:07.415", "1:56.434"])
        driver = Driver(abbreviation, driver, car, start_time, end_time, speed)
        Drivers_list.append(driver)
    return Drivers_list


def sort_list_by_format(drivers_list: list[Driver], format: str, order: bool, columns: int = 6):
    sort_list = sorted(drivers_list, key=lambda x: x.speed, reverse=order)
    column_names = list(Driver.__match_args__)[:columns]
    if columns == 2:
        dict_of_lists = [
            dict(zip(column_names, (i.abbreviation, i.driver))) for i in sort_list
            ]
        if format == "json":
            result = json.dumps([obj for obj in dict_of_lists]).replace(": ", ":").replace(", ", ",")
            return f'{result}\n'.encode()
        if format == "xml":
            result = dumps({'response': dict_of_lists})
            return f'{result}'.encode()
    else:
        if format == "json":
            result = json.dumps([obj.__dict__ for obj in sort_list]).replace(": ", ":").replace(", ", ",")
            return f'{result}\n'.encode()
        if format == "xml":
            dict_of_lists = [
                dict(zip(column_names, (
                    i.abbreviation, i.driver, i.car, i.start_time, i.end_time, i.speed))) for i in sort_list
            ]
            result = dumps({'response': dict_of_lists})
            return f'{result}'.encode()


lIST_DRIVERS = [
    Driver('SVF', 'Sebastian Vettel', 'FERRARI', '12:02:58.917', '12:04:03.332', '1:04.415'),
    Driver('DRR', 'Daniel Ricciardo', 'RED BULL RACING TAG HEUER', '12:14:12.054', '12:11:24.067', '57:12.013')
    ]
DRIVER_DRR = Driver('DRR', 'Daniel Ricciardo', 'RED BULL RACING TAG HEUER', '12:14:12.054', '12:11:24.067', '57:12.013')
DRR = ('DRR', 'Daniel Ricciardo', 'RED BULL RACING TAG HEUER', '12:14:12.054', '12:11:24.067', '57:12.013')

DICT_ABB = {
    "DRR": {"driver": "Daniel Ricciardo", "car": "RED BULL RACING TAG HEUER"},
    "SVF": {"driver": "Sebastian Vettel", "car": "FERRARI"},
}
DICT_TIME = {"SVF": "12:02:58.917", "DRR": "12:14:12.054"}
