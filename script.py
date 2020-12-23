import pygame
import sys
import random

SCREEN_WIDTH = 480
SCREEN_HEIGTH = 480

GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH / GRID_SIZE
GRID_HEIGTH = SCREEN_HEIGTH / GRID_SIZE

UP = (0,-1)
DOWN= (0,1)
LEFT = (-1,0)
RIGTH = (1,0)


class Snake(object):

    def __init__(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH/2), (SCREEN_HEIGTH/2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGTH])
        self.color = (17, 24, 47)

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0]* -1,point[1]* -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x*GRID_SIZE)) % SCREEN_WIDTH), (cur[1] + (y*GRID_SIZE % SCREEN_HEIGTH)))

        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()

        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH/2), (SCREEN_HEIGTH/2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGTH])

    def draw(self,surface):
        for x in self.positions:
            r = pygame.Rect((x[0],x[1]), (GRID_SIZE,GRID_SIZE))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (93,216,228),r,1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(UP)
                elif event.key == pygame.KEYDOWN:
                    self.turn(DOWN)
                elif event.key == pygame.K_LEFT:
                    self.turn(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.turn(RIGTH)

class Food(object):

    def __init__(self):
        self.position = (0,0)
        self.color = (223,163,49)
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH - 1) * GRID_SIZE, (random.randint(0, GRID_HEIGTH -1) * GRID_SIZE))

    def draw(self, surface):
       r = pygame.Rect((self.position[0],self.position[1]), (GRID_SIZE,GRID_SIZE))
       pygame.draw.rect(surface, self.color,r)
       pygame.draw.rect(surface, (93, 216, 228), r, 1)


def drawGrid(surface):
    for y in range(0,int(GRID_HEIGTH)):
        for x in range(0, int(GRID_WIDTH)):
            if (x+y) % 2 == 0:
                r = pygame.Rect((x*GRID_SIZE,y*GRID_SIZE), (GRID_SIZE,GRID_SIZE))
                pygame.draw.rect(surface,(93,216,228),r)
            else:
                rr = pygame.Rect((x * GRID_SIZE, y * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
                pygame.draw.rect(surface, (84, 194, 205), rr)




def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_HEIGTH,SCREEN_HEIGTH),0,32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    drawGrid(surface)

    score = 0
    snake = Snake()
    food = Food()

    while True:

        clock.tick(10)
        snake.handle_keys()
        drawGrid(surface)
        snake.move()

        if snake.get_head_position() == food.position:
            snake.length += 1
            score += 1
            food.randomize_position()
        snake.draw(surface)
        food.draw(surface)
     #   myfont = pygame.font.SysFont('timesnewroman', 30)
        screen.blit(surface, (0, 0))
      #  text = myfont.render("Score {0}".format(score),1,(0,0,0))
      #  screen.blit(text, (5, 10))
        pygame.display.update()
main()