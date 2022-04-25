import pygame
import numpy as np
import random
from Cell import Cell

class ConwayGame:
    # constructor get width,height,scale and offset each cell
    def __init__(self, width, height, scale, offset):
        self.scale = scale
        # calculate number of row and columns
        self.columns = int(height/scale)
        self.rows = int(width/scale)
        # tuple for size screen
        self.size = (self.rows, self.columns)
        # create matrix with this size
        self.grid_board = np.ndarray(shape=(self.size))
        self.offset = offset

    # fill matrix
    def fill_array_board(self, reset=0):
        for x in range(self.rows):
            for y in range(self.columns):
                # if receive 1 for reset parameter fill matrix with zero else fill matrix with  0 or 1 randomly
                if reset == 1:
                    self.grid_board[x][y] = 0
                else:
                    self.grid_board[x][y] = random.randint(0,1)
    # draw board based on matrix
    def draw_board(self,off_color,on_color,surface):
        for x in range(self.rows):
            for y in range(self.columns):
                # calculate cell coordinate
                y_pos = y * self.scale
                x_pos = x * self.scale
                # create an object of Cell class with this coordinate and scale
                rect = Cell(surface,x_pos,y_pos,self.scale,self.offset)
                # if this index (x,y) of matrix is 1, call draw_cell from cell class and and draw a live cell else draw dead cell
                if self.grid_board[x][y] == 1:
                    rect.draw_cell(on_color)
                else:
                    rect.draw_cell(off_color)
    # run with conway rule
    def run_conway(self, off_color, on_color, surface, pause):
        # draw board
        self.draw_board(off_color,on_color,surface)
        # reset matrix
        next = np.ndarray(shape=(self.size))
        # if game not pause
        if pause == False:
            for x in range(self.rows):
                for y in range(self.columns):
                    # status of cell,0(dead),1(live)
                    state = self.grid_board[x][y]
                    # count cell neighbours 
                    neighbours = self.number_neighbours( x, y)
                    # conway rule
                    # next is new board with applay conway rule
                    if state == 0 and neighbours == 3:
                        next[x][y] = 1
                    elif state == 1 and (neighbours < 2 or neighbours > 3):
                        next[x][y] = 0
                    else:
                        next[x][y] = state
            # applay new board
            self.grid_board = next

    # the cell which is clicked by user 
    def HandleMouse(self, x, y):
        # calculate rectangle position
        _x = x//self.scale
        _y = y//self.scale
        # if this cell exist
        if self.grid_board[_x][_y] != None and self.grid_board[_x][_y] == 0:
            # keep a cell alive
            self.grid_board[_x][_y] = 1
        elif self.grid_board[_x][_y] != None and self.grid_board[_x][_y] == 1:
            # kill this cell
            self.grid_board[_x][_y] = 0

        
    # count cell neighbors
    def number_neighbours(self, x, y):
        # counter neighbours number
        c = 0
        for n in range(-1, 2):
            for m in range(-1, 2):
                # calculate coordinate of top,left right, bottom neighbors in each loop round
                x_edge = (x+n+self.rows) % self.rows
                y_edge = (y+m+self.columns) % self.columns
                # neighbour status sum with c(this number 0 or 1)
                c += self.grid_board[x_edge][y_edge]

        c -= self.grid_board[x][y]
        return c
