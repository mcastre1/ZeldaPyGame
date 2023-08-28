import pygame
from entity import Entity

class Enemy(Entity):
    def __init__(self, monster_name, pos, groups):
        super().__init__(groups)

        # general setup
        self.sprite_type = 'enemy'

        # graphics setup
        self.image = pygame.Surface((64, 64))
        self.rect = self.image.get_rect(topleft = pos)