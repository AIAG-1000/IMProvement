'''
This file is to store functions, to keep main clean
'''
import pygame
import dialogue
import main
from dialogue import Textobject
from main import Main

def textbox(): # This function should animate a frame to set text inside, call render_text(), await user input, and move offscreen
    # To solve issue with drawing rectangle over scene, make a scene() function and invoke it here?
    text_rec = dialogue.Textobject.text_rec # Initial coordinates for the box
    while text_rec.y > 544: # 544 is as high as I want the textbox to go
        pygame.draw.rect(Main.screen, (153, 50, 204), text_rec) # Drawing box to the main screen, then declaring RGB value and coordinates
        text_rec.y -= 1 # Increment box height
        pygame.time.wait(1) # To make the animation a little less jarring, waiting for one millisecond
        pygame.display.update(text_rec)
        print(text_rec.y) # Debug feature, delete later
        if text_rec.y == 768: # This shouldn't be called anymore, written to catch a bug
            return

    if text_rec.y <= 544: # There is potential for the box to move too high, this condition prevents bugs
        text_rec.y = 544
        pygame.draw.rect(Main.screen, (153, 50, 204), text_rec)
        print("YEHA") # Debug line, delete
        dialogue.Textobject.render_text(dialogue.sample_render) # Calling the text delivery function
        pygame.display.update(text_rec)

        while pygame.key.get_pressed()[pygame.K_SPACE] == False:
            pygame.event.wait() # Nothing happens until space is pressed, not an elegant way of doing it
        else:

            if pygame.key.get_pressed()[pygame.K_SPACE] == True: # This might be redundant
                while text_rec.y < 768:
                    text_rec.y += 1 # Same as above, but decreasing box height and redrawing it
                    pygame.time.wait(1)
                    pygame.draw.rect(Main.screen, (153, 50, 204), text_rec)
                    pygame.display.update(text_rec)
                    if text_rec.y == 768: # Once box is offscreen, we break the loop
                        break

def scenecall(scene): # This function runs once per frame, and will draw the background and any items to the screen
    # To work, this function needs to pass an item from the scenes file as an argument (eg. scenes.intro_room_1)
    Main.screen.blit(scene.image,(0,0)) # Taking the function argument, and drawing its image object to screen. Coordinates must be zero so this is hardcoded.

    for x in scene.items: # Multiple items can be loaded, so for every item in the list:
        Main.screen.blit(x.image,x.position) # blit the item image at the item position
