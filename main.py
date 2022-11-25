"""
Currently working on:
A function to handle player movement -x
Collision works, currently have to scale it up


"""
#  importing pygame to do most things
#  importing exit to prevent crashes when closing game
# importing time because I keep wasting it
import pygame
from sys import exit
import time



# FUNCTIONS
# Storing functions here

def player_input(button):
    #if testplayer_frame.colliderect(rec1): return # Not great, leaving this here for now
    global player_x, player_y, start_game # Cannot declare these within the function so they are set to global
    if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]: # Check if cursor keys were pressed
        if event.key in [pygame.K_UP, pygame.K_DOWN]: # Cross-references the key with a dictionary where movement integers are kept
            player_y += (movement[event.key])
            if collision_check() == True:
                player_y -= (movement[event.key])
        else: player_x += (movement[event.key])
        if collision_check() == True:
            player_x -= (movement[event.key])

    elif event.key == pygame.K_SPACE: start_game = True

    else: pass# This is for other modifier keys

def collision_check():
    for x in rec_list:
        if x.collidepoint(player_x,player_y) == True: return True










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
testsurface = pygame.image.load('graphics/testmap.png').convert()
testplayer = pygame.image.load('graphics/playerimp.png').convert_alpha() # The wee fella
test_font = pygame.font.Font(None,64)

#menu and menu text
menu_surface = pygame.image.load('graphics/main_menu.png')
menu_title = test_font.render('IMProvement',False,(255,255,255))
pygame.display.set_icon(testplayer) # Window icon

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
testplayer_frame = testplayer.get_rect(center = (player_x,player_y)) # This returns a rectangle equal to the size of testplayer, with a centrepoint set to the values of player_x and player_y

rec1 = pygame.Rect(256+16,256+16,128,128)

rec2 = pygame.Rect.inflate(pygame.Rect.copy(rec1),-64,-64) # a duplicate of rec1, shrunk by 64px per axis
pygame.Rect.move_ip(rec2,-16,-16) #moving rec2 to centre it correctly

rec3 = pygame.Rect.copy(rec2)
pygame.Rect.move_ip(rec3,0,128)

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


# MAIN LOOP
# Core logic to maintain display and await input from user


while True: # This is to ensure loop always runs
    for event in pygame.event.get(): # For each event in the event queue:
        if event.type == pygame.QUIT: # If the eventtype is .QUIT:
            pygame.quit() # Tears down the display
            exit() # Properly exits the Python script



        # Main Menu
        if start_game == False:
            screen.blit(menu_surface,(0,0))
            screen.blit(menu_title,(32,32))
            if event.type == pygame.KEYDOWN:
                player_input(event.key)


    if start_game == True:
        # Background
        screen.blit(testsurface,(0,0))
        rec1.topleft = 240,240 # Top-left corner should be at given coordinates
        pygame.draw.rect(screen, 'red', rec1) # Draw rec1 to the 'screen', make it 'red'
        pygame.draw.rect(screen, 'green', rec2)
        pygame.draw.rect(screen, 'silver', rec3)

        # Player

        # Player movement
        if event.type == pygame.KEYDOWN:
            player_input(event.key)

        # Collision
        #if testplayer_frame.colliderect(rec1): print("JINKIES")



        testplayer_frame = testplayer.get_rect(center=(player_x, player_y))
        screen.blit(testplayer,(testplayer_frame))


    pygame.display.update()
    clock.tick(10)

