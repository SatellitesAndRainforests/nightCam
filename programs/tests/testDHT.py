import Adafruit_DHT
import os
import time

DHT_SENSOR = Adafruit_DHT.DHT22
GPIO_PIN = 24

while True:
    try:

        humidity, temperature = Adafruit_DHT.read_retry( DHT_SENSOR, GPIO_PIN )

        tempC = temperature
        tempF = temperature * (9 / 5) + 32

        print(
                "Temp: {:.1f} F / {:.1f} C    Humidity: {:.1f}% ".format(
                    tempF, tempC, humidity
                    )
                )

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
    except KeyboardInterrupt:
        dhtDevice.exit()
        print('exiting script')
    time.sleep(2.0)



