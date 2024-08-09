import pygame, pyghelpers, Constants

# intro screens
intro_background = pygame.image.load('images/intro/introscreen.png')
intro_hoverstart = pygame.image.load('images/intro/introscreen_hoverstart.png')

class IntroScene(pyghelpers.Scene):

    def __init__(self, window):

        self.window = window
        self.screen = pygame.display.set_mode((Constants.SCREENWIDTH, Constants.SCREENHEIGHT))
        pygame.display.set_caption("Exoplanet Eradication")
        pygame.display.set_icon(pygame.image.load('images/screenicon.png'))

        # music
        pygame.mixer.music.load('audio/Messages from the Stars.mp3')
        pygame.mixer.music.play()

    def handleInputs(self, eventsList, keyPressedList):

        mouse = pygame.mouse.get_pos()

        for event in eventsList:
            if event.type == pygame.QUIT: 
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN: 
                
                # if the mouse is clicked on start
                if 440 <= mouse[0] <= 519 and 322 <= mouse[1] <= 338: 
                    self.goToScene('TUTORIAL_SCENE')

    def draw(self):

        mouse = pygame.mouse.get_pos()

        # if mouse is hovered on start
        if 440 <= mouse[0] <= 519 and 322 <= mouse[1] <= 338: 
            self.window.blit(intro_hoverstart, (0, 0))
        else:
            self.window.blit(intro_background, (0, 0))
    
    # def leave(self):
    #     pygame.mixer.music.stop()