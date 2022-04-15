import pygame
from time import sleep

pygame.init()

window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.mixer.init()
#add first music
pygame.mixer.music.load(".\music\cool.mp3")
pygame.mixer.music.play()
sleep(5)
#add second music
pygame.mixer.music.load(".\music\mg.mp3")
pygame.mixer.music.play()
sleep(0)
#add image
image = pygame.image.load(".\img\scary.jpg")
window.blit(image,(0,0))
pygame.display.update()
sleep(3)