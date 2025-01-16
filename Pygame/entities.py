import pygame, time
from pygame.locals import *


class Animation: # 
    def __init__(self, sprite_sheet, frame_width, frame_height, frame_count, fps):
        self.sprite_sheet = sprite_sheet
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.frame_count = frame_count
        self.fps = fps
        self.frames = self._extract_frames()
        self.current_frame = 0
        self.time_per_frame = 1000 / self.fps  # Milliseconds per frame
        self.last_update = pygame.time.get_ticks()

    def _extract_frames(self):
        """Extract frames from the sprite sheet."""
        frames = []
        sheet_width, sheet_height = self.sprite_sheet.get_size()
        for i in range(self.frame_count):
            x = (i * self.frame_width) % sheet_width
            y = (i * self.frame_width) // sheet_width * self.frame_height
            frame = self.sprite_sheet.subsurface(pygame.Rect(x, y, self.frame_width, self.frame_height))
            frames.append(frame)
        return frames

    def update(self):
        """Update the current frame based on time."""
        now = pygame.time.get_ticks()
        if now - self.last_update > self.time_per_frame:
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % self.frame_count

    def get_frame(self):
        """Get the current frame to render."""
        return self.frames[self.current_frame]

class Player:
    def __init__(self, x, y):
        self.current_pos = (x, y)
        self.player_speed = 10
        self.idle_animation = pygame.image.load("idle.png")
        self.walk_up_animation = pygame.image.load("walking_up.png")
        self.walk_down_animation = pygame.image.load("walking_down.png")
        self.walk_left_animation = pygame.image.load("walking_left.png")
        self.walk_right_animation = pygame.image.load("walking_right.png")

        # Define animations
        self.idle_animation = Animation(self.idle_animation, 50, 50, 10, 12)  # 10 frames, 12 FPS
        self.walk_up_animation = Animation(self.walk_up_animation, 50, 50, 12, 12)  # Example for walking up
        self.walk_down_animation = Animation(self.walk_down_animation, 50, 50, 12, 12)
        self.walk_left_animation = Animation(self.walk_left_animation, 50, 50, 12, 12)
        self.walk_right_animation = Animation(self.walk_right_animation, 50, 50, 12, 12)

        self.current_animation = self.idle_animation

    def player_movement(self, current_pos):
        player_x, player_y = current_pos
        keys = pygame.key.get_pressed()
        moved = False

        if keys[K_w]:  # Moves player up
            player_y -= self.player_speed
            self.current_animation = self.walk_up_animation
            moved = True
        if keys[K_s]:  # Moves player down
            player_y += self.player_speed
            self.current_animation = self.walk_down_animation
            moved = True
        if keys[K_a]:  # Moves player left
            player_x -= self.player_speed
            self.current_animation = self.walk_left_animation
            moved = True
        if keys[K_d]:  # Moves player right
            player_x += self.player_speed
            self.current_animation = self.walk_right_animation
            moved = True

        if not moved:
            self.current_animation = self.idle_animation

        current_pos = player_x, player_y
        return current_pos

    def player_animation(self, screen, x, y):
        self.current_animation.update()
        frame = self.current_animation.get_frame()
        screen.blit(frame, (x, y))


    def player_out_of_bounds(self, pos_x, pos_y, bounds_x, bounds_y):
        return pos_x < 0 or pos_x > (bounds_x - 50) or pos_y < 0 or pos_y > (bounds_y - 50)

    def check_touching_enemy(self, sprite_group):
        return any(pygame.sprite.spritecollide(self, sprite_group, False))
    
    def player_mechanics(self):
        pass
    
class Enemy():
    def __init__(self):
        self.jumpscare_photo = "pranushan-ditherlicious.png"
        self.jumpscare_sound = "pranushan_jumpscare.flac"
    def jumpscare(self,screen):
            jumpscare = pygame.image.load(self.jumpscare_photo)
            pygame.mixer.music.load(self.jumpscare_sound)
            pygame.mixer.music.play(0,0,0)
            jumpscare = pygame.transform.scale(jumpscare, (700,700))
            screen.fill((0,0,0))
            screen.blit(jumpscare,(0,0))
            pygame.display.update()
            time.sleep(8)
            
class Bosses(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.image = pygame.image.load("pranushan red.jpg")  # Load boss sprite image
        self.image = pygame.transform.scale(self.image, (100, 100))  # Scale to 50x50
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed

    def follow_player(self, player_pos):
        """Move the boss toward the player's position."""
        player_x, player_y = player_pos
        boss_x, boss_y = self.rect.center

        # Calculate direction vector
        dir_x = player_x - boss_x
        dir_y = player_y - boss_y

        # Normalize direction vector
        length = max((dir_x**2 + dir_y**2) ** 0.5, 1)  # Avoid division by zero
        dir_x /= length
        dir_y /= length

        # Update boss position
        self.rect.x += int(dir_x * self.speed)
        self.rect.y += int(dir_y * self.speed)