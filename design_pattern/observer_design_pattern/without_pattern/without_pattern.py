class PhoneDisplay:
    def update(self, new_temp):
        print(f"Phone display temperature = {new_temp}")


class TVDisplay:
    def update(self, new_temp):
        print(f"TV display temperature = {new_temp}")


class WeatherStation:
    def __init__(self):
        self.__temperature = 0
        self.__phone_dispay = PhoneDisplay() # Tightly coupled with WeatherStation
        self.__tv_display = TVDisplay() # Tightly coupled with WeatherStation

    def update_temperature(self, new_temp):
        self.__temperature = new_temp
        self.notify_display()

    def notify_display(self):
        self.__phone_dispay.update(self.__temperature)
        self.__tv_display.update(self.__temperature)


ws = WeatherStation()
ws.update_temperature(30)

ws.update_temperature(40)