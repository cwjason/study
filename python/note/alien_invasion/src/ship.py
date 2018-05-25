import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        #init ship pos in screen
        self.screen = screen
        self.ai_settings = ai_settings

        #load ship pic and get it outsize
        self.image = pygame.image.load("../res/rocket-3309711__340.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #set every ship in screen center
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False
        
        self.center = float(self.rect.centerx)
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factgor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factgor

        self.rect.centerx = self.center
    def blitme(self):
        ''' draw ship on specify place '''
        self.screen.blit(self.image, self.rect)