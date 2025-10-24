import machine                                 
import utime                                    

pinoLed = 15  
led = machine.Pin(pinoLed, machine.Pin.OUT)     

while True:                                     
                                                
                                          
    led.value(1)     # Acende o LED
    
    utime.sleep(1)   # Aguarda o intervalo de tempo entre parenteses em segundos
    
    led.value(0)     # Apaga o LED
    
    utime.sleep(1)   # Aguarda o intervalo de tempo entre parenteses em segundos