#!/usr/bin/env python


def main():
	BUTTON()


def BUTTON():
	# if button for power off is pressed this happens
	btn = 0
	# when fysical button is pressed btn = 1
	if btn == 1:
		# check if power is on or off
		if power == 0:
			powerOn()
		elif power == 1:
			powerOff()


def power():
	# check sensor, if Amp is lower then 0.8
	ampSensor = 0
	ampSensor = input('off(0) or on(1)')
	print(ampSensor)

def powerOn():
	# if power = 0, we send signal to power on
	print('The power is ON')
	power.ampSensor = input(1)

def powerOff():
	# if power = 1, we send signal to power off
	print('The power is OFF')


if __name__ == '__main__':
	main()
