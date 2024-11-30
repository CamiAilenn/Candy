import pygame
from colores import *
from Candy_Crush import *
print(BLUE2)
pygame.init()       #iniciar la pantalla
#declarar constantes
ANCHO_VENTANA = 1200
ALTO_VENTANA = 700

filas = 4
columnas = 7
clave = "Piezas"
inicio_piezas = 1
fin_piezas = 3
bandera_ganador = False
lista_caramelos_uno = []
lista_caramelos_dos = []
lista_caramelos_tres = []
lista_posicion_caramelos_uno = []
lista_posicion_caramelos_dos = []
lista_posicion_caramelos_tres = []

pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))   # Creo la pantalla
pygame.display.set_caption("Candy Dulce Crush")     # Pongo un titulo en la ventana

#IMAGENES
imagen_caramelo_uno = pygame.image.load("caramelo_uno.png")
imagen_caramelo_dos = pygame.image.load("caramelo_dos.jpg")
imagen_caramelo_tres = pygame.image.load("caramelo_tres.png")

imagen_caramelo_uno = pygame.transform.scale(imagen_caramelo_uno,(100,100))
imagen_caramelo_dos = pygame.transform.scale(imagen_caramelo_dos,(100,100))
imagen_caramelo_tres =pygame.transform.scale(imagen_caramelo_tres,(100,100))

tablero = generar_tablero(filas, columnas, clave, inicio_piezas, fin_piezas)
#mostrar_lista(tablero)


posicion_mouse = pygame.Rect(0,0,6,6)





flag_correr = True          # El juego corre mientras la bandera esta True
while flag_correr:

    lista_eventos = pygame.event.get()      # Guardo los eventos de la ventada en una lista
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:      # Si el tipo de evento es SALIR (detecta si el usuario cierra la ventana)
            flag_correr = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            posicion_click = list(evento.pos)     #print(evento.pos)  me imprime la posicion donde se hizo click
            posicion_mouse[0] = posicion_click[0] #modifico el left del rect
            posicion_mouse[1] = posicion_click[1]
      
    

    pantalla.fill(MAGENTA3)    # Pongo un fondo de color en la pantalla principal  

    for i in range(4):
        for j in range(7): 
            posicion_caramelo = [(j+1) *125, (i+1) *125]
            posicion_rect_caramelo = pygame.Rect(posicion_caramelo[0],posicion_caramelo[1],6,6)
            if numero_en_posicion(tablero, i, clave, j) == 1:
                pantalla.blit(imagen_caramelo_uno,posicion_caramelo)
                lista_caramelos_uno.append(posicion_caramelo)
                lista_posicion_caramelos_uno.append([i , j])

            elif numero_en_posicion(tablero, i, clave, j) == 2: 
                pantalla.blit(imagen_caramelo_dos,(posicion_caramelo))
                lista_caramelos_dos.append(posicion_caramelo)
                lista_posicion_caramelos_dos.append([i , j])
                
            else:
                pantalla.blit(imagen_caramelo_tres,(posicion_caramelo))
                lista_caramelos_tres.append(posicion_caramelo)
                lista_posicion_caramelos_tres.append([i , j])
   
    for i in range(len(lista_caramelos_uno)):
        posicion_caramelo_uno = pygame.Rect(lista_caramelos_uno[i][0],lista_caramelos_uno[i][1], 10, 10)
        rect_caramelo_uno = imagen_caramelo_uno.get_rect()
        rect_caramelo_uno.x = lista_caramelos_uno[i][0] 
        rect_caramelo_uno.y = lista_caramelos_uno[i][1] 
        if posicion_mouse.colliderect(rect_caramelo_uno):
            numero = 1
            fila = lista_posicion_caramelos_uno[i][0]
            columna = lista_posicion_caramelos_uno[i][1]
            if revisar_filas(tablero, fila, clave, columna, numero):
                posicion_circulo = [1100, 200]
                pygame.draw.circle(pantalla, GREEN2, posicion_circulo,80)

    for i in range(len(lista_caramelos_dos)):
        posicion_caramelo_dos = pygame.Rect(lista_caramelos_dos[i][0],lista_caramelos_dos[i][1], 10, 10)
        rect_caramelo_dos = imagen_caramelo_dos.get_rect()
        rect_caramelo_dos.x = lista_caramelos_dos[i][0] 
        rect_caramelo_dos.y = lista_caramelos_dos[i][1] 
        if posicion_mouse.colliderect(rect_caramelo_dos):
            numero = 2
            fila = lista_posicion_caramelos_dos[i][0]
            columna = lista_posicion_caramelos_dos[i][1]
            if revisar_filas(tablero, fila, clave, columna, numero):
                posicion_circulo = [1100, 400]
                pygame.draw.circle(pantalla, RED1 ,posicion_circulo,80)
    
    for i in range(len(lista_caramelos_tres)):
        posicion_caramelo_tres = pygame.Rect(lista_caramelos_tres[i][0],lista_caramelos_tres[i][1], 10, 10)
        rect_caramelo_tres = imagen_caramelo_tres.get_rect()
        rect_caramelo_tres.x = lista_caramelos_tres[i][0] 
        rect_caramelo_tres.y = lista_caramelos_tres[i][1] 
        if posicion_mouse.colliderect(rect_caramelo_tres):
            numero  = 3
            fila = lista_posicion_caramelos_tres[i][0]
            columna = lista_posicion_caramelos_tres[i][1]
            if revisar_filas(tablero, fila, clave, columna, numero):
                posicion_circulo = [1100, 600]
                pygame.draw.circle(pantalla, BLUE, posicion_circulo,80)
    

    '''
    if evento.type == pygame.MOUSEBUTTONDOWN:
        #ganador(revisar_filas(tablero, fila, clave, columna, numero))
        if revisar_filas(tablero, fila, clave, columna, numero):
            pygame.draw.rect(pantalla, COLOR_BLANCO,(500,500,600,1000))
            pygame.display.flip()'''



    pygame.display.flip()         # Muestro los cambios en la pantalla

pygame.quit()       # Termina el programa
