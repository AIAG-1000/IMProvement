"""
Currently working on:
A function to handle player movement -x
Collision works, currently have to scale it up
A menu system!  Using a class to handle menus -x (more or less complete)
Dialogue system? - Textbox complete-ish
Consider externalising functions? - In progress, major hurdle complete
A scene function is necessary -
"""

#  importing pygame to do most things
#  importing exit to prevent crashes when closing game
#  importing time because I keep wasting it
import pygame
from sys import exit
import time



# Main class
# Migrating everything into Main that won't be within MainLoop, WIP
class Main:
    winwidth = 1024
    winheight = 768
    screen = pygame.display.set_mode((winwidth, winheight))
    testplayer = pygame.image.load('graphics/playerimp.png').convert_alpha()  # The wee fella




    def __init__(self): # This class should load everything that needs to be loaded, then call MainLoop
        self.caption = pygame.display.set_caption('IMProvement')
        self.icon = pygame.display.set_icon(Main.testplayer)
        self.MainLoop()

    def MainLoop(self):
        global text_rec_y, text_rec
        # MAIN LOOP
        # Core logic to maintain display and await input from user

        while True:  # This is to ensure loop always runs
            for event in pygame.event.get():  # For each event in the event queue:
                if event.type == pygame.QUIT:  # If the eventtype is .QUIT:
                    pygame.quit()  # Tears down the display
                    exit()  # Properly exits the Python script
                if event.type == pygame.MOUSEBUTTONDOWN:  # This is a debug feature for eyeballing where exactly things are
                    print(pygame.mouse.get_pos())

                # Main Menu
                if start_game == False:
                    Main.screen.blit(menu_surface, (0, 0))
                    Main.screen.blit(menu_title, (32, 32))
                    Main.screen.blit(menu_new_game, (832, 608))
                    Main.screen.blit(menu_load_game, (832, 672 - menus.menu_load.offset))
                    Main.screen.blit(menu_quit_game, (832, 736 - menus.menu_quit.offset))
                    Main.screen.blit(gem_orange, (800, 604 + menu_offset))
                    if event.type == pygame.KEYDOWN:
                        menu_input(event.key)

                    if event.type == pygame.MOUSEBUTTONDOWN:  # This is a debug feature, delete this later
                        if pygame.mouse.get_pressed(num_buttons=3) == (0,0,1): # This translates to "right click only"
                            while dialogue.Textobject.text_rec.y > 544: # Repeatedly running this function as long as the box is not in position
                                functions.textbox()
                            if dialogue.Textobject.text_rec.y == 544: # Box is now in ideal position, function should change behaviour
                                functions.textbox()
                            break

                            #else:
                                #print("ONE STEP CLOSER TO THE EDGE")
                               # break
                            #dialogue.Textobject.render_text(dialogue.sample_render)
                            # Note to future me: Draw the animations, then just add rectangle to the main loop
                            # THEN draw text over it



            if start_game == True:
                # Background
                Main.screen.blit(testsurface, (0, 0))
                rec1.topleft = 240, 240  # Top-left corner should be at given coordinates
                pygame.draw.rect(Main.screen, 'red', rec1)  # Draw rec1 to the 'screen', make it 'red'
                pygame.draw.rect(Main.screen, 'green', rec2)
                pygame.draw.rect(Main.screen, 'silver', rec3)

                # Player

                # Player movement
                if event.type == pygame.KEYDOWN:
                    player_input(event.key)

                # Collision
                # if testplayer_frame.colliderect(rec1): print("JINKIES")

                testplayer_frame = Main.testplayer.get_rect(center=(player_x, player_y))
                Main.screen.blit(Main.testplayer, (testplayer_frame))

            pygame.display.update()
            clock.tick(10)


