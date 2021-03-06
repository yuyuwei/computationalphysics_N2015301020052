#A bouncing ball

import sys, pygame

__author__ = {'name' : 'Hongten',
              'mail' : 'hongtenzone@foxmail.com',
              'blog' : 'http://www.cnblogs.com/hongten',
              'QQ'   : '648719819',
              'Version' : '1.0'}

pygame.init()

size = width, height = 600, 500
speed = [1, 1]
black = 249, 130, 57

screen = pygame.display.set_mode(size)

ball = pygame.image.load('c:\\test\\ball.gif')
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = - speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
