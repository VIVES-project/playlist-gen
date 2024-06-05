# import the module
import python_weather

import asyncio
import os


async def getweather():
    # declare the client. the measuring unit used defaults to the metric system (celcius, km/h, etc.)
    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
        # fetch a weather forecast from a city
        weather = await client.get("Brugge")

        # returns the current day's forecast temperature (int)
        # print(f"Date:{weather.datetime} \n Temp:{weather.temperature}\n")

        # get the weather forecast for a few days
        for daily in weather.daily_forecasts:
            latestItem = daily
            for hourly in daily.hourly_forecasts:
                weatherLabel = hourly.kind

        print(latestItem.date)
        print(hourly.time)
        print(weatherLabel)


if __name__ == "__main__":
    # see https://stackoverflow.com/questions/45600579/asyncio-event-loop-is-closed-when-getting-loop
    # for more details
    if os.name == "nt":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(getweather())
