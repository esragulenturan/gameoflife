import pygame

class Cell():
    # constructor method get screen and x position and y position and scale of each cell and distance between cell
    def __init__(self,surface,x_pos,y_pos,scale,offset):
        self.surface = surface
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.scale = scale
        self.offset = offset
    # getter for scale
    @property
    def scale(self):
        return self._scale
    # setter for scale (scale must be greater than 10)
    @scale.setter
    def scale(self, scale):
        if scale<10:
            raise ValueError("don't enter scale below ten")
        self._scale = scale

    # getter for offset
    @property
    def offset(self):
        return self._offset
    # setter for offset (offset must be beetween 0 to 3)
    @offset.setter
    def offset(self, offset):
        if offset<0 and offset>3:
            raise ValueError("don't enter offset negative or greater than 3")
        self._offset = offset
        
    # draw rectangle with class properties
    def draw_cell(self,color):
        pygame.draw.rect(self.surface, color, [self.x_pos, self.y_pos, self.scale-self.offset, self.scale-self.offset])
