import pygame
import math
import random
import os
import string

# Setup game
pygame.init()
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game!")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load images
images = []
lst = os.listdir('images')
for i in range(0, len(lst) - 1):
    image = pygame.image.load("images/hangman" + str(i) + ".png")
    images.append(image)

# Button games variables
RADIUS = 20
GAP = 15
letters = []
x_start_pos = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
y_start_pos = 400
alphabet = list(string.ascii_uppercase)
for i in range(26):
    x = x_start_pos + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = y_start_pos + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, alphabet[i], True])

# Fonts
LETTER_FONT = pygame.font.SysFont('Ariel', 40)
WORD_FONT = pygame.font.SysFont('Ariel', 60)
TITLE_FONT = pygame.font.SysFont('Ariel', 70)

# Get words from text file
with open('words.txt', 'r') as f:
    file_words = f.readlines()
words = []
for file_word in file_words:
    words.append(file_word[:-1].upper())
word = random.choice(words)

# Game variables
hangman_status = 0
guessed = []
running = True


def draw():
    screen.fill(WHITE)

    text = TITLE_FONT.render("DEVELOPER HANGMAN", True, BLACK)
    screen.blit(text, (WIDTH / 2 - text.get_width() / 2, 20))

    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, True, BLACK)
    screen.blit(text, (400, 200))

    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(screen, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, True, BLACK)
            screen.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))

    screen.blit(images[hangman_status], (150, 100))
    pygame.display.update()


def display_message(message):
    pygame.time.delay(1000)
    screen.fill(WHITE)
    text = WORD_FONT.render(message, True, BLACK)
    screen.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(3000)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr, visible = letter
                if visible:
                    dis = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)
                    if dis < RADIUS:
                        letter[3] = False
                        guessed.append(ltr)
                        if ltr not in word:
                            hangman_status += 1

    draw()

    won = True
    for letter in word:
        if letter not in guessed:
            won = False
            break

    if won:
        display_message("You WON!")
        break

    if hangman_status == 6:
        display_message("You LOST!")
        break

pygame.quit()
