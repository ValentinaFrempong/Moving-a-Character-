import pygame

black = (0,0,0)
white = (255,255,255,)
red = (255,0,0)
purple = (183, 161, 214)
aqua = (85, 181, 165)
purple = (188, 167, 217)
light = (161, 214, 200)

class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """

    # -- Methods
    def __init__(self,filename):

        super().__init__()

        self.image = pygame.image.load(filename).convert()

        self.image.set_colorkey(white)

        self.rect = self.image.get_rect()
        # -- Attributes
        # Set speed vector
        self.change_x = 0
        self.change_y = 0


    def changespeed(self, x, y):
        """ Change the speed of the player"""
        self.change_x += x
        self.change_y += y


    def update(self):
        """ Find a new position for the player"""
        self.rect.x += self.change_x
        self.rect.y += self.change_y


# Call this function so the Pygame library can initialize itself
pygame.init()




# Create an 800x600 sized screen      
screen = pygame.display.set_mode([750, 450])

# Set the title of the window
pygame.display.set_caption('Test')

# Create the player object
player = Player("player.png")
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(player)

clock = pygame.time.Clock()
running = True

bg = pygame.image.load("bg.jpg").convert()
bg_pos = [0,0]

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    

        # Set the speed based on the key pressed
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, -3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 3)

        # Reset speed when key goes up
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, 3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -3)

    # This actually moves the player block based on the current speed
    player.update()

    # -- Draw everything
    # Clear screen
    screen.blit(bg,bg_pos)

    # Draw sprites
    all_sprites_list.draw(screen)

    # Flip screen
    pygame.display.flip()

    # Pause
    clock.tick(60)

pygame.quit()
