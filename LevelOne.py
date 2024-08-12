import pygame, pyghelpers, random, requests, Constants

# screens
instructions = pygame.image.load('images/level1/instructions.png')

class LevelOne(pyghelpers.Scene):

    def __init__(self, window):

        self.window = window
        self.startGame = False
        
        self.window = window
        self.screen = pygame.display.set_mode((Constants.SCREENWIDTH, Constants.SCREENHEIGHT))
        pygame.display.set_caption("Exoplanet Eradication")
        pygame.display.set_icon(pygame.image.load('images/screenicon.png'))

        # Initialize planet attributes
        self.x_val = None
        self.y_val = None
        self.radius = None

    def enter(self, blah):

        # base URL
        tap_url = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync"

        # adql query for planet name and number of planets in system
        query_sy_pnum = """
            SELECT pl_name, sy_pnum
            FROM ps
        """
        params = {
            "request": "doQuery",
            "lang": "ADQL", 
            "query": query_sy_pnum, 
            "format": "json" 
        }
 
        response = requests.get(tap_url, params)
        self.exoplanets = response.json() 
        random.shuffle(self.exoplanets)


    def handleInputs(self, eventsList, keyPressedList):

        mouse = pygame.mouse.get_pos()

        for event in eventsList:
            if event.type == pygame.QUIT: 
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN: 
                
                # if the mouse is clicked on start
                if 356 <= mouse[0] <= 603 and 379 <= mouse[1] <= 429:
                    self.startGame = True
                
                # check if clicked in planet
                if self.x_val is not None and self.y_val is not None:
                    distance = ((mouse[0] - self.x_val) ** 2 + (mouse[1] - self.y_val) ** 2) ** 0.5

                    if distance <= self.radius:
                        self.x_val = None
                        self.y_val = None

    def draw(self):

        self.window.fill((0, 0, 0))

        if (self.startGame):

            if self.x_val is None or self.y_val is None:
                self.spawn_planet()
            else:
                pygame.draw.circle(self.window, (self.r_val, self.g_val, self.b_val), (self.x_val, self.y_val), self.radius)
        
        else: 
            self.window.blit(instructions, (0,0))

    def spawn_planet(self):
        
        # get random color
        self.r_val = random.randint(10, 255)
        self.g_val = random.randint(10, 255)
        self.b_val = random.randint(10, 255)

        # get random spawnpoint
        self.x_val = Constants.SCREENWIDTH*random.random()
        self.y_val = Constants.SCREENHEIGHT*random.random()

        # radius
        self.radius = Constants.SCREENWIDTH/20

# Logic:
# Get random circular spheres as the images for planets. 
# Underneath the images, state the name of the planet and how many planets are in its system.
# Spawn one image at a time randomly around the screen (random color as well)
# Once right or left clicked, add +1 to the score for a correct click, -1 to the score for an incorrect click. Delete the image and spawn a new one.
# go through the shuffled exoplanet list one by one
