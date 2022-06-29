from dataclasses import dataclass
from typing import Literal
import requests

import config
from exceptions import CantGetCoordinates


@dataclass(slots=True, frozen=True)
class Coordinates:
    latitude: float
    longitude: float


def get_gps_coordinates() -> Coordinates:
    """Returns current coordinates using ipinfo.io"""
    coordinates = _get_ipinfo_coordinates()
    return _round_coordinates(coordinates)

def _get_ipinfo_coordinates() -> Coordinates:
    output = _get_ipinfo_output()
    return Coordinates(
        latitude=output[0],
        longitude=output[1]
    )


def _get_ipinfo_output() -> list[str]:
    try:
        output = requests.get(f"http://ipinfo.io/loc?token={config.ipinfo_token}").text.strip()
    except:
        raise CantGetCoordinates
    return output.split(",")

def _parse_float_coordinate(value: str) -> float:
    try:
        return float(value)
    except ValueError:
        raise CantGetCoordinates

def _round_coordinates(coordinates: Coordinates) -> Coordinates:
    if not config.USE_ROUNDED_COORDS:
        return coordinates
    return Coordinates(*map(
        lambda c: round(c, 1),
        [coordinates.latitude, coordinates.longitude]
    ))


if __name__ == "__main__":
    print(get_gps_coordinates())