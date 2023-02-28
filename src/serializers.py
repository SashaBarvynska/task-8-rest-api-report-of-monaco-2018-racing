from task_Barvynska import Driver


def data_to_json(list_drivers: list[Driver]) -> list[Driver]:
    return [{"abbreviation": x.abbreviation, "driver": x.driver} for x in list_drivers]


def data_to_xml(list_drivers: list[Driver]) -> list[Driver]:
    return [x.__dict__ for x in list_drivers]
