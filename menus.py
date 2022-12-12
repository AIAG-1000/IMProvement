'''
This file will hold various menu functions to be called by the main process
'''
class Menuitems: # Testing classes with these menu functions, will be handy if more menus are needed later

    def __init__(self,text,size,offset,colour): # Each example of Menuitems will have a name, a size and an offset
        #self.name = name
        self.text = text # The string that will be rendered to screen
        self.size = size # Determines font size
        self.offset = offset # Determines Y-offset when positioning text
        self.colour = colour # RGB value as a tuple, eg (255,255,255)

    def start_game(self):
        global start_game
        start_game = True

    def load_game(self):
        pass # First work out how to save the game, then put the opposite of that here I guess

    def exit_game(self):
        pygame.quit()
        exit()

#Main Menu Items
menu_list_colour = (255,155,155) # RGB Value
menu_new = Menuitems('New Game',32,0,(menu_list_colour))
menu_load = Menuitems('Load Game',32,32,(menu_list_colour))
menu_quit = Menuitems('Quit Game',32,64,(menu_list_colour))
menu_list = [menu_new, menu_load, menu_quit]