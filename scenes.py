'''
This file should collate information for each scene.
Each scene needs to contain:
-Background image (most important, just needs to be a .png)
-Player position (Not yet clear if this should be part of this class)
-Interactable objects (Ideally should just be a list of objects) Note: This may have to be a seperate class actually
-Where collision is (Could easily just be a list of defined rectangles to load in)
-
'''
import pygame


### HOW TO USE THE SCENE CLASS:
### IMAGE OBJECT SHOULD BE THE FILE PATH FOR THE IMAGE
### COLLIDE OBJECT CAN BE A LIST OF RECTANGLES
import items


class Scene:
    def __init__(self,image,collide,items):
        self.image = pygame.image.load(image).convert() # When the class is invoked, this should load the image and convert the alphas
        self.collide = collide
        self.items = items


# Collision
# Rectangle lists stored here
# Boundary rectangles - This provides a 32px border on the edges of the window
left_boundary = pygame.Rect(0, 0, 96, 768)
right_boundary = pygame.Rect(928, 0, 96, 768)
top_boundary = pygame.Rect(0, 0, 1024, 96)
bottom_boundary = pygame.Rect(0, 672, 1024, 96)
lrtb_list = [left_boundary, right_boundary, top_boundary,
             bottom_boundary]

# Scenes
# Create scenes here

# INTRO ROOM
# This is the first room, and should be loaded after New Game is selected
blue_imp = (608,320) # Consolidating placement coordinates as a tuple, see how this works
intro_items = [items.blue_imp]
intro_room_1 = Scene('graphics/intro_room.png',lrtb_list,intro_items)

# Collision
# Rectangle lists stored here


