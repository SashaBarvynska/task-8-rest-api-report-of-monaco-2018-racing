from unittest.mock import patch

import pytest

from src.controller import DriverAdaptor, get_drivers
from tests.constants import (DICT_ABB, DICT_TIME, DRIVER_DRR, DRIVER_SVF,
                             LIST_DRIVERS, lIST_ALL_DRIVERS_ASC,
                             lIST_ALL_DRIVERS_DESC)


@patch("src.controller.get_drivers", return_value=lIST_ALL_DRIVERS_ASC)
@pytest.mark.parametrize("key,value,expected", [
    (
        "abbreviation",
        "DRR",
        DRIVER_DRR
    ),
    (
        "driver",
        "Sebastian Vettel",
        DRIVER_SVF
    ),
])
def test_get_driver(mock_get_drivers, key, value, expected):
    instance = DriverAdaptor()
    mock_get_drivers.assert_called_once()
    assert instance.get_driver(key, value) == expected


@patch(
    "src.controller.Files.find_files",
    return_value=["path_1", "path_2", "path_3"],
)
@patch(
    "src.controller.Files.open_files",
    return_value="file_content",
)
@patch(
    "src.controller.FormatFile.format_file_abbreviation_data",
    return_value=DICT_ABB,
)
@patch(
    "src.controller.FormatFile.format_file_time",
    return_value=DICT_TIME,
)
@patch("src.controller.Drivers.build_report", return_value=LIST_DRIVERS)
def test_get_drivers(mock_build_report, mock_format_file_time, mock_format_file_abbr, mock_open_files, mock_find_files):
    assert get_drivers() == LIST_DRIVERS
    mock_find_files.assert_called_with("data_files")
    mock_open_files.assert_called_with("path_2")
    mock_format_file_abbr.assert_called_with("file_content")
    mock_format_file_time.assert_called_with("file_content")
    mock_build_report.assert_called_with(DICT_ABB, DICT_TIME, DICT_TIME)


@patch("src.controller.get_drivers", return_value=lIST_ALL_DRIVERS_ASC)
@pytest.mark.parametrize("test_input,expected", [
    (
        True,
        lIST_ALL_DRIVERS_ASC
    ),
    (
        False,
        lIST_ALL_DRIVERS_DESC
    ),
])
def test_sort_data(mock_get_drivers, test_input, expected):
    instance = DriverAdaptor()
    assert instance.sort_data(test_input) == expected
    mock_get_drivers.assert_called_once()
