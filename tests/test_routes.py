from unittest.mock import patch

import pytest
from flask import Response

from tests.constants import (ASC_SVF, DESC_SVF, DRIVER_DRR, DRR,
                             lIST_ALL_DRIVERS_ASC)


@patch("src.controller.get_drivers", return_value=lIST_ALL_DRIVERS_ASC)
@pytest.mark.parametrize("order, sort", [
    (
        "desc", DESC_SVF
    ),
    (
        "asc", ASC_SVF
    ),
    ])
def test_show_report(mock_get_drivers, order, sort, client):
    response: Response = client.get(f"/report?order={order}")
    assert sort in response.data.decode()
    assert response.status_code == 200


@patch("src.controller.get_drivers", return_value=lIST_ALL_DRIVERS_ASC)
def test_show_drivers(mock_get_drivers, client):
    response: Response = client.get("/report/drivers")
    assert DRR in response.data.decode()
    assert response.status_code == 200


@patch("src.controller.get_drivers", return_value=lIST_ALL_DRIVERS_ASC)
@patch("src.routes.DriverAdaptor.get_driver", return_value=DRIVER_DRR)
def test_get_info(mock_get_driver, mock_get_drivers, client):
    response: Response = client.get("/report/drivers/DRR")
    assert "Daniel Ricciardo" in response.data.decode()
    assert response.status_code == 200
    mock_get_driver.assert_called_with("abbreviation", "DRR")
