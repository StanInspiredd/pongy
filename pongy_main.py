# Pongy
# A simple pong game with realistic physics and AI
#
# Made using my own code and some of chatgpts for the creater of Pongys (Me) benefit and learning
#
# This is NOT A professional Pong game or professional game at all for that matter ok ty bye
#
# The code in this will be setout in an easy to understand way, should other python beginners wish to use this in their own games.
#
# Released under the GNU General Public License

version = "0.1"  # This is purely for source code to assign versions, it doesn't hold any actual importance xx

# Importation of the pygame and sys libraries
import pygame
import sys

# Pygame initialization (because yes)
pygame.init()

# This bit makes the window n all
WIDTH, HEIGHT = 800, 600  # Change the values of this to whatever you want, will change screen size
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Only change if you know what you're doing!
pygame.display.set_caption("Pongy 0.1")  # Changes the window name

# Paddle properties
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 100

# Paddle positions
left_paddle = pygame.Rect(30, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)  # Left paddle
right_paddle = pygame.Rect(WIDTH - 30 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)  # Right paddle

# Ball properties
BALL_SIZE = 20
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)  # Ball position
ball_speed_x = 5  # Speed of the ball in the x-direction (horizontal)
ball_speed_y = 5  # Speed of the ball in the y-direction (vertical)

# Game loop (aka actual game)
while True:
    screen.fill((0, 0, 0))  # Fill the screen with black (background)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # This quits Pygame so you have no more pygame
            sys.exit()  # This one actually closes the software after you leave because it doesn't do that naturally for some bizarre reason

    # Paddle movement
    keys = pygame.key.get_pressed()  # Get a list of all the keys being pressed

    # Left paddle controls (W and S keys)
    if keys[pygame.K_w] and left_paddle.top > 0:  # If W is pressed and the paddle is not at the top
        left_paddle.y -= 10  # Move the left paddle up
    if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:  # If S is pressed and the paddle is not at the bottom
        left_paddle.y += 10  # Move the left paddle down

    # Right paddle controls (Up and Down arrow keys)
    if keys[pygame.K_UP] and right_paddle.top > 0:  # If the Up arrow is pressed and the paddle is not at the top
        right_paddle.y -= 10  # Move the right paddle up
    if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:  # If the Down arrow is pressed and the paddle is not at the bottom
        right_paddle.y += 10  # Move the right paddle down

    # Ball movement
    ball.x += ball_speed_x  # Update ball's position horizontally
    ball.y += ball_speed_y  # Update ball's position vertically

    # Ball collision with top and bottom of the screen
    if ball.top <= 0 or ball.bottom >= HEIGHT:  # If the ball hits the top or bottom
        ball_speed_y = -ball_speed_y  # Reverse the vertical direction of the ball

    # Ball collision with paddles
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):  # If the ball collides with a paddle
        ball_speed_x = -ball_speed_x  # Reverse the horizontal direction of the ball

    # Ball goes off the left or right side (reset ball)
    if ball.left <= 0 or ball.right >= WIDTH:
        ball.x = WIDTH // 2 - BALL_SIZE // 2  # Reset the ball to the center
        ball.y = HEIGHT // 2 - BALL_SIZE // 2
        ball_speed_x = -ball_speed_x  # Change ball direction after reset

    # Draw paddles and ball
    pygame.draw.rect(screen, (255, 255, 255), left_paddle)  # Draw the left paddle in white
    pygame.draw.rect(screen, (255, 255, 255), right_paddle)  # Draw the right paddle in white
    pygame.draw.ellipse(screen, (255, 255, 255), ball)  # Draw the ball in white

    pygame.display.flip()  # Update the display