if __name__ == "__main__":
    # importing my own files here
    import dialogue
    import menus
    import functions
    pygame.init()
    test_font = pygame.font.Font(None, 64)
    menu_sub = pygame.font.Font(None, 32)
    testsurface = pygame.image.load('graphics/testmap2.png').convert()
    gem_orange = pygame.image.load('graphics/gem04.png').convert_alpha()

    # FUNCTIONS
    # Storing functions here

    def player_input(button):
        #if testplayer_frame.colliderect(rec1): return # Not great, leaving this here for now
        global player_x, player_y, start_game # Cannot declare these within the function so they are set to global
        if button in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]: # Check if cursor keys were pressed
            if button in [pygame.K_UP, pygame.K_DOWN]: # Cross-references the key with a dictionary where movement integers are kept
                player_y += (movement[button])
                if collision_check() == True:
                    player_y -= (movement[button])
            else: player_x += (movement[button])
            if collision_check() == True:
                player_x -= (movement[button])

        else: pass# This is for other modifier keys

    def collision_check():
        for x in rec_list:
            if x.collidepoint(player_x,player_y) == True: return True


    def menu_input(button):
        global menu_offset, start_game
        if button == pygame.K_UP and menu_offset > 0:
            menu_offset += (movement[button])
        if button == pygame.K_DOWN and menu_offset < 64:
            menu_offset += (movement[button])
        elif button in [pygame.K_SPACE, pygame.K_RETURN]: # Need to change this later
            (menu_dict[menu_offset])()
            #start_game = True
        else: pass

        # Menu functions
        # These functions are called when the main menu options are selected
        # Maybe externalise these to another file?
    def start_game():
        global start_game
        start_game = True

    def load_game():
        pass

    def exit_game():
        pygame.quit()
        exit()



    '''
    As each block is migrated into Main, it will be archived here incase the class implementation doesn't work

    # DISPLAY SETUP
    # init to select appropriate backend
    # set_mode to select resolution (Window size is a multiple of 8 as tiles will also be sized by a multiple of 8)
    # caption for window title
    pygame.init()
    screen = pygame.display.set_mode((1024,768))
    pygame.display.set_caption('IMProvement')
    #pygame.display.set_icon(testplayer)
    

    # VISUAL ASSETS
    # Loading images here
    testsurface = pygame.image.load('graphics/testmap2.png').convert()
    testplayer = pygame.image.load('graphics/playerimp.png').convert_alpha() # The wee fella
    gem_orange = pygame.image.load('graphics/gem04.png').convert_alpha()
    test_font = pygame.font.Font(None,64)
    menu_sub = pygame.font.Font(None,32)
    '''
    #menu and menu text
    menu_surface = pygame.image.load('graphics/main_menu.png')
    menu_title = test_font.render('IMProvement',False,(255,155,155))
    menu_new_game = menu_sub.render(menus.menu_new.text,True,(menus.menu_list_colour)) # These lines written before Class implementation, refer to menus.py
    menu_load_game = menu_sub.render(menus.menu_load.text,True,(menus.menu_list_colour))
    menu_quit_game = menu_sub.render(menus.menu_quit.text,True,(menus.menu_list_colour))
    pygame.display.set_icon(Main.testplayer) # Window icon
    menu_offset = 0 # Add or subtract multiples of this offset to neatly move the cursor
    menu_dict = {0:start_game,32:load_game,64:exit_game} # Dictionary pairs menu_offset with function names

    #menu_item = menu_sub.render('New Game',True,(255,255,255))



    '''
    Testing menu class stuff here
    
    menu_list_colour = (255,255,255) # RGB Value
    menu_new = Menuitems('New Game',32,0,(menu_list_colour))
    menu_load = Menuitems('Load Game',32,32,(menu_list_colour))
    menu_quit = Menuitems('Quit Game',32,64,(menu_list_colour))
    menu_list = [menu_new, menu_load, menu_quit]
    '''

    # CLOCK SETUP
    # To handle animation and frame control
    clock = pygame.time.Clock()
    time = time.time()
    keytime = pygame.time.get_ticks()

    # INPUT
    # Input-related variables here
    cursorkey = 0
    player_x = 96 + 16 # Adding 16 as an offset as the 'grid' isn't centred on the tiles
    player_y = 96 + 16
    movement = {pygame.K_UP : -32, pygame.K_DOWN : + 32, pygame.K_LEFT : -32, pygame.K_RIGHT : + 32}
    start_game = False # This is so the game starts the menu first

    # RECTANGLES
    # Defining size and position of rectangles before main loop starts
    testplayer_frame = Main.testplayer.get_rect(center = (player_x,player_y)) # This returns a rectangle equal to the size of testplayer, with a centrepoint set to the values of player_x and player_y

    rec1 = pygame.Rect(256+16,256+16,128,128)

    rec2 = pygame.Rect.inflate(pygame.Rect.copy(rec1),-64,-64) # a duplicate of rec1, shrunk by 64px per axis
    pygame.Rect.move_ip(rec2,-16,-16) #moving rec2 to centre it correctly

    rec3 = pygame.Rect.copy(rec2)
    pygame.Rect.move_ip(rec3,0,128)

    #text_rec_y = 768 # 544 is the target!
    #text_rec = pygame.Rect(64,text_rec_y,896,160) # Decent basis for text box size


        #Boundary rectangles
    left_boundary = pygame.Rect(0,0,96,768)
    right_boundary = pygame.Rect(928,0,96,768)
    top_boundary = pygame.Rect(0,0,1024,96)
    bottom_boundary = pygame.Rect(0,672,1024,96)
    lrtb_list = [left_boundary, right_boundary, top_boundary, bottom_boundary] # To tidy up rec_list, adding these recs to a list
    # TEST
    # Temporary code for debugging use
    rec_list = [
        rec1,
        rec2,
        rec3] + lrtb_list
         # rec_list is a list of all the collision objects, some of which are also lists.  Since movement is grid-based all collision can be expressed in rectangles!

    Main()
