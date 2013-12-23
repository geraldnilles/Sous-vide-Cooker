PUMP_GPIO_NUM = 4
HEATER_GPIO_NUM = 4
SPIDEV = "/dev/spidev0.0"



def gpio_output_enable(number):
	f = open("/sys/class/gpio/export","w")
	f.write(str(number))
	f.close()

	f = open("/sys/class/gpio/gpio"+str(number)+"/direction","w")
	f.write("out")
	f.close()

def gpio_set(number):
	gpio_output_enable(number)

	f = open("/sys/class/gpio/gpio"+str(number)+"/value","w")
	f.write("1")
	f.close()

def gpio_clear():
	gpio_output_enable(number)

	f = open("/sys/class/gpio/gpio"+str(number)+"/value","w")
	f.write("0")
	f.close()


# Reads the current tempreature from the ADC IC
def read_temperature():
	f = open(SPIDEV,"rb")
	data = f.read(4)
	f.close()

	print repr(data)

	# convert the first 16 bits to an signed short
	short = struct.unpack("<h",data)

	# Get the last 2 bits by dividing by 2^2 (4)
	shifted = data/(4)

	# convert 1/4 degrees units to a degrees C
	tempC = shifted / 4.0

	tempF = tempC * 9 / 5 + 32

	print tempC, tempF

	return tempF


# Enables the circulating water pump
def enable_pump():
	gpio_output_clear(PUMP_GPIO_NUM)

# Disable the circulating water pump
def disable_pump():
	gpio_output_set(PUMP_GPIO_NUM)

# Enable Heating Coil
def enable_heater():
	gpio_output_clear(HEATER_GPIO_NUM)

# Disable Heating Coil
def disable_heater():
	gpio_output_set(HEATER_GPIO_NUM)



