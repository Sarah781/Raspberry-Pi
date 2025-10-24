import machine                                  # Importa a biblioteca machine, responsavel pelo comando dos pinos, entre outras funcoes

import utime                                    # Importa a biblioteca utime, responsavel pela gestao de tempo


pinoLed = 15                                    # Declara a variável pinoLed e atribui o valor 15 a ela


led = machine.Pin(pinoLed, machine.Pin.OUT)     # Configura a porta 15 (valor da variável pinoLed) como saida e da a ela o nome led


while True:                                  
    
    for x in range(0,3):                        # Repete os comandos dentro da tabulacao aninhada 3 vezes
        
        led.value(1)                            # Acende o LED
        
        utime.sleep_ms(150)                     # Aguarda 150 milissegundos
        
        led.value(0)                            # Apaga o LED
        
        utime.sleep_ms(150)                     # Aguarda 150 milissegundos
        
    utime.sleep_ms(200)                         # Aguarda 200 milissegundos entre as letras
    

    
    for x in range(0,3):                        # Repete os comandos dentro da tabulacao aninhada 3 vezes
        
        led.value(1)                            # Acende o LED
        
        utime.sleep_ms(450)                     # Aguarda 450 milissegundos
        
        led.value(0)                            # Apaga o LED
        
        utime.sleep_ms(150)                     # Aguarda 150 milissegundos
        
    utime.sleep_ms(200)                         # Aguarda 200 milissegundos entre as letras
 
  
 
    for x in range(0,3):                        # Repete os comandos dentro da tabulacao aninhada 3 vezes                                      
        
        led.value(1)                            # Acende o LED
        
        utime.sleep_ms(150)                     # Aguarda 150 milissegundos
        
        led.value(0)                            # Apaga o LED
        
        utime.sleep_ms(150)                     # Aguarda 150 milissegundos
        
    utime.sleep_ms(3000)                        # Aguarda 5000 milissegundos (5 segundos)