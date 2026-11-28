from modules.buzzer import Buzzer
import uasyncio as asyncio

buzzer = Buzzer(14)

async def welcome():
    await buzzer.EasyPlay([("B4", 1.5, 0.01), ("A4", 1.5, 0.01), ("G4", 1.5, 0.01)])

asyncio.run(welcome())    