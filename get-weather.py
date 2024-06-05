# import the module
import python_weather

import asyncio
import os


async def getweather():
    # declare the client. the measuring unit used defaults to the metric system (celcius, km/h, etc.)
    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
        # fetch a weather forecast from a city
        weather = await client.get("Brugge")

        weatherData = []
        dailyData = []

        # get the last (current) weather, by the most recent hour they can provide
        # from there we can access the time, kind of weather, etc.
        for daily in weather.daily_forecasts:
            dailyData.append(daily)
            latestItem = dailyData[0]
            for hourly in daily.hourly_forecasts:
                weatherLabel = hourly.kind

        weatherData.append({str(latestItem.date), str(hourly.time), str(weatherLabel)})

        return weatherData


if __name__ == "__main__":
    # see https://stackoverflow.com/questions/45600579/asyncio-event-loop-is-closed-when-getting-loop
    # for more details
    if os.name == "nt":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    weatherData = asyncio.run(getweather())

    # optional: just for checking
    for data in weatherData:
        print(data)
