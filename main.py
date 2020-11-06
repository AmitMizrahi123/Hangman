import pygame
import random
import os

# Setup game display
pygame.init()
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game!")

# Load images
images = []
lst = os.listdir('images')
for i in range(0, len(lst) - 1):
    image = pygame.image.load("images/hangman" + str(i) + ".png")
    images.append(image)

# Get words from text file
with open('words.txt', 'r') as f:
    file_words = f.readlines()
words = []
for word in enumerate(file_words):
    if word[0] == len(file_words) - 1:
        words.append(word[1])
    else:
        words.append(word[1][:-1])

# Gave variables
word = random.choice(words)
hangman_status = 0
guessed = []
running = True

# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
