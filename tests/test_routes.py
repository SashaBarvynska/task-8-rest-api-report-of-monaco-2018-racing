import json
from unittest.mock import patch

import pytest
from flask import Response
from task_Barvynska import Driver

from tests.constants import (DRIVER_DRR, DRR, create_driver, lIST_DRIVERS,
                             sort_list_by_format)

drivers_list = create_driver(2)


@patch("src.controller.get_drivers", return_value=drivers_list)
@pytest.mark.parametrize("order, format, result", [
    (
        "desc", "json", sort_list_by_format(drivers_list, "json", True)
    ),
    (
        "asc", "json", sort_list_by_format(drivers_list, "json", False)
    ),
    (
        "desc", "xml", sort_list_by_format(drivers_list, "xml", True),
    ),
    (
        "asc", "xml", sort_list_by_format(drivers_list, "xml", False),
    )
    ])
def test_show_report(mock_get_drivers, order, format, result, client):
    response: Response = client.get(f"/report?order={order}&format={format}")
    assert response.status_code == 200
    assert response.data == result


@patch("src.controller.get_drivers", return_value=drivers_list)
@pytest.mark.parametrize("order, format, result", [
    (
        "desc", "json", sort_list_by_format(drivers_list, "json", True, 2)
    ),
    (
        "asc", "json", sort_list_by_format(drivers_list, "json", False, 2)
    ),
    (
        "desc", "xml", sort_list_by_format(drivers_list, "xml", True, 2),
    ),
    (
        "asc", "xml", sort_list_by_format(drivers_list, "xml", False, 2),
    )
    ])
def test_show_drivers(mock_get_drivers, order, format, result, client):
    response: Response = client.get(f"/report/drivers?order={order}&format={format}")
    assert response.status_code == 200
    assert response.data == result


@patch("src.controller.get_drivers", return_value=lIST_DRIVERS)
@patch("src.routes.DriverAdaptor.get_driver", return_value=DRIVER_DRR)
def test_get_info(mock_get_driver, mock_get_drivers, client):
    response: Response = client.get("/report/drivers/DRR?format=json")
    driver = dict(zip(list(Driver.__match_args__), DRR))
    assert response.status_code == 200
    assert response.data == f'{json.dumps(driver).replace(": ", ":").replace(", ", ",")}\n'.encode()
    mock_get_driver.assert_called_with("abbreviation", "DRR")


@patch("src.controller.get_drivers", return_value=lIST_DRIVERS)
@patch("src.routes.DriverAdaptor.get_driver", return_value=None)
def test_get_info_error(mock_get_driver, mock_get_drivers, client):
    response: Response = client.get("/report/drivers/DRR?format=json")
    assert response.status_code == 404
    assert response.data == b'{"message":"No such driver"}\n'
    mock_get_driver.assert_called_with("abbreviation", "DRR")


def test_wrong_routes(client):
    response: Response = client.get("/report/&^%SashaBarvynska474")
    assert response.status_code == 404
    assert response.data == b'{"message":"Page Not Found"}\n'
