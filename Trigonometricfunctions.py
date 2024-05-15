import pygame
import sys

PI = 3.1415926535897932384626


# sin 함수
def sin_series(x):
    y = 0
    for i in range(0,5):
        y += ((-1)**i) * ((x)**(2*i+1)) / (factorial(2*i+1))
    return y 

def sin(x):
    # x를 주기인 2π로 나눈 나머지를 구함
    x = x % (2 * PI)
    
    # sin 함수의 주기를 넘어간 경우를 처리하기 위해 범위를 0에서 2π로 변환
    if x < 0:
        x += 2 * PI
        
    if 0 <= x <PI/2:
        return sin_series(x)
    elif 3*PI/2 <= x < 2*PI:
        return sin_series(x-2*PI)
    elif PI/2 <= x < 3*PI/2:
        return sin_series(PI-x)
    else:
        print("error")

# cos 함수
def cos_series(x):
    y = 0
    for i in range(0,5):
        y += ((-1)**i) * ((x)**(2*i)) / (factorial(2*i))
    return y

def cos(x):
    # x를 주기인 2π로 나눈 나머지를 구함
    x = x % (2 * PI)
    
    # sin 함수의 주기를 넘어간 경우를 처리하기 위해 범위를 0에서 2π로 변환
    if x < 0:
        x += 2 * PI
        
    if 0 <= x <PI/2:
        return cos_series(x)
    elif 3*PI/2 <= x < 2*PI:
        return cos_series(x-2*PI)
    elif PI/2 <= x < 3*PI/2:
        return -cos_series(PI-x)
    else:
        print("error")

# tan 함수
def tan(x):
    y = 0
    y = sin(x)/cos(x)
    return y

# 팩토리얼 함수
def factorial(n):
    fac = 1
    for i in range(1, n+1):
        fac *= i
    return fac
    
#dgree to radian
def dtr(n):
    return (PI/180)*n

def rotation(pos_x, pos_y, origin_x, origin_y, angle):
    # 원점으로 평행이동
    pos_x = pos_x - origin_x
    pos_y = pos_y - origin_y

    # 회전
    x = pos_x*cos(angle)-pos_y*sin(angle)
    y = pos_x*sin(angle)+pos_y*cos(angle)

    # 다시 원래 좌표로 평행이동
    x = x + origin_x
    y = y + origin_y

    return (x, y)


# ------------- pygame 구현 -------------

# 화면 초기화
screen = pygame.display.set_mode((192*7, 108*7))
pygame.display.set_caption('Rotation')

point_x = [100,200,200,100]
point_y = [100,100,200,200]

origin_x = 150
origin_y = 150

speed = 5

clock = pygame.time.Clock()
# 메인 루프
while True:
    #이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        pressed = pygame.key.get_pressed()
        # 플레이어 이동
        if pressed[pygame.K_w]: 
            for i in range(0,4):
                point_y[i] -= speed
            origin_y = (point_y[0] + point_y[1] + point_y[2] + point_y[3])/4
        if pressed[pygame.K_a]: 
            for i in range(0,4):
                point_x[i] -= speed
            origin_x = (point_x[0] + point_x[1] + point_x[2] + point_x[3])/4
        if pressed[pygame.K_s]: 
            for i in range(0,4):
                point_y[i] += speed
            origin_y = (point_y[0] + point_y[1] + point_y[2] + point_y[3])/4
        if pressed[pygame.K_d]: 
            for i in range(0,4):
                point_x[i] += speed
            origin_x = (point_x[0] + point_x[1] + point_x[2] + point_x[3])/4

        # 플레이어 회전
        if pressed[pygame.K_k]:
            for i in range(0,4):
                (point_x[i],point_y[i])=rotation(point_x[i],point_y[i],origin_x,origin_y,dtr(5))
        if pressed[pygame.K_l]:
            for i in range(0,4):
                (point_x[i],point_y[i])=rotation(point_x[i],point_y[i],origin_x,origin_y,dtr(-5))
        a = 1

    # 화면 지우기
    screen.fill((0, 0, 0))
    
    for i in range(0,4):
        pygame.draw.circle(screen,(255,0,0),(point_x[i], point_y[i]),4)

    pygame.draw.circle(screen,(0,255,0),(origin_x, origin_y),4)
    
    pygame.display.flip()
    clock.tick(60)