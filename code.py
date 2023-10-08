"""
T2310_pwr_ina219
Author:	Tom Hoglund 2023
git:	https://github.com/infrapale/T2310_pwr__ina219

Based on :Sample code and test for adafruit_ina219
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
"""

import time
import board
import busio
import digitalio
import neopixel
from adafruit_ina219 import ADCResolution, BusVoltageRange, INA219


i2c_bus = board.I2C()  # uses board.SCL and board.SDA
# i2c_bus = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
ina219 = INA219(i2c_bus)
PIXEL_PIN = board.NEOPIXEL
ORDER = neopixel.GRB
COLOR_GREEN = (0, 255, 0)
COLOR_RED = (255, 0, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_CYAN = (0, 255, 255)
COLOR_MAGENTA = (255, 0, 255)

pixel = neopixel.NeoPixel(
    PIXEL_PIN, 1, brightness=0.2, auto_write=True, pixel_order=ORDER
)

pixel[0] = COLOR_GREEN

print("T2310_pwr_ina219.py by Tom Hoglund")
'''
print("Config register:")
print("  bus_voltage_range:    0x%1X" % ina219.bus_voltage_range)
print("  gain:                 0x%1X" % ina219.gain)
print("  bus_adc_resolution:   0x%1X" % ina219.bus_adc_resolution)
print("  shunt_adc_resolution: 0x%1X" % ina219.shunt_adc_resolution)
print("  mode:                 0x%1X" % ina219.mode)
print("")
'''

# optional : change configuration to use 32 samples averaging for both bus voltage and shunt voltage
ina219.bus_adc_resolution = ADCResolution.ADCRES_12BIT_32S
ina219.shunt_adc_resolution = ADCResolution.ADCRES_12BIT_32S
# optional : change voltage range to 16V
#ina219.bus_voltage_range = BusVoltageRange.RANGE_16V

# measure and display loop
while True:
    cmd = input()
    #print (rd_cmd)
    if cmd == 'I':
        current = int(ina219.current)  # current in mA        
        print("{}".format(current))
        pixel[0] = COLOR_CYAN
    elif cmd == 'U':
        bus_voltage = ina219.bus_voltage
        print("{}".format(int(bus_voltage*1000)))
        pixel[0] = COLOR_MAGENTA
    else:
        pixel[0] = COLOR_RED
        
    #bus_voltage = ina219.bus_voltage  # voltage on V- (load side)
    #shunt_voltage = ina219.shunt_voltage  # voltage between V+ and V- across the shunt
    #current = int(ina219.current)  # current in mA
    #power = ina219.power  # power in watts
    # INA219 measure bus voltage on the load side. So PSU voltage = bus_voltage + shunt_voltage
    #print("Voltage (VIN+) : {:6.3f}   V".format(bus_voltage + shunt_voltage))
    #print("Voltage (VIN-) : {:6.3f}   V".format(bus_voltage))
    #print("Shunt Voltage  : {:8.5f} V".format(shunt_voltage))
    #print("Shunt Current  : {:7.4f}  A".format(current / 1000))
    #print("{}".format(current))
    #print("Power Calc.    : {:8.5f} W".format(bus_voltage * (current / 1000)))
    #print("Power Register : {:6.3f}   W".format(power))
    #print("")

    # Check internal calculations haven't overflowed (doesn't detect ADC overflows)
    if ina219.overflow:
        print("Internal Math Overflow Detected!")
        print("")

    #time.sleep(0.01)

