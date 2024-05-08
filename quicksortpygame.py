import pygame
import sys
import random

def quicksort(v):
    if len(v) <= 1:
        return v
    pivot = v[len(v) // 2]
    left = [x for x in v if x < pivot]
    middle = [x for x in v if x == pivot]
    right = [x for x in v if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Quicksort Visualizado com Pygame")
    clock = pygame.time.Clock()

    v = [9, 8, 7, 4, 3]   

    sorted_v = quicksort(v)
    bar_width = 30
    gap = 10
    bar_height_factor = 50

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((255, 255, 255))

       
        for i in range(len(sorted_v)):
            pygame.draw.rect(screen, (0, 0, 0), (i * (bar_width + gap), 600 - sorted_v[i] * bar_height_factor, bar_width, sorted_v[i] * bar_height_factor))


        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()