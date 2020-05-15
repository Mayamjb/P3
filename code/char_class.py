class Character():

    def __init__(self, x, y, img, trame):
        self.x = x
        self.y = y
        self.img = img
        self.trame = trame
        # list to tcheck if all objects has been taken
        self.obj_taken = []

    def __check_collision(self, x, y):
        """ Fuction that checks collisions.
        Checks collisions with walls to allow movements.
        Checks collisions with objects to get them.
        Checks collisions with guardian to finish game.
        """
        # this character "#" represent walls in the list
        if self.trame[y][x] != "#":
            # Check objects on the way
            if self.trame[y][x] in ["K", "L", "H"]:
                self.obj_taken.append(self.trame[y][x])
                # deleting obj image when taken."." represent free way
                self.trame[y][x] = "."
            if self.trame[y][x] == "G":
                # Check if all objects are taken
                if len(self.obj_taken) == 3:
                    # erase guardian when asleeped
                    self.trame[y][x] = "."
            return True
        else:
            return False

    def go(self, add_x, add_y):
        """Fuction that define a movement in the maze_list.
            It takes the incrementation needed for each coordinate
            to allow movement.
        """
        if self._Character__check_collision(self.x + add_x, self.y + add_y):
            self.x += add_x
            self.y += add_y
