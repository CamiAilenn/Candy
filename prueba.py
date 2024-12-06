import pygame
from colores import *
from Candy_Crush import *
pygame.init()       #iniciar la pantalla
#declarar constantes
ANCHO_VENTANA = 1200
ALTO_VENTANA = 700
POS_TIMER = (1000,100)
segundos = "10"
fin_tiempo = False
nombre_archivo = "Jugadores_Candy.csv"
filas = 4
columnas = 7
clave = "Piezas"
inicio_piezas = 1
fin_piezas = 3
bandera_ganador = False
contador_ganador = 0
contador_perdedor = 0


def preparar_armado_lista(tablero, i, clave, j,imagen_caramelo_uno,posicion_caramelo,lista_caramelos):
    numero = numero_en_posicion(tablero, i, clave, j)
    if numero == 1:
        pantalla.blit(imagen_caramelo_uno,posicion_caramelo)
        if len(lista_caramelos[0]["Numero"])<=filas*columnas:
            armar_lista_caramelos(lista_caramelos, numero, posicion_caramelo, i, j)
    elif numero == 2: 
        pantalla.blit(imagen_caramelo_dos,(posicion_caramelo))
        if len(lista_caramelos[0]["Numero"])<= filas*columnas:
            armar_lista_caramelos(lista_caramelos, numero, posicion_caramelo, i, j)
    else:
        pantalla.blit(imagen_caramelo_tres,(posicion_caramelo))
        if len(lista_caramelos[0]["Numero"])<=filas*columnas:
            armar_lista_caramelos(lista_caramelos, numero, posicion_caramelo, i, j)

tablero = generar_tablero(filas, columnas, clave, inicio_piezas, fin_piezas)
lista_caramelos = iniciar_lista_caramelos()

#PANTALLA
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))   # Creo la pantalla
pygame.display.set_caption("Three Candy en columna")     # Pongo un titulo en la ventana

#IMAGENES
imagen_logo = pygame.image.load("candy_logo.jpg")
imagen_jugar =pygame.image.load("jugar.jpg")
imagen_caramelo_uno = pygame.image.load("caramelo_uno.png")
imagen_caramelo_dos = pygame.image.load("caramelo_dos.jpg")
imagen_caramelo_tres = pygame.image.load("caramelo_tres.png")
imagen_jugar_de_nuevo = pygame.image.load("jugar_de_nuevo.jpg")

#TAMAÑO DE LAS IMAGENES
imagen_logo =pygame.transform.scale(imagen_logo,(800,600))
imagen_jugar =pygame.transform.scale(imagen_jugar,(150,75))
imagen_caramelo_uno = pygame.transform.scale(imagen_caramelo_uno,(100,100))
imagen_caramelo_dos = pygame.transform.scale(imagen_caramelo_dos,(100,100))
imagen_caramelo_tres = pygame.transform.scale(imagen_caramelo_tres,(100,100))
imagen_jugar_de_nuevo = pygame.transform.scale(imagen_jugar_de_nuevo,(300,100))


posicion_mouse = pygame.Rect(0,0,6,6)
posicion_logo = [200, 65]
posicion_jugar = [1025, 500]
posicion_jugar_de_nuevo = [800,400]


timer_segundos = pygame.USEREVENT                   #Defino un Timer
pygame.time.set_timer(timer_segundos,1000)          #1000 es 1 segundo


fuente_timer = pygame.font.SysFont("Comic Sans", 80)      # Defino texto que ingresa usuario


font_input = pygame.font.SysFont("Arial", 50)       #Ingreso de texto del usuario
ingreso = ""
ingreso_rect = pygame.Rect(100,200,500,100)

#TEXTOS
fuente_texto = pygame.font.SysFont("Comic Sans", 30)           #el texto va a ser una superficie
mensaje = "hola"
texto = fuente_texto.render(mensaje , True, GREEN1)    #transforma el texto en una imagen



flag_correr = True          # El juego corre mientras la bandera esta True
flag_primer_pantalla = True
flag_pantalla_juego = True
flag_pantalla_final = True

