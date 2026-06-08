'''import pygame
pygame.init()
pygame.mixer.music.load('Ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()'''


import pygame

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("Ex021.mp3")
pygame.mixer.music.play()

input("Pressione ENTER para sair...")