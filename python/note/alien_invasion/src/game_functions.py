import sys
import pygame

from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

def check_events(ai_settings, screen, ship, bullets):
    ''' response key and mouse event'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                #right move
                ship.moving_right = True

            if event.key == pygame.K_LEFT:
                #left move
                ship.moving_left = True

            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                #right move
                ship.moving_right = False

            if event.key == pygame.K_LEFT:
                #left move
                ship.moving_left = False
                
def update_screen(ai_settings, screen, ship, aliens, bullets):
    #set bg color
    screen.fill(ai_settings.bg_color)
    

    #draw all bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    #set draw screen visible
    pygame.display.flip()

def update_bullets(bullets):
    bullets.update()

    #delect dispear bullet
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def create_fleet(ai_settings, screen, aliens):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))

    for alien_number in range(number_aliens_x):
        alien = Alien(ai_settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)

