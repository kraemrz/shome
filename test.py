def main():
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


def powerOn():
    print('The power is now ON')


def powerOff():
    print ('The power is now OFF')

if __name__ == '__main__':
    main()