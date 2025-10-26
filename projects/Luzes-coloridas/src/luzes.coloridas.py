import machine                                          # Importa a biblioteca machine, responsavel pelo comando dos pinos, entre outras funcoes
import utime                                            # Importa a biblioteca utime, responsavel pela gestao de tempo


pinoLed_R = 16                                          # Declara a variável led_R e atribui o valor 16 a ela

pinoLed_G = 17                                          # Declara a variável led_G e atribui o valor 17 a ela

pinoLed_B = 18                                          # Declara a variável led_B e atribui o valor 18 a ela


def acendeVermelho():                                   # Acende Vermelho
    led_R.value(0)
    led_G.value(1)
    led_B.value(1)

def acendeRoxo():                                       # Acende Roxo(mistura de Vermelho e Azul)
    led_R.value(0)
    led_G.value(1)
    led_B.value(0)

def acendeVerde():                                      # Acende verde
    led_R.value(1)
    led_G.value(0)
    led_B.value(1)

def acendeAmarelo():                                    # Acende Amarelo (mistura Vermelho e Verde)
    led_R.value(0)
    led_G.value(0)
    led_B.value(1)

def acendeCiano():                                      # Acende Ciano (mistura Verde e Azul)
    led_R.value(1)
    led_G.value(0)
    led_B.value(0)

def acendeAzul():                                       # Acende Azul
    led_R.value(1)
    led_G.value(1)
    led_B.value(0)


def apagaLed():
    
    led_R.value(1)                                      # Apaga a cor Vermelha do LED
    led_G.value(1)                                      # Apaga a cor Verde do LED
    led_B.value(1)                                      # Apaga a cor Azul do LED



led_R = machine.Pin(pinoLed_R, machine.Pin.OUT)  
led_G = machine.Pin(pinoLed_G, machine.Pin.OUT)         
led_B = machine.Pin(pinoLed_B, machine.Pin.OUT)         


while True:                                             
                                
    acendeVermelho()
    utime.sleep_ms(1000)
    
    acendeVerde()
    utime.sleep_ms(1000)
    
    acendeAmarelo()
    utime.sleep_ms(1000)
    
    acendeCiano()
    utime.sleep_ms(1000)
    
    acendeRoxo()
    utime.sleep_ms(1000)
    
    acendeAzul()
    utime.sleep_ms(1000)                                # Aguarda 1000 milissegundos (1 segundo)
  
    apagaLed()                                          # Chama a funcao de apagar todas as cores do LED
    utime.sleep_ms(1000)                                # Aguarda 1000 milissegundos (1 segundo)