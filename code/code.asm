;
; Sous-Vide Cooking MCU Code
;

; Setup
; Read Temperature from EEPROM
; Setup UARTRX Interrupt
; Setup Timer Interrupt
; Setup ADC INterrupt



; Timer Interrupt: Occurs once a second
TIMER:
TEMP = Ambient*A + Water*B
if TEMP > SETTEMP
Disable Relay
else
Enable Relay
RETFIE                          ; Return from interrupt


; ADC Interrupt
ADC:
if ADC Channel is 1
store ADC result in Ambient
Set ADC channel to 2
else
store ADC result in Water
set ADC channel to 1
RETFIE                          ; Return From Interrupt


; UART RX Interrupt
UARTRX:
if DATA = 0x00                  ; Computer is asking for current temp data
Set TX register to TEMP
else
Set TEMP to TX                  ; Computer is sending a temp to set
RETFIE                          ; Return from Interrupt
