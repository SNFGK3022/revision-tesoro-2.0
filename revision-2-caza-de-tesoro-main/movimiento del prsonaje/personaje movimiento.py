import pygame
import sys
from random import randint

# Inicialización de Pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 580
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Movimiento Personaje")

# Fuente y reloj
font = pygame.font.SysFont(None, 36)
clock = pygame.time.Clock()

# Carga de imágenes
fondo = pygame.image.load("fondo.jpg")
personaje_img = pygame.image.load("p.png")
personaje_img = pygame.transform.scale(personaje_img, (60, 80))

personaje2_img = pygame.image.load("p2.png")
personaje2_img = pygame.transform.scale(personaje2_img, (60, 80))

bolsa_img = pygame.image.load("bolsa.png")
bolsa_img = pygame.transform.scale(bolsa_img, (60, 60))

# Puntuación de los jugadores
puntos1 = 0
puntos2 = 0

# Posiciones iniciales
bolsa = bolsa_img.get_rect(topleft=(WIDTH // 2, HEIGHT - 60))
jugador1 = personaje_img.get_rect(topleft=(WIDTH // 4, HEIGHT - 60))
jugador2 = personaje2_img.get_rect(topleft=(3 * WIDTH // 4, HEIGHT - 60))

# Velocidad de los jugadores
jugador1_speed = 5
jugador2_speed = 5

# Función para mostrar texto en pantalla
def draw_text(text, x, y, color=(225, 225, 225)):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

# Bucle principal del juego
while True:
    screen.blit(fondo, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Control de teclas
    keys = pygame.key.get_pressed()

    # Movimiento jugador 1 (WASD)
    if keys[pygame.K_a]: jugador1.x -= jugador1_speed
    if keys[pygame.K_d]: jugador1.x += jugador1_speed
    if keys[pygame.K_w]: jugador1.y -= jugador1_speed
    if keys[pygame.K_s]: jugador1.y += jugador1_speed

    # Movimiento jugador 2 (flechas)
    if keys[pygame.K_LEFT]: jugador2.x -= jugador2_speed
    if keys[pygame.K_RIGHT]: jugador2.x += jugador2_speed
    if keys[pygame.K_UP]: jugador2.y -= jugador2_speed
    if keys[pygame.K_DOWN]: jugador2.y += jugador2_speed

    # Colisiones con la bolsa
    if jugador1.colliderect(bolsa):
        puntos1 += 1
        bolsa.topleft = (randint(0, WIDTH - bolsa.width), randint(0, HEIGHT - bolsa.height))

    if jugador2.colliderect(bolsa):
        puntos2 += 1
        bolsa.topleft = (randint(0, WIDTH - bolsa.width), randint(0, HEIGHT - bolsa.height))

    # Mantener jugadores dentro de la pantalla
    jugador1.clamp_ip(screen.get_rect())
    jugador2.clamp_ip(screen.get_rect())

    # Dibujo en pantalla
    screen.blit(bolsa_img, bolsa.topleft)
    screen.blit(personaje_img, jugador1.topleft)
    screen.blit(personaje2_img, jugador2.topleft)
    draw_text(f"Player 1: {puntos1}", 10, 10)
    draw_text(f"Player 2: {puntos2}", 600, 10)

    # Actualizar pantalla
    pygame.display.flip()
    clock.tick(60)
