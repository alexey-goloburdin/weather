# ipinfo.io/[IP address]?token=98045abb33e482
ipinfo_token = "" # you may append API token here
USE_ROUNDED_COORDS = False
OPENWEATHER_API = ""  # paste API token here
OPENWEATHER_URL = (
    "https://api.openweathermap.org/data/2.5/weather?"
    "lat={latitude}&lon={longitude}&"
    "appid=" + OPENWEATHER_API + "&lang=ru&"
    "units=metric"
)
