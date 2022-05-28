from urllib.error import URLError
from json import JSONDecodeError

import urllib.request
import json
import config

from datatypes import Coordinates
from coordinates import Coordinates
from exceptions import CantGetCoordinates, ApiServiceError

def get_coordinates() -> Coordinates:
    """Get coordinates from ipapi.com"""
    coordinates = _get_ipapi_coordinates()
    return coordinates

def _get_ipapi_coordinates() -> Coordinates:
    ipapi_output = _get_ipapi_response()
    coordinates = _parse_ipapi_coordinates(ipapi_output)
    return coordinates

def _get_ipapi_response() -> str:
    try:
        result = urllib.request.urlopen(config.IPAPI_URL).read()
    except URLError:
        raise ApiServiceError#("Не удалось получить данные с ipapi")

    return result

def _parse_ipapi_coordinates(ipapi_output: bytes) -> Coordinates:
    try:
        output = json.loads(ipapi_output)
    except JSONDecodeError:
        raise CantGetCoordinates#("Ошибка при обработке данных с ipapi")
    
    if "latitude" and "longitude" in output:
        return Coordinates(
            latitude=output["latitude"],
            longitude=output["longitude"]
        )
    else:
        raise CantGetCoordinates#("Сервер ipapi вернул некорректные данные")