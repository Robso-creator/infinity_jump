import pygame
from sys import exit


def timer_score():
    current_time = pygame.time.get_ticks() - start_time
    score_surf = test_font.render(f'Score: {round((current_time/1000),1)}', False, (64, 64, 64))
    score_rec = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score_rec)


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Infinity Jumps')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = False
start_time = 0

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rec = snail_surf.get_rect(midbottom=(800, 300))

player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rec = player_surf.get_rect(midbottom=(80, 300))
player_stand = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0, 2.5)
player_stand_rec = player_stand.get_rect(center=(400, 200))
player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.KEYDOWN and player_rec.bottom >= 300:
                if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                    player_gravity = -20
            if event.type == pygame.MOUSEBUTTONDOWN and player_rec.bottom >= 300:
                player_gravity = -20
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                game_active = True
                snail_rec.left = 800
                start_time = pygame.time.get_ticks()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                    game_active = True
                    snail_rec.left = 800
                    start_time = pygame.time.get_ticks()

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        timer_score()

        snail_rec.x -= 5
        if snail_rec.right <= 0:
            snail_rec.left = 800
        screen.blit(snail_surf, snail_rec)

        player_gravity += 1
        player_rec.y += player_gravity
        if player_rec.bottom >= 300:
            player_rec.bottom = 300
        screen.blit(player_surf, player_rec)

        # colisão
        if snail_rec.colliderect(player_rec):
            game_active = False
    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rec)
    pygame.display.update()
    clock.tick(60)