while flag_correr:

    while flag_primer_pantalla:
        #posicion_mouse = pygame.Rect(0,0,6,6)
        lista_eventos = pygame.event.get()      # Guardo los eventos de la ventada en una lista
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:      # Si el tipo de evento es SALIR (detecta si el usuario cierra la ventana)
                flag_primer_pantalla = False
                flag_correr = False
                flag_pantalla_juego = False
                flag_pantalla_final = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                posicion_click = list(evento.pos)     #print(evento.pos)  me imprime la posicion donde se hizo click
                posicion_mouse[0] = posicion_click[0]   #modifico el left del rect
                posicion_mouse[1] = posicion_click[1]
      
        pantalla.fill(TURQUOISE3)
        pantalla.blit(imagen_logo, posicion_logo)
        pantalla.blit(imagen_jugar, posicion_jugar)
        rect_posicion_jugar = pygame.Rect(posicion_jugar[0],posicion_jugar[1], 150, 75)
        if posicion_mouse.colliderect(rect_posicion_jugar):
            flag_primer_pantalla = False

        pygame.display.flip()  
    contador_ganador = 0
    
    while flag_pantalla_juego:

        flag_juego = True       #Para volver a entrar al juego
        posicion_mouse = pygame.Rect(0,0,6,6)       #Posicion del mouse vuelve a 0 porque sino mantiene en memoria la anterior
        tablero = generar_tablero(filas, columnas, clave, inicio_piezas, fin_piezas)        #Genero el tablero de nuevo
        lista_caramelos = iniciar_lista_caramelos()
        while flag_juego:
            lista_eventos = pygame.event.get()      # Guardo los eventos de la ventada en una lista
            for evento in lista_eventos:
                if evento.type == pygame.QUIT:      # Si el tipo de evento es SALIR (detecta si el usuario cierra la ventana)
                    flag_correr = False
                    flag_pantalla_juego = False
                    flag_juego = False
                    flag_pantalla_final = False
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    posicion_click = list(evento.pos)     #print(evento.pos)  me imprime la posicion donde se hizo click
                    posicion_mouse[0] = posicion_click[0] #modifico el left del rect
                    posicion_mouse[1] = posicion_click[1]
                if evento.type == pygame.USEREVENT:
                    if evento.type == timer_segundos:
                        if fin_tiempo == False:
                            segundos = int(segundos) - 1
                            if int(segundos) == 0:
                                fin_tiempo = True
                                flag_pantalla_juego = False
                                flag_juego = False
                                flag_pantalla_final = True

            pantalla.fill(MAGENTA3)    # Pongo un fondo de color en la pantalla principal  
            segundos_texto = fuente_timer.render(str(segundos), True, BLUE)
            pantalla.blit(segundos_texto, POS_TIMER)


            for i in range(filas):
                for j in range(columnas): 
                    posicion_caramelo = [(j+1) *125, (i+1) *125]

                    preparar_armado_lista(tablero, i, clave, j,imagen_caramelo_uno,posicion_caramelo,lista_caramelos)

            for i in range(filas * columnas):
                posicion_caramelo = pygame.Rect(lista_caramelos[1]["Posicion rect"][i][0],lista_caramelos[1]["Posicion rect"][i][1], 10, 10)
                rect_caramelo = imagen_caramelo_uno.get_rect()
                rect_caramelo.x = lista_caramelos[1]["Posicion rect"][i][0] 
                rect_caramelo.y = lista_caramelos[1]["Posicion rect"][i][1] 

                if posicion_mouse.colliderect(rect_caramelo):

                    numero = lista_caramelos[0]["Numero"][i]
                    fila = lista_caramelos[2]["Posicion tablero"][i][0] 
                    columna = lista_caramelos[2]["Posicion tablero"][i][1] 
                    if revisar_filas(tablero, fila, clave, columna, numero):
                        posicion_circulo = [1100, 200]
                        pygame.draw.circle(pantalla, GREEN2, posicion_circulo,80)
                        contador_ganador += 1
                        flag_juego = False
                    else: 
                        print("Perdiste")
                        if segundos > 0:
                            segundos = int(segundos) - 1
                            if int(segundos) == 0:
                                fin_tiempo = True
                                flag_pantalla_juego = False
                                flag_pantalla_final = True
                        contador_perdedor += 1
                        flag_juego = False

            pygame.display.flip()    
    pygame.display.flip()
    
    
    while flag_pantalla_final:
        posicion_mouse = pygame.Rect(0,0,6,6)       #Posicion del mouse vuelve a 0 porque sino mantiene en memoria la anterior
        lista_eventos = pygame.event.get()      # Guardo los eventos de la ventada en una lista
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:      # Si el tipo de evento es SALIR (detecta si el usuario cierra la ventana)
                flag_correr = False                    
                flag_pantalla_final = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                posicion_click = list(evento.pos)     #print(evento.pos)  me imprime la posicion donde se hizo click
                posicion_mouse[0] = posicion_click[0]   #modifico el left del rect
                posicion_mouse[1] = posicion_click[1]
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_BACKSPACE:
                    ingreso = ingreso[0:-1]
                else:
                    ingreso += evento.unicode
        
        puntos = contador_ganador * 10
        if contador_ganador > 0:
            mensaje = f"Usted a sumando {puntos} puntos. Ingrese su nombre:"
        else:
            mensaje = "Usted no a sumado puntos. Ingrese su nombre:"
        
        
        rect_posicion_jugar_de_nuevo = pygame.Rect(posicion_jugar_de_nuevo[0],posicion_jugar_de_nuevo[1], 300, 100)
        if posicion_mouse.colliderect(rect_posicion_jugar_de_nuevo):
            flag_pantalla_final = False
            #flag_primer_pantalla = True
            flag_pantalla_juego = True
            fin_tiempo = False
            segundos = "10"
        
        
        pantalla.fill(PURPLE)    # Pongo un fondo de color en la pantalla principal  
        
        pantalla.blit(imagen_jugar_de_nuevo, posicion_jugar_de_nuevo)

        pygame.draw.rect(pantalla, GREEN, ingreso_rect , 2)             #MUESTRO LA CAJA DE TEXTO PARA QUE INGRESE UN TEXTO
        font_input_surface = font_input.render(ingreso, True, RED2) 
        pantalla.blit(font_input_surface,( ingreso_rect.x + 5 , ingreso_rect.y + 5 ))

        texto = fuente_texto.render(mensaje , True, GREEN1)    #transforma el texto en una imagen
        pantalla.blit(texto,(50,75)) #fundir el texto en la pantalla


        pygame.display.flip()    
    if flag_correr:
        generar_csv("Jugadores_Candy.csv", ingreso, puntos)
    pygame.display.flip()  # Muestro los cambios en la pantalla
pygame.quit()       # Termina el programa

print(contador_ganador)
print(contador_perdedor)
mostrar_lista(tablero)
for i in range(3):
    print(lista_caramelos[i])
