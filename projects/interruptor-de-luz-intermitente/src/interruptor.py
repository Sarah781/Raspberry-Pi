import machine                                                               
import utime                                                                 


pinoBotao = 16                                                             
pinoLed = 15                                                                 
estadoLed = 0                                                                
estadoBotao = 0                                                              


led = machine.Pin(pinoLed, machine.Pin.OUT)                                  

botao = machine.Pin(pinoBotao, machine.Pin.IN, machine.Pin.PULL_UP)          

while True:                                                                 
                                                                             
    estadoBotao = botao.value()                                              
    
    estadoLed = not estadoBotao                                              
    
    led.value(estadoLed)                                                     
    
    utime.sleep_ms(10)                                                       