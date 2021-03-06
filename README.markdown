# Sous-vide Cooker

The goal of this project is to creat a cheap Sous-Vide cooker using cheap electronic components and items already in my kitchen.

# About Sous-Vide
Sous-Vide is a special slow cooker that uses heated water to cook meat.
Rather than heating the air (like in an oven) or oil (like in a deep frier), sous-vide uses water to transfer heat.
To keep the meat's juices in, the meat is contained in an air-tight vaccume bag.

The differnce between Sous-Vide and a Crock Pot is that sous-vide meat does not lose any moisure.

# Major Components

## Container
I will use a large plastic thermos.  
The kind used to keep liquids cold on a picnic.

THis container is cheap and just big enough to fit most types of meat.

## Heater
In order to heat the water, we will use a low power heating coil.

THis heater will be turned on and off using a relay and powered by AC wall power.

## Pump
To keep the water temeprature even throughout the container, we will need a water pump.
I will use a cheap foutain pump to circulate the water.

This pump will be turned on and off using a relay and powered by the AC wall power.

## Temperature Reading
In order to maintain and exact water temperature, we will need a thermometer.
I will use thermocouples to do this.
Thermocouples are very cheap and can handle wide varieties of conditions.

However, thermocouples are relative measuring devices so we will need to know the ambiet temperature in order to properly measure the water temperature.
TO do this, we will use a thermistor that stays at the base of the thermocouples.

## Communication
In order to set tempreatures and report tempreatures, a bluetooth modem will be used to communicate with a nearby PC.

Initially i wanted to use a 7-segment deisplay, but found that there are many cheap bluetooth transievers that would keep things simple.

I will just need to find a UART to BT transiever that im set!

You can buy whole modules for $7 to $15. 
This one looks [Promising](http://air.imag.fr/mediawiki/index.php/Wireless_Bluetooth_RS232_TTL_Transceiver_Module) and only costs 4$
This transcevier will handle the entire BT stack and simply act like a UART port

Or you can buy an SOC from Nordic which looks promising

## Control
ALl of the above circuits will be controlled by a MCU.
The type of MCU is TBD.
ALl it will need to do is communicate over UART and have ADC capabilities.

### MCU Requirements
* 2 ADC Inputs
* UART Communication
* 5V Operating voltage

PIC12F1822 is an 8Bit part with 2 ADC channels, a UART communication path.
COul be good!  Base part is that it only costs $1.38 on mouser.

2 inpus for ADC
2 Pins for UART
1 pin for REST
1 pin for Relay control
2 pins for PWR and GND

### Programmer
I should be able to program a PIC using an adruino board.  We'll see.

# User Interface
Setting tempreatures will be done on a computer using bluetooth.

The program will likely be written in Python and simply read/write UART commands to the device.

This will (a) make the project cool and (b) actaully be cheaper and easier than  adding multipler buttons and an LCD.


# Softare

## MCU Code
C code or assembly

It will either toggle the relays or create a 60Hz square wave

### Compiler
We will need to find a PIC compiler

GPUTILS looks like a good assembler/linker that we could use.

## Computer Code
Python code to read/write commands from/to the MCU.

A serial port will be used.
It can either be a USB to serial adaptor or it can us bluetooth.
