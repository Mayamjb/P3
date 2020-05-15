from maze_class import Mapp
import pygame


def main():
    pygame.init()
    mapp = Mapp("the_map_2.txt")
    running = True
    while running:

        # Display player at initial position, without any movement
        mapp.display_character()
        mapp.mapp_display()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                mapp.move(event.key)
        pygame.display.flip()
        pygame.display.update()


if __name__ == "__main__":
    main()
