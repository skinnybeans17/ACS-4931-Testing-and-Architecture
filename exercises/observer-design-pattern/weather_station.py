"""
Final Implementation of WeatherData.  Complete all the TODOs
"""


class Subject:
    # Both of the following two methods take an
    # observer as an argument; that is, the observer
    # to be registered ore removed.

    def __init__(self):
        self.observers = []
    def registerObserver(self, observer):
        self.observers.append(observer)
    def removeObserver(self, observer):
        self.observers.remove(observer)

    # This method is called to notify all observers
    # when the Subject's state (measuremetns) has changed.
    def notifyObservers():
        pass

# The observer class is implemented by all observers,
# so they all have to implemented the update() method. Here
# we're following Mary and Sue's lead and
# passing the measurements to the observers.
class Observer:
    def __init__(self, weatherData):
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0
        self.weatherData = weatherData
        weatherData.registerObserver(self)

    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.display()

# WeatherData now implements the subject interface.
class WeatherData(Subject):

    def __init__(self):
        self.observers = []
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0

    def registerObserver(self, observer):
        # When an observer registers, we just
        # add it to the end of the list.
        self.observers.append(observer)

    def removeObserver(self, observer):
        # When an observer wants to un-register,
        # we just take it off the list.
        self.observers.remove(observer)

    def notifyObservers(self):
        # We notify the observers when we get updated measurements
        # from the Weather Station.
        for ob in self.observers:
            ob.update(self.temperature, self.humidity, self.pressure)

    def measurementsChanged(self):
        self.notifyObservers()

    def setMeasurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

        self.measurementsChanged()

    # other WeatherData methods here.

class CurrentConditionsDisplay(Observer):

    def __init__(self, weatherData):
        self.temerature = 0
        self.humidity = 0
        self.pressure = 0

        self.weatherData = weatherData # save the ref in an attribute.
        weatherData.registerObserver(self) # register the observer
                                           # so it gets data updates.
    def update(self, temperature, humidity, pressure):
        self.temerature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.display()

    def display(self):
        print("Current conditions:", self.temerature,
              "F degrees and", self.humidity,"[%] humidity",
              "and pressure", self.pressure)

# TODO: implement StatisticsDisplay class and ForecastDisplay class.

class StatisticsDisplay(Observer):
    def __init__(self, weatherData):
        self.min_temp = float('inf')
        self.min_humidity = float('inf')
        self.min_pressure = float('inf')
        self.max_temp = float('-inf')
        self.max_humidity = float('-inf')
        self.max_pressure = float('-inf')
        self.average_temp = 0
        self.average_humidity = 0
        self.average_pressure = 0

        self.weatherData = weatherData
        weatherData.registerObserver(self)

    def calculate_stats(self):
        self.min_temp = round(min(self.min_temp, self.temperature), 2)
        self.max_temp = round(max(self.max_temp, self.temperature), 2)
        self.average_temp = round((self.min_temp + self.max_temp) / 2, 2)
        self.min_humidity = round(min(self.min_humidity, self.humidity), 2)
        self.max_humidity = round(max(self.max_humidity, self.humidity), 2)
        self.average_humidity = round((self.min_humidity + self.max_humidity) / 2, 2)
        self.min_pressure = round(min(self.min_pressure, self.pressure), 2)
        self.max_pressure = round(max(self.max_pressure, self.pressure), 2)
        self.average_pressure = round((self.min_pressure + self.max_pressure) / 2, 2)

    def display(self):

        self.calculate_stats()

        print("Temperature Stats:")
        print("Min:", self.min_temp)
        print("Max:", self.max_temp)
        print("Average:", self.average_temp)

        print("Humidity Stats:")
        print("Min:", self.min_humidity)
        print("Max:", self.max_humidity)
        print("Average:", self.average_humidity)

        print("Pressure Stats:")
        print("Min:", self.min_pressure)
        print("Max:", self.max_pressure)
        print("Average:", self.average_pressure)


class ForecastDisplay(Observer):
    def __init__(self, weatherData):
        self.forecast_temp = 0
        self.forecast_humidity = 0
        self.forecast_pressure = 0
        self.weatherData = weatherData
        weatherData.registerObserver(self)

    def calculate_forecast(self):
        self.forecast_temp = round(self.temperature + 0.11 * self.humidity + 0.2 * self.pressure, 2)
        self.forecast_humidity = round(self.humidity - 0.9 * self.humidity, 2)
        self.forecast_pressure = round(self.pressure + 0.1 * self.temperature - 0.21 * self.pressure, 2)

    def display(self):
        self.calculate_forecast()

        print("Forecast:")
        print("Temperature:", self.forecast_temp)
        print("Humidity:", self.forecast_humidity)
        print("Pressure:", self.forecast_pressure)
        print

class WeatherStation:
    def main(self):
        weather_data = WeatherData()
        current_display = CurrentConditionsDisplay(weather_data)
        statistics_display = StatisticsDisplay(weather_data)
        forecast_display = ForecastDisplay(weather_data)

        # TODO: Create two objects from StatisticsDisplay class and
        # ForecastDisplay class. Also register them to the concerete instance
        # of the Subject class so the they get the measurements' updates.

        # The StatisticsDisplay class should keep track of the min/average/max
        # measurements and display them.

        # The ForecastDisplay class shows the weather forcast based on the current
        # temperature, humidity and pressure. Use the following formuals :
        # forcast_temp = temperature + 0.11 * humidity + 0.2 * pressure
        # forcast_humadity = humidity - 0.9 * humidity
        # forcast_pressure = pressure + 0.1 * temperature - 0.21 * pressure

        weather_data.setMeasurements(80, 65, 30.4)
        weather_data.setMeasurements(82, 70, 29.2)
        weather_data.setMeasurements(78, 90, 29.2)

        # un-register the observer
        #weather_data.removeObserver(current_display)
        #weather_data.setMeasurements(120, 100,1000)


if __name__ == "__main__":
    w = WeatherStation()
    w.main()
