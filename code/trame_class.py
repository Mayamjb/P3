import random


class Trame:

    def __init__(self, txt_file):
        self.txt_file = txt_file
        self.trame = self._Trame__run("H", "K", "L")

    def __run(self, obj1, obj2, obj3):
        """ Fuction that places the 3 objects in the list.
            The three parameters represent the objects to place
            The function returns the list with three objects placed
        """
        var1 = self._Trame__get_map_from_txt(self.txt_file)
        var2 = self._Trame__get_mapp_with_objects(obj1, obj2, obj3, var1)
        return var2

    def __get_map_from_txt(self, map_txt):
        """function to get the mapp fron a txt file.
            The parameter map_txt represent a file.txt where the map is located
            The function returns the file.txt content in a list.
        """
        mappp = open(map_txt, "r")  # openning the mapp ti "r" just read it
        data = mappp .readlines()  # reading line in the file
        mappp .close()
        listttt = []
        for line in data:
            # each line is a list, each character is separted with " ",
            listttt.append(line.strip().split(" "))
        return listttt

    def __place_object_randomly(self, obj, trame):
        """ Function that place an obj
            at a random place in the maze list"""
        # taking 2 random numbers from 0 to 14 because game is in 15x15
        u = random.randint(0, 14)
        v = random.randint(0, 14)
        counter = 0
        while counter < 1:
            # place objects only on free way execpt way out after guardian
            if (trame[u][v] == ".") and ((v, u) != (8, 14)):
                trame[u][v] = obj
                counter += 1
            # means that randint are on a wall or character, get 2 new randint
            else:
                u = random.randint(0, 9)
                v = random.randint(0, 12)
        return trame

    def __get_mapp_with_objects(self, obj1, obj2, obj3, trame):
        # placing objects on the map one by one. returning last map
        self._Trame__place_object_randomly(obj1, trame)
        self._Trame__place_object_randomly(obj2, trame)
        mapp3 = self._Trame__place_object_randomly(obj3, trame)
        return mapp3
