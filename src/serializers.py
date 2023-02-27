from src.controller import DriverAdaptor


def data_json(order: bool) -> list[dict[str, str]]:
    instance = DriverAdaptor()
    sorted_data = instance.sort_data(order == "desc")
    dict_of_lists = [{"abbreviation": x.abbreviation, "driver": x.driver} for x in sorted_data]
    return dict_of_lists


def data_xml(order: bool) -> list[dict[str, str]]:
    instance = DriverAdaptor()
    sorted_data = instance.sort_data(order == "desc")
    dict_of_lists = [x.__dict__ for x in sorted_data]
    return dict_of_lists
