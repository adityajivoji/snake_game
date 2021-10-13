import pygame
import cv2 as cv
pygame.init()
clock = pygame.time.Clock()
width = height = 10
start_pos_x = 320
start_pos_y = 240
pos_array = ((320,240))
screen = pygame.display.set_mode((640,480))
# head = pygame.image.load('3.jpg').convert()
# head_rect = head.get_rect(center = (320,240))
# body = pygame.image.load('1.jpg').convert()
# body_rect = body.get_rect(center = (335,240))
# food = pygame.image.load('2.jpg').convert()
# food_rect = food.get_rect(center = (300,300))
bg = pygame.image.load('grass.jpg')
position = [(320,240),(335,240),(350,240)]
# rectangles = [head_rect,body_rect]
# rectangles.append(body.get_rect(center = (350,240)))
# print(rectangles)
# pygame.draw.rect(screen, RED, (x, y, WIDTH, HEIGHT), 0)

key = 0
img = cv.imread("grass.jpg")

exit_condition = True
while exit_condition and key != 27:
    cv.waitKey(5000)
    screen.blit(bg,(0,0))
    length = len(position) - 1
    print('1')
    for i in range(length):
        position[length - i] = position[length - i - 1]
        print("changung positon")
    print('2')
    print('3')
    for i in range(1,length):
        

    
    #body_rect.left += 1
    # for rect in rectangles:
    #     if(rect == head_rect):
    #         screen.blit(head,rect)
    #         print("its here sir")
    #     else:
    #         screen.blit(body,rect)
    #         print("nbo its here sir")
    #     print("displat reoc")


    print('4')
    pygame.display.update()

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            exit_condition = False
    clock.tick(60)
    key = cv.waitKey(5000)
