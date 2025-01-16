import pygame, sys, entities, maps, time, os

##########################################################################
#                               INITIALIZER                              #
##########################################################################

pygame.init()
screen = pygame.display.set_mode((700, 700))
clock = pygame.time.Clock()
enemies = entities.Enemy()


##########################################################################
#                               METHODS                                  #
##########################################################################

def ctpd(): # Locates where the script is currently running, and then changes to parent directory of the file
    directoryLocation = os.path.realpath(__file__)
    fileName = os.path.basename(__file__)
    os.chdir(directoryLocation[0:-(len(fileName))])
ctpd()

def main_menu():
    screen.fill(BG)
    screen.blit(start_button_image, START_BUTTON_RECT)
    screen.blit(controls_button_image, CONTROLS_BUTTON_RECT)
    pygame.display.flip()

def controls():
    screen.fill(BLACK)
    title_text = Text("CONTROLS:", 60, WHITE, (SCREEN_WIDTH // 2, 100), font_type="Roboto/Roboto-Black.ttf")
    KEY_W_text = Text("W = Move Up", 45, WHITE, (SCREEN_WIDTH // 2, 200), font_type="Roboto/Roboto-Light.ttf")
    KEY_A_text = Text("A = Move Left", 45, WHITE, (SCREEN_WIDTH // 2, 250), font_type="Roboto/Roboto-Light.ttf")
    KEY_S_text = Text("S = Move Down", 45, WHITE, (SCREEN_WIDTH // 2, 300), font_type="Roboto/Roboto-Light.ttf")
    KEY_D_text = Text("D = Move Right", 45, WHITE, (SCREEN_WIDTH // 2, 350), font_type="Roboto/Roboto-Light.ttf")
    title_text.draw(screen)
    KEY_W_text.draw(screen)
    KEY_A_text.draw(screen)
    KEY_S_text.draw(screen)
    KEY_D_text.draw(screen)
    pygame.display.flip()

def loading_screen():
    start_time = pygame.time.get_ticks()  # Get the starting time
    count_down = 3  # Start from 3

    while count_down > 0:
        screen.fill(BLACK)
        # Display the countdown number
        Text(f"{count_down}..", 60, WHITE, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), font_type="Roboto/Roboto-Black.ttf").draw(screen)
        
        pygame.display.flip()  # Update the screen
        
        # Wait for a second (or until a second has passed since start_time)
        while pygame.time.get_ticks() - start_time < 1000:  # 1000 milliseconds = 1 second
            pygame.event.pump()  # Make sure pygame events are handled (e.g., quitting)
        
        # Decrease the countdown
        count_down -= 1
        start_time = pygame.time.get_ticks()  # Reset start time for the next countdown
    
    # After the countdown ends, clear the screen
    screen.fill(BLACK)
    pygame.display.flip()

def level_1():
    loading_screen()
    screen_size = (700, 700)
    screen = pygame.display.set_mode(screen_size)
    player_data = entities.Player(0, 0)
    map_load = maps.Maps()
    old_pos = player_data.current_pos
    new_pos = player_data.current_pos
    running = True
    lives = 1
    pygame.mixer.music.load("pranushan_neo.wav")
    pygame.mixer.music.play(-1)
    # Load the map and get the barriers
    barriers = map_load.map_1(screen)
    if barriers is None:
        barriers = []

    while running:
        clock.tick(12)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Get new position from player movement
        new_pos = player_data.player_movement(old_pos)
        is_OOB = player_data.player_out_of_bounds(*new_pos, *screen_size)
        
        # Create a rect for the new position
        new_rect = pygame.Rect(*new_pos, 50, 50)

        # Check for collision with walls
        if any(new_rect.colliderect(barrier) for barrier in barriers):
            lives -= 1  # Lose a life
            print(f"Hit a wall! Lives remaining: {lives}")
            if lives == 0:
                print("Game Over! You ran out of lives.")
                enemies.jumpscare(screen)
                pygame.quit()
                running = False
            else:
                new_pos = old_pos  # Reset position to prevent movement through walls

        elif not is_OOB:
            old_pos = new_pos  # Update position ONLY if no collision and not out of bounds

        # Clear screen and redraw everything
        screen.fill((0, 0, 0))

        # Background image
        screen.blit(background, (0, 0))

        # Draw barriers
        for barrier in barriers:
            pygame.draw.rect(screen, (255, 0, 0), barrier)

        # Draw player using animation instead of a rectangle
        player_data.player_animation(screen, *old_pos)

        # Draw checkpoint
        checkpoint = pygame.Rect(600, 50, 50, 50)
        pygame.draw.rect(screen, (255, 255, 255), checkpoint)

        if new_rect.colliderect(checkpoint):
            print("You won!")
            state = LEVEL_2
            running = False
            

        pygame.display.flip()  # Update the screen

    return state

def level_2():
    screen_size = (700, 700)
    screen = pygame.display.set_mode(screen_size)
    player_data = entities.Player(0, 600)
    map_load = maps.Maps()
    old_pos = player_data.current_pos
    new_pos = player_data.current_pos
    running = True
    lives = 1 
    
    # Load the map and get the barriers
    barriers = map_load.map_2(screen)
    if barriers is None:
        barriers = []

    while running:
        clock.tick(12)  # Limit game loop to 12 FPS (matching animation FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Get new position from player movement
        new_pos = player_data.player_movement(old_pos)
        is_OOB = player_data.player_out_of_bounds(*new_pos, *screen_size)
        
        # Create a rect for the new position
        new_rect = pygame.Rect(*new_pos, 50, 50)

        # Check for collision with walls
        if any(new_rect.colliderect(barrier) for barrier in barriers):
            lives -= 1  # Lose a life
            print(f"Hit a wall! Lives remaining: {lives}")
            if lives == 0:
                print("Game Over! You ran out of lives.")
                enemies.jumpscare(screen)
                pygame.quit()
                running = False
            else:
                new_pos = old_pos  # Reset position to prevent movement through walls

        elif not is_OOB:
            old_pos = new_pos  # Update position ONLY if no collision and not out of bounds

        # Clear screen and redraw everything
        screen.fill((0, 0, 0))

        # Background image
        screen.blit(background, (0, 0))

        # Draw barriers
        for barrier in barriers:
            pygame.draw.rect(screen, (255, 0, 0), barrier)

        # Draw player using animation instead of a rectangle
        player_data.player_animation(screen, *old_pos)

        # Draw checkpoint
        checkpoint = pygame.draw.rect(screen, WHITE,(500,430,50,50)) # (placeholder) goal

        if new_rect.colliderect(checkpoint):
            print("You won!")
            state = LEVEL_3
            running = False

        pygame.display.flip()  # Update the screen

    return state

def level_3():
    screen_size = (700, 700)
    player_data = entities.Player(580, 50)
    map_load = maps.Maps()
    old_pos = player_data.current_pos
    new_pos = player_data.current_pos
    running = True
    lives = 1 
    # Load the map and get the barriers
    barriers = map_load.map_3(screen)
    if barriers is None:
        barriers = []

    while running:
        clock.tick(12)  # Limit game loop to 12 FPS (matching animation FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Get new position from player movement
        new_pos = player_data.player_movement(old_pos)
        is_OOB = player_data.player_out_of_bounds(*new_pos, *screen_size)
        
        # Create a rect for the new position
        new_rect = pygame.Rect(*new_pos, 50, 50)

        # Check for collision with walls
        if any(new_rect.colliderect(barrier) for barrier in barriers):
            lives -= 1  # Lose a life
            print(f"Hit a wall! Lives remaining: {lives}")
            if lives == 0:
                print("Game Over! You ran out of lives.")
                enemies.jumpscare(screen)
                pygame.quit()
                running = False
            else:
                new_pos = old_pos  # Reset position to prevent movement through walls

        elif not is_OOB:
            old_pos = new_pos  # Update position ONLY if no collision and not out of bounds

        # Clear screen and redraw everything
        screen.fill((0, 0, 0))

        # Background image
        screen.blit(background, (0, 0))

        # Draw barriers
        for barrier in barriers:
            pygame.draw.rect(screen, (255, 0, 0), barrier)

        # Draw player using animation instead of a rectangle
        player_data.player_animation(screen, *old_pos)

        # Draw checkpoint
        checkpoint = pygame.draw.rect(screen, WHITE,(400,40,50,50)) # (placeholder) goal

        if new_rect.colliderect(checkpoint):
            print("You won!")
            state = BOSS
            running = False

        pygame.display.flip()  # Update the screen

    return state

def boss_level():
    pygame.mixer.music.load("pranushan_yapping.wav")
    pygame.mixer.music.play(-1)
    screen_size = (700, 700)
    screen = pygame.display.set_mode(screen_size)
    player_data = entities.Player(350, 350)
    boss = entities.Bosses(100, 100, 6)  # Boss starting position and speed
    clock = pygame.time.Clock()

    running = True
    lives = 1  # Number of player lives

    while running:
        clock.tick(30)  # Limit game loop to 30 FPS

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update player position
        new_pos = player_data.player_movement(player_data.current_pos)
        is_OOB = player_data.player_out_of_bounds(*new_pos, *screen_size)
        if not is_OOB:
            player_data.current_pos = new_pos

        # Update boss position
        boss.follow_player(player_data.current_pos)

        # Check collision between player and boss
        player_rect = pygame.Rect(*player_data.current_pos, 50, 50)
        if boss.rect.colliderect(player_rect):
            lives -= 1
            print(f"Lives remaining: {lives}")
            if lives == 0:
                print("Game Over!")
                enemies.jumpscare(screen)
                running = False
                pygame.quit()

        # Clear screen and redraw everything
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))

        # Draw player
        player_data.player_animation(screen, *player_data.current_pos)

        # Draw boss
        screen.blit(boss.image, boss.rect)

        pygame.display.flip()
##########################################################################
#                               CLASSES                                  #
##########################################################################

class Text:
    def __init__(self, text, font_size, color, position, font_type=None):
        """Creates a text object."""
        if font_type:
            self.font = pygame.font.Font(font_type, font_size) 
        else:
            self.font = pygame.font.Font(None, font_size) 
        self.text = text
        self.color = color
        self.position = position
        self.text_surface = self.font.render(text, True, color)
        self.text_rect = self.text_surface.get_rect(center=position)

    def draw(self, surface):
        """Draws the text on the given surface."""
        surface.blit(self.text_surface, self.text_rect)

##########################################################################
#                          VARIABLES                          #
##########################################################################

# SCREEN DIMENSIONS
SCREEN_WIDTH, SCREEN_HEIGHT = 700, 700
screen_size = (700, 700)
BUTTON_LENGTH, BUTTON_WIDTH = 200, 50

# LOAD BUTTON IMAGES
start_button_image = pygame.image.load("start_button.png")
start_button_image = pygame.transform.scale(start_button_image, (BUTTON_LENGTH, BUTTON_WIDTH))
controls_button_image = pygame.image.load("controls_button.png")
controls_button_image = pygame.transform.scale(controls_button_image, (BUTTON_LENGTH, BUTTON_WIDTH))

# BUTTON RECTANGLES
START_BUTTON_RECT = start_button_image.get_rect(center=(SCREEN_WIDTH // 2, 225))
CONTROLS_BUTTON_RECT = controls_button_image.get_rect(center=(SCREEN_WIDTH // 2, 375))

# RANDOM RECTANGLE
WHITE_RECT = pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(30, 30, 60, 60))

# COLORS / BACKGROUND
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BG = (50, 50, 50)

# GAME STATE
MENU = "menu"
CONTROLS = "controls"
RUNNING = "running"
END = "end"
LEVEL_2 = "level2"
LEVEL_3 = "level3"
BOSS = "boss"

state = MENU

# SPRITES / IMAGES
background = pygame.image.load("background.png")  # Replace with your image file
background = pygame.transform.scale(background, screen_size)  # Scale to fit screen

##########################################################################
#                                 GAME                                   #
##########################################################################

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        elif state == MENU:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if START_BUTTON_RECT.collidepoint(event.pos):
                    state = RUNNING
                elif CONTROLS_BUTTON_RECT.collidepoint(event.pos):
                    state = CONTROLS

        elif state == CONTROLS:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                state = MENU
        

    if state == MENU:
        main_menu()

    if state == CONTROLS:
        controls()

    if state == RUNNING:
        state = level_1()
    
    if state == LEVEL_2:
        state = level_2()

    if state == LEVEL_3:
        state = level_3()

    if state == BOSS:
        boss_level()
    pygame.display.flip()
