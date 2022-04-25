import pygame
import time
import random
import numpy as np
import os
import grid
from tkinter import *

#resolution
width, height = 800,500
size = (width, height)
# create object from ConwayGame class
Grid = grid.ConwayGame(width,height,10, 1)
# pause and run flage
pause = False
run = True
def initial_game(btn):
    # access to global variable
    global run,pause
    # initional pygame
    pygame.init()
    # set title for window
    pygame.display.set_caption("GAME OF LIFE")
    # create pygame screen
    screen = pygame.display.set_mode(size)
    # set time for update screen
    clock = pygame.time.Clock()
    fps = 30
    # call fill_array_board method from Grid class and send 1 for it for play manually
    if btn=="manual":
        Grid.fill_array_board(1)
    # call fill_array_board method from Grid class for play randomly
    if btn=="random":
        Grid.fill_array_board()
    # repeat while run is true
    while run:
        # set speed of update screen
        clock.tick(fps)
        # check events (click or press a key)
        for event in pygame.event.get():
            # if click quit button
            if event.type == pygame.QUIT:
                # change run flage to false
                run = False
            # check key is pressed
            if event.type == pygame.KEYUP:
                # if escape key is pressed exit game
                if event.key == pygame.K_ESCAPE:
                    run = False
                # if space key is pressed pause game
                if event.key == pygame.K_SPACE:
                    pause = not pause
        # call draw_board method from Grid class
        Grid.draw_board(off_color="white", on_color="blue", surface=screen)
        if btn == "initial":
            # call run_conway method from Grid class    
            Grid.run_conway(off_color="white", on_color="blue", surface=screen, pause=pause)
        # get mous position on the screen
        if pygame.mouse.get_pressed()[0]:
            mouseX, mouseY = pygame.mouse.get_pos()
            # call HandleMouse method and send mous position for it
            Grid.HandleMouse(mouseX, mouseY)

        # update pygame screen
        pygame.display.update()
        # update tkinter screen
        app.update()
# create game panel  with tkinter
app=Tk()
random_btn=Button(app, text="Random Board",command=lambda:initial_game("random"))
random_btn.grid(row=0, column = 0)
start_btn=Button(app, text="Manual",command=lambda:initial_game("manual") )
start_btn.grid(row=0, column = 1)
start_btn=Button(app, text="Initial",command=lambda:initial_game("initial") )
start_btn.grid(row=0, column = 2)
start_btn=Button(app, text="Reset",command=lambda:initial_game("manual") )
start_btn.grid(row=0, column = 3)

app.mainloop()

