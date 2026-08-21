from weather_station import WeatherStation
from tv import TVDisplay
from mobile import MobileDisplay

ws = WeatherStation()
tv = TVDisplay()
mobile = MobileDisplay()


ws.add_observer(tv)
ws.update_temperature(50)
ws.update_temperature(44)

print ("\n=================== After Update ======================")
ws.add_observer(mobile)
ws.update_temperature(20)

print("\n================== remove one observer =================")
ws.remove_observer(tv)
ws.update_temperature(10)
