import machine                                     # Importa a biblioteca machine, responsavel pelo comando dos pinos, entre outras funcoes

import utime                                       # Importa a biblioteca utime, responsavel pela gestao de tempo


pinoLed = 15                                       # Declara a variável pinoLed e atribui o valor 15 a ela

incremento = 1285                                  # Declara a variável incremento e atribui o valor 1285 a ela

decremento = 1285                                  # Declara a variável decremento e atribui o valor 1285 a ela



led = machine.PWM(machine.Pin(pinoLed))            # Configura a porta 15 (valor da variável pinoLed) como saida do tipo PWM e da a ela o nome led

led.freq(1000)                                     # Define a frequencia do PWM para 1000 Hz (1 kHz)


while True:                                        
                                
   
                                                   
    for brilho in range(0,65535,incremento):       # Repete os comandos dentro da identacao aninhada 51 vezes (de acordo com a variavel incremento)
        
        led.duty_u16(brilho)                       # Controla o brilho no pino do LED
        
        utime.sleep_ms(30)                         # Aguarda 30 milissegundos
    
    
    for brilho in range(65535,0,-decremento):      # Repete os comandos dentro da identacao aninhada 51 vezes (de acordo com a variavel decremento)
        
        led.duty_u16(brilho)                       
        
        utime.sleep_ms(30)                         