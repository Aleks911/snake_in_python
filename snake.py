import pygame
import sys
import random
import time




class Snake():
    def __init__(self):
        self.position = [100,50]
        self.body = [[100,50],[90,50],[80,50]]
        self.direction = "RIGHT"
        self.changeDirectionTo = self.direction

    def changeDirTo(self, dir):
        if dir == "RIGHT" and not self.direction == "LEFT":
            self.direction = "RIGHT"
        if dir == "LEFT" and not self.direction == "RIGHT":
            self.direction = "LEFT"
        if dir == "UP" and not self.direction == "DOWN":
            self.direction = "UP"
        if dir == "DOWN" and not self.direction == "UP":
            self.direction = "DOWN"

    def move(self, foodPosition, starPosition):
        if self.direction == "RIGHT":
            self.position[0] += 10
        if self.direction == "LEFT":
            self.position[0] -= 10
        if self.direction == "UP":
            self.position[1] -= 10
        if self.direction == "DOWN":
            self.position[1] += 10

        self.body.insert(0, list(self.position))
        if self.position == foodPos or self.position == starPos:
            return 1

        else:
            self.body.pop()
            return 0



    def checkCollision(self):
        if self.position[0] > 490 or self.position[0] < 0:
            return 1
        elif self.position[1] > 490 or self.position[1] < 0:
            return 1
        for bodyPart in self.body[1:]:
            if self.position == bodyPart:
                return 1
        return 0

    def getHeadPos(self):
        return self.position
    def getBody(self):
        return self.body

class FoodSpawer():
    def __init__(self):
        self.position = [random.randrange(1,50)*10, random.randrange(1,50)*10]
        self.isFoodOnScreen = True

    def spawnFood(self):
        if self.isFoodOnScreen == False:
            self.position = [random.randrange(1,50)*10, random.randrange(1,50)*10]
            self.isFoodOnScreen = True
        return self.position

    def setFoodOnScreen(self, b):
        self.isFoodOnScreen = b



class Star():
    def __init__(self):
        self.position = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10]
        self.isStarOnScreen = True

    def spawnStar(self):
        if self.isStarOnScreen == False:
            self.position = [random.randrange(1,50)*10, random.randrange(1,50)*10]
            self.isStarOnScreen = True
        return self.position

    def setStarOnScreen(self, b):
        self.isStarOnScreen = b




window = pygame.display.set_mode((500,500))
pygame.display.set_caption("Wow  Snake")
fps = pygame.time.Clock()
score = 0
starImg = pygame.image.load('star.png')
snake = Snake()
foodSpawer = FoodSpawer()

starSpawer = Star()


def gameOver():
    screen = pygame.display.set_mode((500, 500))
    pygame.font.init()

    myfont = pygame.font.SysFont('Comic Sans MS', 20)

    textsurface = myfont.render('Twój wynik: ' + str(score) + '  Aby zakończyć naciśnij ESC', False, (255, 255, 255))

    screen.blit(textsurface, (50, 180))

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()





while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.changeDirTo('RIGHT')
            if event.key == pygame.K_LEFT:
                snake.changeDirTo('LEFT')
            if event.key == pygame.K_UP:
                snake.changeDirTo('UP')
            if event.key == pygame.K_DOWN:
                snake.changeDirTo('DOWN')


    foodPos = foodSpawer.spawnFood()
    starPos = starSpawer.spawnStar()

    if (snake.move(foodPos,starPos) == 1):

        if (snake.getHeadPos() == foodPos):
            foodSpawer.setFoodOnScreen(False)
            score += 1

        elif (snake.getHeadPos() == starPos):
            starSpawer.setStarOnScreen(False)
            score += 10





    window.fill(pygame.Color(225,225,225))
    for pos in snake.getBody():
        pygame.draw.rect(window, pygame.Color(0,225,0), pygame.Rect(pos[0],pos[1],10,10))
    pygame.draw.rect(window, pygame.Color(225,0,0), pygame.Rect(foodPos[0],foodPos[1],10,10))


    if score!=0 and score%6==0:
        window.blit(starImg,(starPos[0],starPos[1]))



    if (snake.checkCollision() == 1):
        gameOver()

    pygame.display.set_caption("Wow Snake | Score : " + str(score))
    pygame.display.flip()
    fps.tick(12)


