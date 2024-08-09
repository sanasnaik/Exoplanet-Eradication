import pygame, pyghelpers

# screens
background = pygame.image.load('images/tutorial/computer_background.png')
notif = pygame.image.load('images/tutorial/notification.png')
explanation = pygame.image.load('images/tutorial/explanation.png')
instructions = pygame.image.load('images/tutorial/instructions.png')
loading = pygame.image.load('images/tutorial/loading.png')

class TutorialScene(pyghelpers.Scene):

    def __init__(self, window):

        self.window = window
        self.clock = pygame.time.Clock()

        self.show_tutorial = False
        self.show_instructions = False
        
    def enter(self, music):

        # pygame.mixer.music.load('audio/scizzie - aquatic ambience.mp3')
        # pygame.mixer.music.play()
        
        self.start_time = pygame.time.get_ticks()

    def handleInputs(self, eventsList, keyPressedList):

        mouse = pygame.mouse.get_pos()
        self.clock.tick(60)
        current_time = pygame.time.get_ticks()

        for event in eventsList:
            if event.type == pygame.QUIT: 
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                # if the mouse is clicked on email
                if (current_time >= 5000 and 428 <= mouse[0] <= 529 and 240 <= mouse[1] <= 300):
                    self.show_tutorial = True
                    self.email_start_time = pygame.time.get_ticks()

                # mouse clicked on start first task
                elif (356 <= mouse[0] <= 603 and 336 <= mouse[1] <= 386): 
                    self.show_instructions = True
                    self.show_tutorial = False

                # mouse clicked on begin task one
                elif (self.show_instructions and 356 <= mouse[0] <= 603 and 379 <= mouse[1] <= 429):
                    self.goToScene('LEVEL_ONE')

    def draw(self):

        self.clock.tick(60)
        current_time = pygame.time.get_ticks()

        if ((current_time - self.start_time) < 5000):
            self.window.blit(background, (0,0))
            
        elif (self.show_tutorial):
            self.window.blit(explanation, (0,0))
        
        elif (self.show_instructions):
            self.window.blit(instructions, (0,0))

        else:
            self.window.blit(notif, (0,0))