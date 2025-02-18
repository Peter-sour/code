import pygame
import random

# Inisialisasi pygame
pygame.init()

# Ukuran layar
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game Tembak-Tembakan Pesawat")

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Kecepatan pesawat
player_speed = 5
bullet_speed = 7
enemy_speed = 2

# Membuat pesawat player
player_width = 50
player_height = 40
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10
player = pygame.Rect(player_x, player_y, player_width, player_height)

# List untuk peluru dan musuh
bullets = []
enemies = []

# Fungsi untuk menggambar pesawat player
def draw_player():
    pygame.draw.rect(screen, WHITE, player)

# Fungsi untuk menggambar peluru
def draw_bullets():
    for bullet in bullets:
        pygame.draw.rect(screen, RED, bullet)

# Fungsi untuk menggambar musuh
def draw_enemies():
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

# Fungsi untuk menggerakkan pesawat player
def move_player(keys):
    global player_x
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_speed

    player.x = player_x

# Fungsi untuk menembak peluru
def shoot_bullet():
    bullet = pygame.Rect(player.x + player_width // 2 - 5, player.y, 10, 20)
    bullets.append(bullet)

# Fungsi untuk menggerakkan peluru
def move_bullets():
    global bullets
    for bullet in bullets[:]:
        bullet.y -= bullet_speed
        if bullet.y < 0:
            bullets.remove(bullet)

# Fungsi untuk membuat musuh
def create_enemy():
    enemy_x = random.randint(0, screen_width - 50)
    enemy_y = random.randint(-150, -50)
    enemy = pygame.Rect(enemy_x, enemy_y, 50, 40)
    enemies.append(enemy)

# Fungsi untuk menggerakkan musuh
def move_enemies():
    global enemies
    for enemy in enemies[:]:
        enemy.y += enemy_speed
        if enemy.y > screen_height:
            enemies.remove(enemy)

# Fungsi untuk cek tabrakan peluru dengan musuh
def check_collision():
    global bullets, enemies
    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)

# Fungsi utama game
def game_loop():
    global player_x, player_y, bullets, enemies

    clock = pygame.time.Clock()

    # Menambah musuh pada interval tertentu
    enemy_event = pygame.USEREVENT + 1
    pygame.time.set_timer(enemy_event, 2000)

    running = True
    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    shoot_bullet()
            if event.type == enemy_event:
                create_enemy()

        keys = pygame.key.get_pressed()
        move_player(keys)
        move_bullets()
        move_enemies()
        check_collision()

        draw_player()
        draw_bullets()
        draw_enemies()

        pygame.display.update()

        clock.tick(60)  # 60 FPS

    pygame.quit()

# Jalankan game
game_loop()
