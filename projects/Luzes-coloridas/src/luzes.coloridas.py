import machine                                          # Importa a biblioteca machine, responsavel pelo comando dos pinos, entre outras funcoes
import utime                                            # Importa a biblioteca utime, responsavel pela gestao de tempo


pinoLed_R = 16                                          # Declara a variável led_R e atribui o valor 16 a ela

pinoLed_G = 17                                          # Declara a variável led_G e atribui o valor 17 a ela

pinoLed_B = 18                                          # Declara a variável led_B e atribui o valor 18 a ela


def acendeVermelho():
    
    led_R.value(0)                                      # Acende a cor Vermelha do LED
    
    led_G.value(1)                                      # Apaga a cor Vermelha do LED
    
    led_B.value(1)                                      # Apaga a cor Vermelha do LED
    


def acendeVerde():
    
    led_R.value(1)                                      # Apaga a cor Vermelha do LED
    
    led_G.value(0)                                      # Acende a cor Vermelha do LED
    
    led_B.value(1)                                      # Apaga a cor Vermelha do LED
    


def acendeAzul():
    
    led_R.value(1)                                      # Apaga a cor Vermelha do LED
    
    led_G.value(1)                                      # Apaga a cor Vermelha do LED
    
    led_B.value(0)                                      # Acende a cor Vermelha do LED
    


def apagaLed():
    
    led_R.value(1)                                      # Apaga a cor Vermelha do LED
    
    led_G.value(1)                                      # Apaga a cor Vermelha do LED
    
    led_B.value(1)                                      # Apaga a cor Vermelha do LED



led_R = machine.Pin(pinoLed_R, machine.Pin.OUT)         # Configura a porta 11 (valor da variável pinoLed_R) como saida e da a ela o nome led_R

led_G = machine.Pin(pinoLed_G, machine.Pin.OUT)         # Configura a porta 12 (valor da variável pinoLed_G) como saida e da a ela o nome led_G

led_B = machine.Pin(pinoLed_B, machine.Pin.OUT)         # Configura a porta 13 (valor da variável pinoLed_B) como saida e da a ela o nome led_B


while True:                                             
                                
    acendeVermelho()                                    # Chama a funcao de acender a cor Vermelha do LED e apagar as demais
  
    utime.sleep_ms(1000)                                # Aguarda 1000 milissegundos (1 segundo)
  
    acendeVerde()                                       # Chama a funcao de acender a cor Verde do LED e apagar as demais
  
    utime.sleep_ms(1000)                                # Aguarda 1000 milissegundos (1 segundo)
  
    acendeAzul()                                        # Chama a funcao de acender a cor Azul do LED e apagar as demais
  
    utime.sleep_ms(1000)                                # Aguarda 1000 milissegundos (1 segundo)
  
    apagaLed()                                          # Chama a funcao de apagar todas as cores do LED
  
    utime.sleep_ms(1000)                                # Aguarda 1000 milissegundos (1 segundo)