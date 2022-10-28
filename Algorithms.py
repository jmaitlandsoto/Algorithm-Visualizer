import pygame
import time


class Algorithm():
    def __init__(self, arr):
        self.arr = arr
        self.font = pygame.font.Font('freesansbold.ttf', 8)

    def sort(self, screen):
        print("sort")

    def finale(self, screen):
        for i in range(len(self.arr)):
            time.sleep(0.02)
            for j in range(len(self.arr)):
                if j < i:
                    pygame.draw.rect(screen, (0, 200, 0),
                                     [int(400 - (self.arr[j] * 400 / len(self.arr))), int(j * 600 / len(self.arr)),
                                      int(self.arr[j] * 800 / len(self.arr)), int(600 / len(self.arr))], 0)
                    text = self.font.render(str(self.arr[j]), 1, (255, 255, 255))
                    screen.blit(text,
                                (int(400 + (self.arr[j] * 800 / len(self.arr) / 2)), int(j * 600 / len(self.arr))))
                elif j == i:
                    pygame.draw.rect(screen, (0, 0, 0),
                                     [int(400 - (self.arr[j] * 400 / len(self.arr))), int(j * 600 / len(self.arr)),
                                      int(self.arr[j] * 800 / len(self.arr)), int(600 / len(self.arr))], 0)
                else:
                    pygame.draw.rect(screen, (255, 255, 255),
                                     [int(400 - (self.arr[j] * 400 / len(self.arr))), int(j * 600 / len(self.arr)),
                                      int(self.arr[j] * 800 / len(self.arr)), int(600 / len(self.arr))], 0)
            pygame.display.flip()
        for j in range(len(self.arr)):
            pygame.draw.rect(screen, (0, 200, 0),
                             [int(400 - (self.arr[j] * 400 / len(self.arr))), int(j * 600 / len(self.arr)),
                              int(self.arr[j] * 800 / len(self.arr)), int(600 / len(self.arr))], 0)
        time.sleep(2)

    def clear_screen(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), [0, 0, 1200, 800], 0)

    def handle_events(self):
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop

            if event.type == pygame.MOUSEBUTTONDOWN:
                print("click")


class BubbleSort(Algorithm):
    def __init__(self, arr):
        super().__init__(arr)

    def sort(self, screen):

        sorted = False
        while not sorted:
            sorted = True
            for i in range(len(self.arr) - 1):
                if self.arr[i] > self.arr[i + 1]:
                    self.arr[i], self.arr[i + 1] = self.arr[i + 1], self.arr[i]
                    self.clear_screen(screen)
                    for j in range(len(self.arr)):
                        if j < i:
                            pygame.draw.rect(screen, (100, 100, 100),
                                             [int(400 - (self.arr[j] * 400 / len(self.arr))),
                                              int(j * 600 / len(self.arr)),
                                              int(self.arr[j] * 800 / len(self.arr)), int(600 / len(self.arr))], 0)
                            text = self.font.render(str(self.arr[j]), 1, (255, 255, 255))
                            screen.blit(text, (
                                int(400 + (self.arr[j] * 800 / len(self.arr) / 2)), int(j * 600 / len(self.arr))))

                        elif j == i:
                            pygame.draw.rect(screen, (255, 0, 0),
                                             [int(400 - (self.arr[j] * 400 / len(self.arr))),
                                              int(j * 600 / len(self.arr)),
                                              int(self.arr[j] * 800 / len(self.arr)), int(600 / len(self.arr))], 0)
                            text = self.font.render(str(self.arr[j]), 1, (255, 255, 255))
                            screen.blit(text, (
                                int(400 + (self.arr[j] * 800 / len(self.arr) / 2)), int(j * 600 / len(self.arr))))
                        else:
                            pygame.draw.rect(screen, (255, 255, 255),
                                             [int(400 - (self.arr[j] * 400 / len(self.arr))),
                                              int(j * 600 / len(self.arr)),
                                              int(self.arr[j] * 800 / len(self.arr)), int(600 / len(self.arr))], 0)
                            text = self.font.render(str(self.arr[j]), 1, (255, 255, 255))
                            screen.blit(text, (
                                int(400 + (self.arr[j] * 800 / len(self.arr) / 2)), int(j * 600 / len(self.arr))))
                        self.handle_events()
                    pygame.display.flip()
                    sorted = False
        time.sleep(1)
        self.finale(screen)


