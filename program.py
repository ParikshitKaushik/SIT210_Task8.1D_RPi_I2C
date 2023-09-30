import smbus
import time

TIME_BETWEEN_READINGS = 1
TOO_BRIGHT = 200  
BRIGHT = 150     
MEDIUM = 100     
DARK = 50        
TOO_DARK = 30     
SENSOR = 0x23

CONTINUOS_HIG_RES_MODE = 0x13

bus = smbus.SMBus(1)

def getLightReading():
    reading = bus.read_i2c_block_data(SENSOR, CONTINUOS_HIG_RES_MODE)
    return reading[1]

def getBrightnessRanking(lux):
    if lux > TOO_BRIGHT:
        return "Too Bright"
    elif lux > BRIGHT:
        return "Bright"
    elif lux > MEDIUM:
        return "Medium"
    elif lux > DARK:
        return "Dark"
    else:
        return "Too Dark"

def main():
    while True:
        lightLevel = getLightReading()
        print("Light is " + getBrightnessRanking(lightLevel))
        time.sleep(TIME_BETWEEN_READINGS)

if __name__ == "__main__":
    main()