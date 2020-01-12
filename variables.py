#!/bin/python3

#Game variables that can be changed!

#game background colour.
BACKGROUNDCOLOUR = 'lightblue'

#map variables.
MAXTILES  = 64
MAPWIDTH  = 20
MAPHEIGHT = 20

#variables representing the different resources.
DIRT    = 0
GRASS   = 1
WATER   = 2
BRICK   = 3
WOOD    = 4
SAND    = 5

#a list of all game resources.
resources = [DIRT,GRASS,WATER,BRICK,WOOD]

#the names of the resources.
names = {
  DIRT    : 'dirt',
  GRASS   : 'grass',
  WATER   : 'water',
  BRICK   : 'brick',
  WOOD    : 'wood',
  SAND    : 'sand'
}

#a dictionary linking resources to images.
textures = {
  DIRT    : 'dirt.gif',
  GRASS   : 'grass.gif',
  WATER   : 'water.gif',
  BRICK   : 'brick.gif',
  WOOD    : 'wood.gif',
  SAND    : 'sand.gif'
}

#the number of each resource the player has.
inventory = {
  DIRT    : 0,
  GRASS   : 0,
  WATER   : 0,
  BRICK   : 0,
  WOOD    : 0,
  SAND    : 0
}

#the player image.
playerImg = 'player.gif'

#the player position.
playerX = 0
playerY = 0

#rules to make new resources.
crafting = {
  BRICK    : { WATER : 1, DIRT : 2 }
}

#keys for placing resources.
placekeys = {
  DIRT  : '1',
  GRASS : '2',
  WATER : '3',
  BRICK : '4',
  WOOD  : '5',
  SAND  : '6'
}

#keys for crafting tiles.
craftkeys = {
  BRICK : 'r'
}

#game instructions that are displayed.
instructions =  [
  'Instructions:',
  'Use WASD to move'
]
