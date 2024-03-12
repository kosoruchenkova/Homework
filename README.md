
#Homework

import pygame  # Import pygame library
import random  # Import random library for random number generation

screen_width = 700  # Set screen width
screen_hight = 700  # Set screen height

pygame.init()  # Initializing the pygame library
screen = pygame.display.set_mode((screen_width, screen_hight))  # Create a window with the specified dimensions
done = False  # Variable to track program termination

number_of_stars = 100  # Total number of stars
speed = 0.5  # The speed of the stars
stars = []  # A list containing stars 

def new_star() -> list:  # Create a function to generate a new star
    star = [random.randint(0, screen_width) - screen_width // 2, random.randint(0, screen_hight) - screen_hight // 2, 256, 0]  # Generation of coordinates and characteristics of a star
    return star  # Return the generated star

for i in range(0, number_of_stars):  # Cycle to create the specified number of stars
    stars.append(new_star())  # Adding a new star to the star list

while not done:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True  

    screen.fill((0, 0, 0))  # Fill the screen with black

    for i in range(0, number_of_stars):  # An all-star cycle
        s = stars[i]  # Memorize the characteristics of the star in the list

        x = s[0] * 256 / s[2] 
        y = s[1] * 256 / s[2] 
        s[2] -= speed  

        if s[2] <= 0 or x <= -screen_width // 2 or x >= screen_width // 2 or y <= -screen_hight // 2 or y >= screen_hight // 2:  # If the star is out of the screen
            s = new_star()  # Generate a new star

        if s[3] < 256:  # If the color has not reached its maximum brightness
            s[3] += 0.15  # Increase the brightness

        if s[3] >= 256:  # If the brightness is greater than allowed
            s[3] = 255  # Set the maximum brightness value

        stars[i] = s  # Update the characteristics of the star in the list

        x = round(s[0] * 256 / s[2]) + screen_width // 2  
        y = round(s[1] * 256 / s[2]) + screen_hight // 2 
        
        colors = '#%02X%02X%02X' % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # Generate a random color

        pygame.draw.circle(screen, colors, (x, y), 3)  # Display a star on the screen using a random color

    pygame.display.flip()  
pygame.quit() # Quit the game

#This code creates a visual effect of starry sky animation, where stars twinkle, move and change their parameters. The purpose of this work can be pedagogical, using animation to teach the Pygame library, new algorithms, or basic computer graphics concepts.




