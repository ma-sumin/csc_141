# 12-4. Rocket
import pygame

class Rocket:
    """A class to manage the rocket."""

    def __init__(self, ai_game):
        """Initianlize the rocket and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the rocket image and get its rect.
        self.image = pygame.image.load('images/rocket.bmp') # No need to change the background color.

        # Resize the image to (5, 5) if that's what you're aiming for
        self.image = pygame.transform.scale(self.image, (50, 50))
        
        self.rect = self.image.get_rect()

        # Start each new rocket at the center of the screen.
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the rocket at its current location."""
        self.screen.blit(self.image, self.rect)