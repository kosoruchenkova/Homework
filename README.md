# Lab. work Kosoruchenkova E.A.
##  Purpose of the work: 
To create an animation of stars moving on the screen. Each star changes coordinates and brightness to create the effect of movement and color change
## Code
## Preparation
>Firstly we need to install the necessary library and module to make our program work:
```
import pygame  # Import pygame library
import random  # Import random library for random number generation
```
>Set the height and width of the screen where the stars will be displayed. You can try entering different sizes to see how it works:
```
screen_width = 700  # Set screen width
screen_hight = 700  # Set screen height
```
>Сreate a window in which our stars will be reproduced:
```
pygame.init()  # Initializing the pygame library
screen = pygame.display.set_mode((screen_width, screen_hight))  # Create a window with the specified dimensions
done = False  # Variable to track program termination
```
>Choosing the data for varaibales. A list was chosen to store star information because dictionaries are inconvenient to invoke keys in, and you can't add items to a tuple, nor can you modify or delete them once created:
```
number_of_stars = 100  # Total number of stars
speed = 0.5  # The speed of the stars
stars = []  # A list containing stars 
```
## Generating stars
```
def new_star() -> list:  # Create a function to generate a new star
    star = [random.randint(0, screen_width) - screen_width // 2, random.randint(0, screen_hight) - screen_hight // 2, 256, 0]  # Generation of coordinates and characteristics of a star
    return star  
```
```
for i in range(0, number_of_stars):  # Cycle to create the specified number of stars
    stars.append(new_star())  # Adding a new star to the star list

while not done:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True  


    screen.fill((0, 0, 0))  # Fill the screen with black
```
>This code is a loop that goes through all the stars in the list and updates their characteristics. For each star, its coordinates are scaled according to its size, and its size is reduced by a given speed. If a star goes off-screen or its size becomes less than zero, a new star is created. Also, the color of the star is increased by 0.15 until it reaches the maximum value (255):
```
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
```
```
        stars[i] = s  # Update the characteristics of the star in the list
```
> Calculate the coordinates using the formulas from the lecture:
```
        x = round(s[0] * 256 / s[2]) + screen_width // 2  
        y = round(s[1] * 256 / s[2]) + screen_hight // 2
```
## Changing the color of the stars
>This code generates a random color for the star. It uses the random.randint() function to generate three random numbers between 0 and 255, which are then converted to hexadecimal format using a format string. This color is then used to draw a star on the screen using pygame.draw.circle():
```
        colors = '#%02X%02X%02X' % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # Generate a random color

        pygame.draw.circle(screen, colors, (x, y), 3)  # Display a star on the screen using a random color
```
## Finalization
>This code updates the screen to display any changes made to the current frame, and then closes the game window and terminates the Pygame library:
```
    pygame.display.flip()  
pygame.quit() 
```
## Conclusion
This code creates a visual effect of starry sky animation, where stars twinkle, move and change their parameters. The purpose of this work can be pedagogical, using animation to teach the Pygame library, new algorithms, or basic computer graphics concepts. Also a "unique feature" of the work was also created, the README.md file was prepared.




