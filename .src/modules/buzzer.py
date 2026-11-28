from machine import Pin, PWM
import uasyncio as asyncio
class Buzzer:
    melody = {
        "C4" : 262,
        "D4" : 294,
        "E4" : 330,
        "F4" : 349,
        "G4" : 392,
        "A4" : 440,
        "B4" : 494,
        "C5" : 523
    }
    def __init__(self, pin: int):
        self.pwm = PWM(Pin(pin), freq = 2000, duty_u16 = 0)
    async def Play(self, note: str, UsageTime: int, WaitTime: int):
        freq  = self.melody.get(note, 0)
        if freq > 0:
            self.pwm.freq(freq)
            self.pwm.duty_u16(32768)
        else:
            self.pwm.duty_u16(0)
        await asyncio.sleep(UsageTime)
        self.pwm.duty_u16(0)
        await asyncio.sleep(WaitTime)
    async def EasyPlay(self, notes: list):
        for note, duration, wait in notes:
            await self.Play(note, duration, wait)