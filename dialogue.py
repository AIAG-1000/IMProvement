'''
This file should be used to hold the large strings of text used to communicate with the player.
It should also have a function that will output text to the screen over all other images

Tasks:
Output text!
See if strings can be handled when too long? <- What if pygame collision can apply to text?
Create a 'text box' that maybe animates into position? <- from 64 to 960, height will be 608 to 704
'''
import pygame
import menus


pygame.init()
# The text chunks should probably be their own class
class Textobject:
    def __init__(self,string,size,font,colour):
        self.string = string
        self.size = size
        self.font = font
        self.colour = colour

    def render_text(block):  # For putting text on the screen. Function needs to be called after other objects are drawn.
        screen
        screen.blit(block,(64 + border_offset, 544 + border_offset))  # 'block' needs to point to a string
        pass

# These are the parameters for text
sample_string = 'Hello I am a test string'
sample_size = 32
sample_font = pygame.font.Font(None,32)
sample_colour = (255,255,255)
sample_text = Textobject(sample_string,sample_size,sample_font,sample_colour)
# This is the format needed to create a renderable object
sample_render = sample_font.render(sample_string,True,(sample_colour))

# Text settings
# Change fonts, sizes and offsets here
border_offset = 16 # Border offset is 16 when paired with a size 32 font. Consider a dictionary to pair ideal offsets to various font sizes.

# Test code - ideas for a solution go here

# Idea 1
# A function that loads selected text into a 'live text' variable which is always being rendered to screen
# Function awaits user input and sets variable to null as it finishes up