class SelectionSort(Algorithm):
    def __init__(self, arr):
        super().__init__(arr)

    def sort(self, screen):
        smallNumIndex = 0
        for i in range(len(self.arr)):
            smallNumIndex += 1
            if smallNumIndex >= len(self.arr):
                smallNumIndex = len(self.arr) - 1
            self.clear_screen(screen)
            for j in range(i, len(self.arr), 1):
                if self.arr[j] < self.arr[smallNumIndex]:
                    smallNumIndex = j
            for x in range(len(self.arr)):
                for x in range(len(self.arr)):
                    if x < i:
                        pygame.draw.rect(screen, (100, 100, 100),
                                         [int(400 - (self.arr[x] * 400 / len(self.arr))), int(x * 600 / len(self.arr)),
                                          int(self.arr[x] * 800 / len(self.arr)), int(600 / len(self.arr))], 0)
                    elif x == i:
                        pygame.draw.rect(screen, (0, 255, 0),
                                         [int(400 - (self.arr[x] * 400 / len(self.arr))), int(x * 600 / len(self.arr)),
                                          int(self.arr[x] * 800 / len(self.arr)), int(600 / len(self.arr))], 0)
                    elif x == smallNumIndex:
                        pygame.draw.rect(screen, (255, 0, 0),
                                         [int(400 - (self.arr[x] * 400 / len(self.arr))),
                                          int(x * 600 / len(self.arr)),
                                          int(self.arr[x] * 800 / len(self.arr)), int(600 / len(self.arr))], 0)
                    else:
                        pygame.draw.rect(screen, (255, 255, 255),
                                         [int(400 - (self.arr[x] * 400 / len(self.arr))), int(x * 600 / len(self.arr)),
                                          int(self.arr[x] * 800 / len(self.arr)), int(600 / len(self.arr))], 0)
                pygame.display.flip()
            self.arr[i], self.arr[smallNumIndex] = self.arr[smallNumIndex], self.arr[i]
        self.finale(screen)


class InsertionSort(Algorithm):
    def __init__(self, arr):
        super().__init__(arr)

    def sort(self, screen):
        for i in range(1, len(self.arr)):
            x = i
            while x > 0 and self.arr[x - 1] > self.arr[x]:
                self.arr[x], self.arr[x - 1] = self.arr[x - 1], self.arr[x]
                x -= 1
                self.clear_screen(screen)
                for j in range(len(self.arr)):
                    if j < x:
                        pygame.draw.rect(screen, (100, 100, 100),
                                         [int(400 - (self.arr[j] * 400 / len(self.arr))), int(j * 600 / len(self.arr)),
                                          int(self.arr[j] * 800 / len(self.arr)), int(600 / len(self.arr))], 0)
                    elif j == x:
                        pygame.draw.rect(screen, (255, 0, 0),
                                         [int(400 - (self.arr[j] * 400 / len(self.arr))), int(j * 600 / len(self.arr)),
                                          int(self.arr[j] * 800 / len(self.arr)), int(600 / len(self.arr))], 0)
                    else:
                        pygame.draw.rect(screen, (255, 255, 255),
                                         [int(400 - (self.arr[j] * 400 / len(self.arr))), int(j * 600 / len(self.arr)),
                                          int(self.arr[j] * 800 / len(self.arr)), int(600 / len(self.arr))], 0)
                pygame.display.flip()
        self.finale(screen)