'''
    # MAIN LOOP
    # Core logic to maintain display and await input from user


    while True: # This is to ensure loop always runs
        for event in pygame.event.get(): # For each event in the event queue:
            if event.type == pygame.QUIT: # If the eventtype is .QUIT:
                pygame.quit() # Tears down the display
                exit() # Properly exits the Python script
            if event.type == pygame.MOUSEBUTTONDOWN: # This is a debug feature for eyeballing where exactly things are
                print(pygame.mouse.get_pos())




            # Main Menu
            if start_game == False:
                Main.screen.blit(menu_surface,(0,0))
                Main.screen.blit(menu_title,(32,32))
                Main.screen.blit(menu_new_game,(832,608))
                Main.screen.blit(menu_load_game,(832,672-menus.menu_load.offset))
                Main.screen.blit(menu_quit_game,(832,736-menus.menu_quit.offset))
                Main.screen.blit(gem_orange,(800,604+menu_offset))
                if event.type == pygame.KEYDOWN:
                    menu_input(event.key)

                if event.type == pygame.MOUSEBUTTONDOWN: # This is a debug feature, delete this later
                    if pygame.mouse.get_pressed(num_buttons=3) == (0,0,1):
                        #screen.blit(testplayer,(pygame.mouse.get_pos())) # Works great though
                        #screen.blit(dialogue.sample_render,(pygame.mouse.get_pos()))
                        pygame.draw.rect(Main.screen, (153,50,204), text_rec)
                        #screen.blit(dialogue.sample_render, (64+16,544+16))
                        dialogue.Textobject.render_text(dialogue.sample_render)



        if start_game == True:
            # Background
            Main.screen.blit(testsurface,(0,0))
            rec1.topleft = 240,240 # Top-left corner should be at given coordinates
            pygame.draw.rect(Main.screen, 'red', rec1) # Draw rec1 to the 'screen', make it 'red'
            pygame.draw.rect(Main.screen, 'green', rec2)
            pygame.draw.rect(Main.screen, 'silver', rec3)

            # Player

            # Player movement
            if event.type == pygame.KEYDOWN:
                player_input(event.key)

            # Collision
            #if testplayer_frame.colliderect(rec1): print("JINKIES")



            testplayer_frame = testplayer.get_rect(center=(player_x, player_y))
            Main.screen.blit(testplayer,(testplayer_frame))


        pygame.display.update()
        clock.tick(10)
'''
