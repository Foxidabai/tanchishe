import pygame
import random
import sys
import os

# 游戏窗口大小
WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20

# 颜色定义
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN1 = (0, 200, 0)
GREEN2 = (0, 255, 100)
ORANGE = (255, 140, 0)
RED = (255, 0, 0)
SCORE_BG = (30, 30, 30, 180)  # 半透明背景

# 初始化pygame
pygame.init()
pygame.font.init()  # 强制初始化字体模块
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('贪吃蛇')
clock = pygame.time.Clock() # Keep clock for tick

# 强制使用本地 NotoSansSC-VariableFont_wght.ttf 字体
FONT_PATH = 'NotoSansSC-VariableFont_wght.ttf'
try:
    font = pygame.font.Font(FONT_PATH, 25)
    game_over_font = pygame.font.Font(FONT_PATH, 40)
except Exception as e:
    print('字体加载失败，使用默认字体！', e)
    font = pygame.font.Font(None, 25)
    game_over_font = pygame.font.Font(None, 40)

# 字体渲染测试，保存为图片
try:
    test_surface = font.render('字体测试 Font Test', True, (255,255,255))
    pygame.image.save(test_surface, 'font_test.png')
except Exception as e:
    print('字体渲染异常:', e)

# 贴图加载（若不存在则为None）
def load_image(filename):
    if os.path.exists(filename):
        img = pygame.image.load(filename).convert_alpha()
        return pygame.transform.smoothscale(img, (BLOCK_SIZE, BLOCK_SIZE))
    return None

snake_head_img = load_image('snake_head.png')
snake_body_img = load_image('snake_body.png')

def draw_gradient_bg():
    for y in range(HEIGHT):
        color = (
            30 + int(70 * y / HEIGHT),
            30 + int(120 * y / HEIGHT),
            60 + int(100 * y / HEIGHT)
        )
        pygame.draw.line(window, color, (0, y), (WIDTH, y))

# 画蛇（支持贴图，自动回退）
def draw_snake(snake, direction):
    HEAD_COLOR = (0, 180, 0)
    BODY_COLOR = (0, 255, 0)
    for i, (x, y) in enumerate(snake):
        color = HEAD_COLOR if i == 0 else BODY_COLOR
        rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(window, color, rect)

def draw_food(pos):
    center = (pos[0] + BLOCK_SIZE // 2, pos[1] + BLOCK_SIZE // 2)
    pygame.draw.circle(window, ORANGE, center, BLOCK_SIZE // 2 - 2)
    pygame.draw.circle(window, WHITE, (center[0] - 3, center[1] - 3), 4)

def random_food(snake):
    while True:
        x = random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        if (x, y) not in snake:
            return (x, y)

def main():
    snake = [(100, 100), (80, 100), (60, 100)]
    direction = 'RIGHT'
    change_to = direction
    food = random_food(snake)
    score = 0
    running = True
    speed = 8  # 初始速度较慢

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != 'DOWN':
                    change_to = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    change_to = 'DOWN'
                elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                    change_to = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    change_to = 'RIGHT'

        direction = change_to
        head_x, head_y = snake[0]
        if direction == 'UP':
            head_y -= BLOCK_SIZE
        elif direction == 'DOWN':
            head_y += BLOCK_SIZE
        elif direction == 'LEFT':
            head_x -= BLOCK_SIZE
        elif direction == 'RIGHT':
            head_x += BLOCK_SIZE
        new_head = (head_x, head_y)

        # 检查碰撞
        if (
            head_x < 0 or head_x >= WIDTH or
            head_y < 0 or head_y >= HEIGHT or
            new_head in snake
        ):
            running = False
            break

        snake.insert(0, new_head)
        if new_head == food:
            score += 1
            food = random_food(snake)
            speed += 0.5  # 吃到食物加速
        else:
            snake.pop()

        # 在窗口标题栏显示分数
        pygame.display.set_caption(f'贪吃蛇 | 得分: {score}')
        # 绘制渐变背景
        draw_gradient_bg()
        # 绘制蛇（支持贴图）
        draw_snake(snake, direction)
        # 绘制食物
        draw_food(food)
        # 绘制分数栏
        score_text = font.render(f'得分: {score}', True, WHITE)
        score_bg_rect = pygame.Surface((140, 40), pygame.SRCALPHA)
        score_bg_rect.fill(SCORE_BG)
        window.blit(score_bg_rect, (10, 10))
        window.blit(score_text, (25, 18))
        pygame.display.flip()
        clock.tick(speed)

    # 游戏结束界面美化
    draw_gradient_bg()
    game_over_text = game_over_font.render('游戏结束!', True, RED)
    score_text = font.render(f'最终得分: {score}', True, WHITE)
    tip_text = font.render('按任意键退出', True, (200, 200, 200))
    window.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 60))
    window.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2))
    window.blit(tip_text, (WIDTH // 2 - tip_text.get_width() // 2, HEIGHT // 2 + 40))
    pygame.display.flip()
    wait_for_exit()

def wait_for_exit():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                pygame.quit()
                sys.exit()

if __name__ == '__main__':
    main() 