// Code


// Global Variables
unsigned char period = 0xff; // Period of cycle in seconds
unsigned char duty = 100; // Duty cycle of Heating Element
unsigned char counter = 0; // Keeps track of current position in cycle
unsigned char set_temp = 140;
unsigned char curr_temp = 0;

int main(){

	// Setup the Timer Register to fire once a second
	// Set all of the GPIO Input/Outputs
	//
}

// 120Hz Interrupt
// I fear that the pump has a 120V to 12V transformer inside of this.  Therefore, it will need an AC source.
// To get aound this, we will probably need to switch the 170V rail at 60Hz
void Timer0_Interrupt(){
	if (MOSFET IS  ON){
		TURN MOSFET OFF
	}else{
		TURN MOSFET ON
	}
}

// Timer Interupt Routine
// This function will be called once a second (roughly)
void Timer_Interrupt(){
	counter++;
	if (counter <= duty){
		// Turn on Heater/pump
	}else{
		// Turn off Heater/Pump
	}

	if(counter >= period){ // End of Cycle Reached
		counter = 0;
		// Calculate the next cycle's duty cycle using PID
		set_duty_cycle();
	}
	// Toggle Heatbeat LED

	// Setup ADC to do a single read
}

// ADC Interrupt Routine
// This function will be called once the ADC has finished reading the 
// temperature of the water.
void ADC_Interrupt(){
	// Read ADC Register
	// Convert to Degrees F
	update_LCD();
}

void update_LCD(){
	// Send the Current Temp and Set temp to the Display screen
}

unsigned int integral = 0
unsigned char prev_error = 0
void set_duty_cydle(){
	unsigned char error = set_temp - curr_temp;
	integral = integral + (int) error;
	unsigned char de_dt = error - prev_error;

	duty = kp*error + kd*de_dt + ki*integral;
}
