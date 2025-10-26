import machine                                          
import utime                                            

pinoLed_R = 16                                          

pinoLed_G = 17                                          
pinoLed_B = 18                                          

pinoPot = 27                                            

valorPot = 0                                            


def acendeVermelho():
    
    led_R.value(0)                                      
    
    led_G.value(1)                                      
    
    led_B.value(1)                                      
    

def acendeVerde():
    
    led_R.value(1)                                      
    
    led_G.value(0)                                      
    
    led_B.value(1)                                      
    

def acendeAzul():
    
    led_R.value(1)                                      
    
    led_G.value(1)                                      
    
    led_B.value(0)                                      

def apagaLed():
    
    led_R.value(1)                                      
    
    led_G.value(1)                                      
    
    led_B.value(1)                                      


led_R = machine.Pin(pinoLed_R, machine.Pin.OUT)         

led_G = machine.Pin(pinoLed_G, machine.Pin.OUT)         

led_B = machine.Pin(pinoLed_B, machine.Pin.OUT)         

pot = machine.ADC(pinoPot)                              

while True:                                             
                                                        
    valorPot = pot.read_u16()                          
    
    if valorPot >= 0 and valorPot <= 16384:            
    
        apagaLed()                                      
        
    if valorPot > 16384 and valorPot <= 32768:         
        acendeVermelho()                                
 
    if valorPot > 32768 and valorPot <= 49152:         

        acendeVerde()                                   
    
    if valorPot > 49152 and valorPot <= 65535:         

        acendeAzul()                                    