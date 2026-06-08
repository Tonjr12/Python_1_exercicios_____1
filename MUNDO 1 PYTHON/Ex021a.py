import pygame

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load('ex021ton.mp3')
pygame.mixer.music.play()

input("Pressione ENTER para sair...")