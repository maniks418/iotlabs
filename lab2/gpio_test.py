#!/usr/bin/python
import time
import gpio


# create an instance of the pi gpio driver.
pigpio = gpio.PiGpio()
print('Blinking all my LEDs in sequence (Ctrl-C to stop)...')
while True:
    # Get the current switch state and print

    # switch = pigpio.read_switch()
    # print('\n============ Switch: {0} ============'.format(switch))
    print('\nLED 1 ON (RED)')
    pigpio.set_led(1, True)
    print('LED1: {0}'.format(pigpio.get_led(1)))
    print('LED2: {0}'.format(pigpio.get_led(2)))
    print('LED3: {0}'.format(pigpio.get_led(3)))
    time.sleep(1.0)

    print('\nLED 2 ON (GRN)')
    pigpio.set_led(2, True)
    print('LED1: {0}'.format(pigpio.get_led(1)))
    print('LED2: {0}'.format(pigpio.get_led(2)))
    print('LED3: {0}'.format(pigpio.get_led(3)))
    time.sleep(1.0)

    print('\nLED 3 ON (BLU)')
    pigpio.set_led(3, True)
    print('LED1: {0}'.format(pigpio.get_led(1)))
    print('LED2: {0}'.format(pigpio.get_led(2)))
    print('LED3: {0}'.format(pigpio.get_led(3)))
    time.sleep(1.0)

    print('\nLED 1 OFF (RED)')
    pigpio.set_led(1, False)
    print('LED1: {0}'.format(pigpio.get_led(1)))
    print('LED2: {0}'.format(pigpio.get_led(2)))
    print('LED3: {0}'.format(pigpio.get_led(3)))
    time.sleep(1.0)

    print('\nLED 2 OFF (GRN)')
    pigpio.set_led(2, False)
    print('LED1: {0}'.format(pigpio.get_led(1)))
    print('LED2: {0}'.format(pigpio.get_led(2)))
    print('LED3: {0}'.format(pigpio.get_led(3)))
    time.sleep(1.0)

    print('\nLED 3 OFF (BLU)')
    pigpio.set_led(3, False)
    print('LED1: {0}'.format(pigpio.get_led(1)))
    print('LED2: {0}'.format(pigpio.get_led(2)))
    print('LED3: {0}'.format(pigpio.get_led(3)))
    time.sleep(1.0)
