## Tunable Variables

set_temp = 120 # degrees F
curr_temp = 120 # degrees F
period = 60 # seconds
dutycycle = 0 # Seconds

# PID variables.  Tuning this will affect how fast the water heats up
Kp = 5
Ki = 0.1
Kd = 0
temp_hist = []
hist_length = 100

# Add a temp reading to the temp history.  Cap the max number of readings
def record_temp():
	temp = hardware.read_temp()
	# If greater than the history_length, remove one
	if len(temp_hist) >= hist_length:
		temp_hist = temp_hist[1:]


	temp_hist.append(temp)


def calculate_dutycycle():
	record_temp()

	# Calculate the P portion
	P_error = set_temp - temp_hist[-1]


	# Calculate the I Portion
	I_error = 0
	for t in hist_length:
		I_error += set_temp - t

	dutycycle = Kp*P_error + Ki*I_error

	# bookened the duty cycle by zero and the period
	if dutycycle < 0:
		dutycycle = 0
	if dutycycle > period:
		dutycycle = period


def handle_communication(conn):
	req = libsock.recv(conn)

	resp = {}

	if req["command"] == "current_temp":
		resp["data"] = temp_hist[-1]
	
	elif req["command"] == "history":
		resp["data"] = temp_hist
	
	elif req["command"] == "set":
		curr_temp = data["temp"]
	else:
		resp["data"] = "ERROR - No Command Provided"
	
	conn.send(libsock.json_to_pkt(resp))

def loop_forever():

	# Initialize the PWM counter
	i = 0

	# Create a Unix Socket to listen to
	s = socket.socket(...)
	# Set Timeout to 1 second
	s.settimeout(1)

	while(1):
		# Wait 1 second for a new socket connection
		try:
			# Accept the new connection
			conn,addr = s.accept()
			# Handle the new connection
			handle_communication(conn)
			# Close the connection
			conn.close()

		# Catch if there is no connection for 1 second
		except socket.TIMEOUT:
					
			# Service the Hardware (depending on duty cycle)
			if i < dutycycle:
				hardware.enable_heater()
				hardware.enable_pump()
			else:
				hardware.disable_heater()
				hardware.disable_pump()
	

			# Service PWM Counter
			if i > period:
				# When the counter exceeds the period
				# ... reset the PWM counter
				i = 0
				## Recauculate Duty Cycle based on temp
				dutycycle = calculate_dutycycle()
			else:
				i++
	




if __name__ == "__main__":
	loop_forever()
