import time
import hardware

set_temp = 145

while(1):
	temp = hardware.read_temperature()
	print "Current:",temp,"degrees F.  Target: ",set_temp

	if temp < set_temp:
		# Temp too low, enabling heater
		hardware.enable_heater()
	else:
		# Temp too high, disabling heater
		hardware.disable_heater()

	# Wait 30 seconds
	time.sleep(30)


