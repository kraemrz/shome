#!/usr/bin/env python


def main():
    while True:
        pressed = input('1 = button press')
        btn = int(pressed)
        BUTTON(btn)


def BUTTON(btn):
    # if button for power off is pressed this happens
    # when fysical button is pressed btn = 1
    print(btn)
    if btn == 1:
        print('checking.....')
        ampSensor = input('is power [0]OFF or [1]On:')
        power = int(ampSensor)
        # check if power is on or off
        if power == 1:
            powerOn()
        elif power == 0:
            powerOff()


def powerOn():
    # if power = 0, we send signal to power on
    print('The power is ON')
    print('''
    ********
    *      *
    *  **  *
    *  **  *
    ********
    ''')
    print('turning power OFF\n')


def powerOff():
    # if power = 1, we send signal to power off
    print('The power is OFF')
    print('''
        ********
        *  **  *
        *  **  *
        *      *
        ********
        ''')
    print('turning power ON\n')


if __name__ == '__main__':
    main()
