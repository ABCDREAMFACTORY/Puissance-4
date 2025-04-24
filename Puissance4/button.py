import pygame
class Button:
    def __init__(self,surface,x,y,width,height,color,text = None,text_color = (255,255,255),taille = 25):
        self.rect = pygame.Rect(x,y,width,height)
        self.rect.center = (x + width / 2, y + height / 2)
        self.color = color
        self.taille_text = pygame.font.Font(pygame.font.get_default_font(), taille)
        self.text = text
        self.text_render = self.taille_text.render(text, 1,text_color)
        self.surface = surface
    def draw(self):
        pygame.draw.rect(self.surface,self.color,self.rect)
        self.surface.blit(self.text_render,self.text_render.get_rect(center = self.rect.center))
    def is_clicked(self,pos):
        if self.rect.collidepoint(pos):
            return True
        return False
    def change_color(self,color):
        self.color = color
    def action(self):
        return self.text