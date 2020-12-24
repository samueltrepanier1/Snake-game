import pygame
import sys
import random

#TODO Ajouter un menu avant de démarrer
#TODO Ajouter une touche pour montrer/cacher les informations
#TODO Ajouter les informations (direction tête, direction queu, vision (8 axes -distance mur, présence pomme, présence serpent)

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
        if self.length > 1 and (point[0]*-1,point[1]* -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x*GRID_SIZE)) % SCREEN_WIDTH), (cur[1] + (y*GRID_SIZE)) % SCREEN_HEIGTH)

        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()

        elif self.is_out():
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
            pygame.draw.rect(surface, (0,255,94),r,0)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(UP)
                elif event.key == pygame.K_DOWN:
                    self.turn(DOWN)
                elif event.key == pygame.K_LEFT:
                    self.turn(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.turn(RIGTH)
    def is_out(self):S
        if (self.get_head_position()[0] == 0) or (self.get_head_position()[1] == 0):
            return True
        elif (self.get_head_position()[0] == (int((SCREEN_WIDTH)-1*GRID_SIZE))) or (self.get_head_position()[1] == (int((SCREEN_WIDTH)-1*GRID_SIZE))):
            return  True
        else:
            return False


class Food(object):

    def __init__(self):
        self.position = (0,0)
        self.color = (223,163,49)
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(1, GRID_WIDTH - 2) * GRID_SIZE, (random.randint(1, GRID_HEIGTH -2) * GRID_SIZE))
        print(self.position)


    def draw(self, surface):
       r = pygame.Rect((self.position[0],self.position[1]), (GRID_SIZE,GRID_SIZE))
       pygame.draw.rect(surface, self.color,r)
       pygame.draw.rect(surface, (255, 0, 0), r, 0)


def drawGrid(surface):
    for y in range(0,int(GRID_HEIGTH)):
        for x in range(0, int(GRID_WIDTH)):



            if (x+y) % 2 == 0:
                r = pygame.Rect((x*GRID_SIZE,y*GRID_SIZE), (GRID_SIZE,GRID_SIZE))
                pygame.draw.rect(surface,(25,25,25),r)
            else:
                rr = pygame.Rect((x * GRID_SIZE, y * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
                pygame.draw.rect(surface, (20, 20, 20), rr)

            if (x == 0) or (y == 0) or x == (int(GRID_HEIGTH)-1) or y == (int(GRID_HEIGTH)-1):
                rrr = pygame.Rect((x * GRID_SIZE, y * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
                pygame.draw.rect(surface, (0, 0, 0), rrr)




def FoodInSnake(food, snake):
    if food.position in snake.positions:
        return True
    else:
        return False


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

    myfont = pygame.font.SysFont("monospace", 16)

    while True:
        score = len(snake.positions)
        clock.tick(15)
        snake.handle_keys()
        drawGrid(surface)
        snake.move()
        if snake.get_head_position() == food.position:
            snake.length += 1


            food.randomize_position()
            #Make sure the food is not in the snake
            while(FoodInSnake(food, snake)):
                food.randomize_position()


        if(snake.is_out() == False):
            snake.draw(surface)
        food.draw(surface)

        screen.blit(surface, (0, 0))
        text_score = myfont.render("Score {0}".format(score), 1, (255, 255, 255))
        text_head = myfont.render("Head = {0}".format(snake.get_head_position()), 1, (255, 255, 255))
        text_food = myfont.render("Food = {0}".format(food.position), 1, (255, 255, 255))
        screen.blit(text_score, (5, 5))
        screen.blit(text_head, (5, 25))
        screen.blit(text_food, (5, 45))
        pygame.display.update()

main()