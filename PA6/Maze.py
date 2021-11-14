#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This module implements a Data Structure to store important information
    about a specific maze.
"""
__author__ = ["Amittai", "Alberto Quattrini Li"]
__copyright__ = "Copyright 2021"
__credits__ = ["Amittai", "Alberto Quattrini Li"]
__email__ = "Amittai.J.Wekesa.24@dartmouth.edu"
__github__ = "@siavava"

from time import sleep

# Maze.py
#  original version by db, Fall 2017
#  Feel free to modify as desired.

# Maze objects are for loading and displaying mazes, and doing collision checks.
#  They are not a good object to use to represent the state of a robot mazeworld search
#  problem, since the locations of the walls are fixed and not part of the state;
#  you should do something else to represent the state. However, each Mazeworldproblem
#  might make use of a (single) maze object, modifying it as needed
#  in the process of checking for legal moves.

# Test code at the bottom of this file shows how to load in and display
#  a few maze data files (e.g., "maze1.maz", which you should find in
#  this directory.)

#  the order in a tuple is (x, y) starting with zero at the bottom left

# Maze file format:
#    # is a wall
#    . is a floor
# the command \robot x y adds a robot at a location. The first robot added
# has index 0, and so forth.


class Maze:

    # internal structure:
    #   self.walls: set of tuples with wall locations
    #   self.width: number of columns
    #   self.height: number of rows

    def __init__(self, mazefilename):
        """
            Initializes a maze from a file.
        """
        
        # initialzie array of map values.
        self.map = []
        self.colors = set()
        self.color_count = 0
        
        # open maze file. exits if failed.
        with open(mazefilename) as f:
            
            # for each line in the file,
            for line in f:
                
                # remove trailing / beginning spaces
                line = line.strip().lower()
                
                # if blank, skip
                # otherwise, save the line
                # and index unique colors in the line.
                if len(line) != 0:
                    self.map.append(line)
                    self.colors |= set(line)
                    
            self.colors.discard("#")
            self.color_count = len(self.colors) 
            f.close()

        # get the width and height of the maze
        self.width = len(self.map[0])
        self.height = len(self.map)
        
        
        
        
    def __iter__(self):
        """
            Returns an iterator over the map. 
            NOTE: this is a list of lists, so it returns lists.
            Map structure:
            
                a total of self.height lists each with self.width elements. 
            ```
                [
                    [...],
                    [...],
                    .
                    .
                    .
                    [...]
                ]
            ```
        """
        return iter(self.map)

    def index(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return y * self.width + x
        return None
    
    def de_index(self, index):
        # print(f"\n\nwidth = %d, height = %d" % (self.width, self.height))
        # print(f"index = {index}")
        # print(f"computed values = {(index % self.width, index // self.width)}")
        return (index % self.width, index // self.width)


    # returns True if the location is a floor
    def get_char(self, x, y):
        """
            Get the character at given position in the Maze.
        """
        
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.map[y][x]
        
        return None
    
    def count_positions(self):
        """
            Get the total number of possible robot positions in the Maze.
        """
        
        positions = 0
        for x in range(self.width):
            for y in range(self.height):
                if self.get_char(x, y) != "#":
                    positions += 1
                
        return positions

    def __str__(self):
        # return a string representation of the maze
        # that looks like a grid
        
        s = ""
        for line in self.map:
            s += line + "\n"

        return s


# A unit test for the Maze class.
def unit_test():
    test_maze1 = Maze("mazes/maze1.maz")
    print(test_maze1)

    test_maze2 = Maze("mazes/maze2.maz")
    print(test_maze2)

    test_maze3 = Maze("mazes/maze3.maz")
    print(test_maze3)

    print(test_maze3)
    print(test_maze3.robotloc)

    print(test_maze3.is_floor(2, 3))
    print(test_maze3.is_floor(-1, 3))
    print(test_maze3.is_floor(1, 0))

if __name__ == "__main__":
    unit_test()