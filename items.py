'''
This file should contain item information.
In this context, item refers to objects drawn over the background image.
Items may have collision and may be movable.
Item objects required:
- Image
- Position
- Collision
'''

import pygame

### HOW TO USE THE ITEM CLASS:
### IMAGE OBJECT SHOULD BE THE FILE PATH FOR THE IMAGE
### POSITION WILL BE A TUPLE FOR X-Y COORDINATES

class Item:
    def __init__(self,image,position): # Consider adding collision later
        self.image = pygame.image.load(image).convert_alpha() # Loads the image and converts the alphas
        self.position = position

# Items
# Make items here

#Blue Imp
# First item, testing class with this wee guy
blue_imp_xy = (608,320)
blue_imp = Item('graphics/playerimp2.png',blue_imp_xy)