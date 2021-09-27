import pygame
import cv2 as cv
pygame.init()
clock = pygame.time.Clock()
start_pos_x = 320
start_pos_y = 240
pos_array = ((320,240))
screen = pygame.display.set_mode((640,480))
head = pygame.image.load('3.jpg').convert()
head_rect = head.get_rect(center = (320,240))
body = pygame.image.load('1.jpg').convert()
body_rect = body.get_rect(center = (335,240))
food = pygame.image.load('2.jpg').convert()
food_rect = food.get_rect(center = (300,300))
bg = pygame.image.load('grass.jpg')
position = [(320,240),(335,240),(350,240),(365,240)]
rectangles = [head_rect,body_rect]
rectangles.append(body.get_rect(center = position[2]))
rectangles.append(body.get_rect(center = position[3]))

counter = 0


exit_condition = True
while exit_condition:
    screen.blit(bg,(0,0))
    length = len(position)
    limit = length - 1
    for i in range(limit):
        position[limit - i] = position[limit - i - 1]
    if(counter < 5):
        position[0] = (position[0][0] - 15 ,position[0][1])
    elif(counter > 4 and counter <10):
        position[0] = (position[0][0] ,position[0][1] + 15)
    elif(counter > 9 and counter < 15):
        position[0] = (position[0][0] + 15,position[0][1])
    else:
        position[0] = (position[0][0] ,position[0][1] - 15)
    for i in range(length):
        rectangles[i].x = position[i][0]
        rectangles[i].y = position[i][1]

    
    for rect in rectangles:
        if(rect == head_rect):
            screen.blit(head,rect)
        else:
            screen.blit(body,rect)
    counter = counter + 1
    if(counter > 20):
        counter = 0
    pygame.display.update()

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            exit_condition = False
    clock.tick(10)