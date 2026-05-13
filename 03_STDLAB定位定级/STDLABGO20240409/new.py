import pygame
import random

# 初始化pygame
pygame.init()

# 设置窗口大小
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

# 设置颜色
white = (255, 255, 255)
green = (0, 255, 0)
red = (213, 50, 80)

# 设置蛇的初始位置和长度
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_length = len(snake_body)
direction = 'RIGHT'

# 设置食物的初始位置
food_pos = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]

# 设置游戏速度
clock = pygame.time.Clock()

# 游戏主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                direction = 'UP'
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                direction = 'DOWN'
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                direction = 'LEFT'
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                direction = 'RIGHT'

    # 检查蛇是否撞到自己
    if snake_pos in snake_body[:-1]:
        pygame.quit()
        exit()

    # 更新蛇的位置
    head_x = snake_pos[0]
    head_y = snake_pos[1]

    if direction == 'UP':
        head_y -= 10
    if direction == 'DOWN':
        head_y += 10
    if direction == 'LEFT':
        head_x -= 10
    if direction == 'RIGHT':
        head_x += 10

    # 检查蛇是否撞到墙壁
    if head_x < 0 or head_x >= width or head_y < 0 or head_y >= height:
        pygame.quit()
        exit()

    # 检查蛇是否吃到食物
    if snake_pos == food_pos:
        snake_body.append([head_x, head_y])
        food_pos = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]
    else:
        snake_body.pop(0)  # 移动蛇的身体，移除尾部的节点

    # 绘制窗口
    screen.fill(white)
    for pos in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, red, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    pygame.display.flip()  # 更新整个待显示的Surface对象到屏幕上

    # 控制游戏速度
    clock.tick(10)

# pygame.quit()  # 游戏结束时，清理