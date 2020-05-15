from char_class import Character
from trame_class import Trame
from data import *
import pygame
import sys


class Mapp(Character):

    def __init__(self, map_txt):
        self.screen = pygame.display.set_mode((450, 650))  # Creating game win
        # instanting Trame
        self.maze_mapp = Trame(map_txt)
        # instanting Player as macgyver
        self.macgyver = Character(1, 1, playerImg, self.maze_mapp.trame)
        # Creating player's coordinates for game window
        self.x_screen = self.macgyver.x + 30
        self.y_screen = self.macgyver.y + 30

    def mapp_display(self):
        """ Function that displays all the items
            that are present on the game window.
        """
        # going through list + getting indexes
        for id, line in enumerate(self.maze_mapp.trame):
            for index, char in enumerate(line):
                if char == "#":
                    # display walls
                    self.screen.blit(bounderiesImg, (index * 30, id * 30))
                elif char == "G":
                    # display guadian
                    self.screen.blit(guardianImg, (index * 30, id * 30))
                # display objects
                elif char == "H":
                    self.screen.blit(needleImg, (index * 30, id * 30))
                elif char == "K":
                    self.screen.blit(etherImg, (index * 30, id * 30))
                elif char == "L":
                    self.screen.blit(tubeImg, (index * 30, id * 30))

    def display_character(self):
        """Function displaying the player's image."""
        self.screen.blit(self.macgyver.img, (self.x_screen, self.y_screen))

    def __movement_definition(self, key):
        """ Fuction that define the player movements
            Using pygame event to get informations from the keyboard.
        """
        # get keybord event
        if key == pygame.K_DOWN:
            self.macgyver.go(0, 1)
        if key == pygame.K_UP:
            self.macgyver.go(0, -1)
        if key == pygame.K_LEFT:
            self.macgyver.go(-1, 0)
        if key == pygame.K_RIGHT:
            self.macgyver.go(1, 0)
        # End game condition
        if (len(self.macgyver.obj_taken) == 3):
            syringeImg_unlocked = pygame.image.load("syringe_unlocked.png")
            self.screen.blit(syringeImg_unlocked, (0, 480))
            self.screen.blit(syringeImg, (357, 480))
            pygame.display.flip()
        # (8, 14) is the outdoor coordinates of the maze
        if ((self.macgyver.x, self.macgyver.y) == (8, 14)):
            if (len(self.macgyver.obj_taken) == 3):
                self.screen.blit(winning, (200, 580))
                pygame.display.flip()
                pygame.time.delay(1500)
                sys.exit()
            else:
                self.screen.blit(loosingImg, (50, 480))
                pygame.display.flip()
                pygame.time.delay(1500)
                sys.exit()

    def move(self, event_key):
        """ Function that run a movement.
            Create a black rectangle to hide player's previous movement.
            Takes a pygame event as a parameter to detect keyboard entries.
        """
        # creating a black rectangle to hide player movement
        self._Mapp__create_rectangle((30, 30))
        # actionning player move
        self._Mapp__movement_definition(event_key)
        # converting list coordinate to pixels
        self.x_screen = self.macgyver.x * 30
        self.y_screen = self.macgyver.y * 30
        # blit player at new position on the game windows in pixels
        self.screen.blit(self.macgyver.img, (self.x_screen, self.y_screen))

    def __create_rectangle(self, size):
        """ Function that create a rectangle
            to hide player's previous position.
            Take the size of the rectangle as a parameter.
            Returns a rectangle.
        """
        # cerating a surface
        surface_filled = pygame.Surface(size)
        # making it a rectangle
        rect = surface_filled.get_rect()
        rect.topleft = (self.x_screen, self.y_screen)
        rectangle = self.screen.blit(surface_filled, rect)
        return rectangle
