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
    if text_rec.y > 544: # 544 is as high as I want the textbox to go
        pygame.draw.rect(Main.screen, (153, 50, 204), text_rec) # Drawing box to the main screen, then declaring RGB value and coordinates
        text_rec.y -= 1 # Increment box height
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
            pygame.event.wait()
        else:
            return
            while text_rec.y < 768:
                text_rec.y += 1
                pygame.draw.rect(Main.screen, (153, 50, 204), text_rec)
                pygame.display.update(text_rec)
            return # Back to the loop