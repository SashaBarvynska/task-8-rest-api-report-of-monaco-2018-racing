from unittest.mock import patch

import pytest

from src.controller import DriverAdaptor, get_drivers
from tests.constants import DICT_ABB, DICT_TIME, lIST_DRIVERS


@patch("src.controller.get_drivers", return_value=lIST_DRIVERS)
@pytest.mark.parametrize("key,value,expected", [
    (
        "abbreviation",
        "DRR",
        lIST_DRIVERS[1]
    ),
    (
        "driver",
        "Sebastian Vettel",
        lIST_DRIVERS[0]
    ),
    (
        "abbreviation",
        "Sebastidsffsdfdsfsfel",
        None
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
@patch("src.controller.Drivers.build_report", return_value=lIST_DRIVERS)
def test_get_drivers(mock_build_report, mock_format_file_time, mock_format_file_abbr, mock_open_files, mock_find_files):
    assert get_drivers() == lIST_DRIVERS
    mock_find_files.assert_called_with("data_files")
    mock_open_files.assert_called_with("path_2")
    mock_format_file_abbr.assert_called_with("file_content")
    mock_format_file_time.assert_called_with("file_content")
    mock_build_report.assert_called_with(DICT_ABB, DICT_TIME, DICT_TIME)


@patch("src.controller.get_drivers", return_value=lIST_DRIVERS)
@pytest.mark.parametrize("test_input,expected", [
    (
        True,
        sorted(lIST_DRIVERS, key=lambda x: x.speed, reverse=True)
    ),
    (
        False,
        sorted(lIST_DRIVERS, key=lambda x: x.speed, reverse=False)
    ),
])
def test_sort_data(mock_get_drivers, test_input, expected):
    instance = DriverAdaptor()
    assert instance.sort_data(test_input) == expected
    mock_get_drivers.assert_called_once()
