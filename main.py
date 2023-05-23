import pygame
import random

pygame.init()

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

screen_width = 1000
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Jogo da cobrinha")
pygame.display.update()

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])

def plot_snake(gameWindow, color, snk_list, snake_size):
    for i, (x, y) in enumerate(snk_list):
        if i == 0:
            pygame.draw.rect(gameWindow, red, [x, y, snake_size, snake_size])
        else:
            pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def gameloop():
    exit_game = False
    game_over = False
    snake_x = screen_width / 2
    snake_y = screen_height / 2
    snk_list = []
    snk_length = 1
    x = 45
    y = 55
    velocity_x = 0
    velocity_y = 0
    for i in range(snk_length):
        snk_list.append([x, y])
        x -= 30

    food_x = random.randint(20, screen_width - 20)
    food_y = random.randint(60, screen_height - 20)
    score = 0
    init_velocity = 5
    snake_size = 25
    fps = 60

    while not exit_game:
        if game_over:
            gameWindow.fill(white)
            text_screen("Perdeu Otário! Pressione Enter para Continuar", red, 100, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_q:
                        score += 10

            snake_x += velocity_x
            snake_y += velocity_y

            snake_head = []
            snake_head.append(snake_x)
            snake_head.append(snake_y)
            snk_list.append(snake_head)

            if len(snk_list) > snk_length:
                del snk_list[0]

            if snake_x < 0 or snake_x > screen_width or snake_y < 60 or snake_y > screen_height:
                game_over = True
                # pygame.mixer.music.load()
                # pygame.mixer.music.play()

            if snake_head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load()
                pygame.mixer.music.play()

            if abs(snake_x - food_x) < 15 and abs(snake_y - food_y) < 15:
                score += 10
                food_x = random.randint(20, screen_width - 20)
                food_y = random.randint(60, screen_height - 20)
                snk_length += 5

            gameWindow.fill(white)
            text_screen("Pontuação: " + str(score * 10), red, 5, 5)
            pygame.draw.rect(gameWindow, black, [0, 0, screen_width, 60])
            plot_snake(gameWindow, black, snk_list, snake_size)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()


gameloop()
