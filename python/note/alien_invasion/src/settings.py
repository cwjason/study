class Settings():
    ''' save alien_invasion all setting '''

    def __init__(self):
        #init game setting
        self.screen_width = 1136
        self.screen_height = 640
        self.bg_color = (230, 230, 230)
        self.ship_speed_factgor = 1.5
        self.bullet_width = 30
        self.bullet_height = 30
        self.bullet_color = 60, 60, 60
        self.bullet_speed_factor = 1
        self.bullets_allowed = 3