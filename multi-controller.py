import asyncio, evdev

player1 = evdev.InputDevice('/dev/input/event4')
player2 = evdev.InputDevice('/dev/input/event5')

async def print_events(device):
    async for event in device.async_read_loop():
        if event.type == evdev.ecodes.EV_KEY:
            print(evdev.categorize(event))

for device in player1, player2:
    asyncio.ensure_future(print_events(device))

loop = asyncio.get_event_loop()
loop.run_forever()