import RPi.GPIO as GPIO


# Sätter hur den ska läsa pin
GPIO.setmode(GPIO.BOARD)
# Sätter vilka pins och om det I eller O'
btn = GPIO.setup(16, GPIO.IN)
relay = GPIO.setup(15, GPIO.OUT)


# connect button to GPIO BOARD 16, relay to GPIO BOARD 15,


def main():
    # might be able to read relay signal instead
    pwr = 0
    # run loop cheking if btn is pressed
    while True:
        # listening for a button press
        if btn == 1:
            # check if power is on or off
            if pwr == 0:
                # if power is off, we turn it on here
                print('The power is off,\n')
                pwr = 1
                print('The power is on\n')
            else:
                # if power is on, we turn it on here
                print('The power is on,\n')
                pwr = 0
                print('The power is off\m')

    '''
    while True:
        button = 0
        power = 0

        button = input('1 = button pressed')
        power = input('[0]PowerOff | [1]PowerOn')

        if button == '1':
            if power == '0':
                powerOn()
            elif power == '1':
                powerOff()
'''


if __name__ == '__main__':
    main()