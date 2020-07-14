import pygame, random

pygame.init()

screen_info = pygame.display.Info()
print(screen_info)

size = (width, height) = (screen_info.current_w, screen_info.current_h)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (0, 127, 255)
fish_image = pygame.image.load('fish.png')
fish_rect = fish_image.get_rect()
fish_rect.center = (400,300)
fish_image = pygame.transform.smoothscale(fish_image,(80,80))
speed = pygame.math.Vector2(0,10)
rotation = random.randint(0,360)
speed.rotate_ip(rotation)
fish_image = pygame.transform.rotate(fish_image, int(180 - rotation))
def move_fish():
  global fish_image
  fish_rect.move_ip(speed)
  if fish_rect.top < 0 or fish_rect.bottom > screen_info.current_h:
    speed[1] *= -1
    fish_image = pygame.transform.flip(fish_image,False, True )
    fish_rect.move_ip(0, speed[1])
  if fish_rect.left < 0 or fish_rect.right > screen_info.current_w:
    speed[0] *= -1
    fish_image = pygame.transform.flip(fish_image,True, False)
    fish_rect.move_ip(speed[0], 0)
def main():
  while True:
    clock.tick(60)
    move_fish()
    screen.fill(color)
    screen.blit(fish_image, fish_rect)
    pygame.display.flip()
if __name__ == '__main__':
  main()