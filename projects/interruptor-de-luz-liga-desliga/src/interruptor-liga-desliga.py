
import machine                                                               
import utime                                                                 


pinoBotao = 16                                                               

pinoLed = 15                                                                 

estadoLed = 0                                                                

estadoBotao = 0                                                              


led = machine.Pin(pinoLed, machine.Pin.OUT)                                 

botao = machine.Pin(pinoBotao, machine.Pin.IN, machine.Pin.PULL_UP)          

while True:                                                                  
                                                                             
    if botao.value() == 0 :                                                  

        estadoLed = not estadoLed                                           
        
        led.value(estadoLed)                                                 
        
        while botao.value() == 0:                                            
            
            pass                                                             
        
    utime.sleep_ms(100)                                                    