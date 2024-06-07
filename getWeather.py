import python_weather
import asyncio
import os
from dataModels import WeatherData
from datetime import datetime


async def getweather():
    # declare the client. the measuring unit used defaults to the metric system (celcius, km/h, etc.)
    async with python_weather.Client(unit=python_weather.METRIC) as client:
        # fetch a weather forecast from a city
        weather = await client.get("Brugge")

        now = datetime.now()
        current_time = now.strftime("%H")
        closeTime = find_closest_digit(int(current_time))
        index = switch_case_dict(closeTime)

        # store data
        dailyData = []
        hourlyTime = []
        hourlyKind = []
        hourlyTemp = []

        # get the last (current) weather, by the most recent hour they can provide
        # from there we can access the time, kind of weather, etc.
        for daily in weather.daily_forecasts:
            dailyData.append(daily)
            latestItem = dailyData[0]
            for hourly in daily.hourly_forecasts:
                hourlyTime.append(hourly.time.strftime("%H"))
                hourlyKind.append(hourly.kind)
                hourlyTemp.append(hourly.temperature)

        # # recent date
        # WeatherData.date = latestItem.date
        # # recent time by hour
        # WeatherData.time = f"{current_time:2}:00:00"
        # # recent kind by hour
        # WeatherData.kind = hourlyKind[index]
        # # recent temp by hour
        # WeatherData.temp = hourlyTemp[index]

        # recent date
        date = str(latestItem.date)
        # recent time by hour
        time = f"{current_time:2}:00:00"
        # recent kind by hour
        kind = str(hourlyKind[index])
        # recent temp by hour
        temp = str(hourlyTemp[index])

        weatherData = WeatherData(date=date, time=time, kind=kind, temp=temp)
        return weatherData


def find_closest_digit(number):
    # Calculate the nearest multiple of 3
    nearest_multiple = round(number / 3) * 3
    return nearest_multiple


def switch_case_dict(value):
    cases = {
        0: 0,
        3: 1,
        9: 2,
        12: 3,
        15: 4,
        18: 5,
        21: 6,
        24: 6,
    }
    return cases.get(value, -1)


if __name__ == "__main__":
    # see https://stackoverflow.com/questions/45600579/asyncio-event-loop-is-closed-when-getting-loop
    # for more details
    if os.name == "nt":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(getweather())

    # # optional: just for checking
    # print(WeatherData.date)
    # print(WeatherData.time)
    # print(WeatherData.kind)
    # print(WeatherData.temp)
