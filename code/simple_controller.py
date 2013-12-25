import time
import hardware

set_temp = 130

on_time = 0.0
off_time = 0.0

while(1):
	temp = hardware.read_temperature()
	print "Current:",temp,"degrees F.  Target: ",set_temp

	if on_time == 0 and off_time == 0:
		pass
	else:
		print "Duty Cycle: ",int((on_time / (off_time+on_time))*100),"%"


	if temp < set_temp:
		# Temp too low, enabling heater
		hardware.enable_heater()
		on_time += 1.0
	else:
		# Temp too high, disabling heater
		hardware.disable_heater()
		off_time += 1.0

	# Wait 30 seconds
	time.sleep(30)


