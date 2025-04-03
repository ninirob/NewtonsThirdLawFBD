# N Roberts

#Discussion Instructions:
# Newton's third law force pair
# Make sure your diagram is correctly labeled and clearly shows that
# the force exerted on one object is equal and opposite to the force applied on the other.
# Provide a brief description that explains the actions of the forces and objects in your pair.

# -------------------------------------------------------------
# Instructions for Running the Code
# -------------------------------------------------------------

# 1. Extract the ZIP file into a folder.
# 2. Ensure that the folder contains:
#    - The Python code file (.py)
#    - An "assets" folder with the following subfolders:
#        - "foot" folder with foot images
#        - "musical_notes"
#        - "bkgrnd" folder
#        - "arrows" folder
# 3. To run the code:
#    - Make sure you have Pygame installed (`pip install pygame`).
#    - Run the Python code using your preferred Python environment.
# 4. If you encounter any issues:
#    - Check that the asset paths in the code match the folder structure.
#    - Ensure that the assets are properly extracted and are in the correct location.
#
# Enjoy the Newton's Third Law animation!


import math
import pygame
import os
import sys
import pygame.freetype

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1000, 600
FOOT_WIDTH, FOOT_HEIGHT = 90, 150
ARROW_UP_SIZE = (60, 150)
ARROW_DOWN_SIZE = (60, 105)

# Set up display window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Newton's Third Law Force Pair Tapping Foot Animation - Nini Roberts")

# Load and scale images
def load_and_scale_image(path, size):
    image = pygame.image.load(path)
    return pygame.transform.scale(image, size)

sky = load_and_scale_image("assets/bkgrnd/sky.png", (WIDTH, HEIGHT))
ground = load_and_scale_image("assets/bkgrnd/ground.png", (WIDTH, 100))
planted_foot = load_and_scale_image("assets/foot/planted_foot.png", (FOOT_WIDTH, FOOT_HEIGHT))
tapping_foot = load_and_scale_image("assets/foot/tapping_foot.png", (100, 150))
arrow_up = load_and_scale_image("assets/arrows/arrow_upFnormal.png", ARROW_UP_SIZE)
arrow_down = load_and_scale_image("assets/arrows/arrow_downFgravity.png", ARROW_DOWN_SIZE)

# Musical notes
note_1 = load_and_scale_image("assets/musical_notes/note_1.png", (30, 30))
note_2 = load_and_scale_image("assets/musical_notes/note_2.png", (30, 30))
note_3 = load_and_scale_image("assets/musical_notes/note_3.png", (30, 30))
note_4 = load_and_scale_image("assets/musical_notes/note_4.png", (30, 30))

# Define initial positions for elements
foot_x, foot_y = 320, 360
note_x_left = foot_x - 150
note_x_right = foot_x + 150

# Variables for tapping foot movement
tapping_offset = 0
tapping_direction = 1
tapping_speed = 3 # 3 looked best but try diff speeds

# Variables for musical note movement
notes = [
    {"image": note_1, "offset": 0, "direction": 1, "speed": 2, "x_pos": note_x_left},
    {"image": note_2, "offset": 0, "direction": -1, "speed": 3, "x_pos": note_x_left},
    {"image": note_3, "offset": 0, "direction": 1, "speed": 1, "x_pos": note_x_left},
    {"image": note_4, "offset": 0, "direction": -1, "speed": 2, "x_pos": note_x_left},
    {"image": note_1, "offset": 0, "direction": 1, "speed": 2, "x_pos": note_x_right},
    {"image": note_2, "offset": 0, "direction": -1, "speed": 3, "x_pos": note_x_right},
    {"image": note_3, "offset": 0, "direction": 1, "speed": 1, "x_pos": note_x_right},
    {"image": note_4, "offset": 0, "direction": -1, "speed": 2, "x_pos": note_x_right}
]

# Initialize fonts
font = pygame.freetype.SysFont("Arial", 20)
equation_font = pygame.freetype.SysFont("Arial", 36)

# Main loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    tapping_offset += tapping_speed * tapping_direction
    if tapping_offset > 30 or tapping_offset < -30:
        tapping_direction *= -1

    for note in notes:
        note["offset"] += note["speed"] * note["direction"]
        if note["offset"] > 50 or note["offset"] < -50:
            note["direction"] *= -1

    # Background
    screen.fill((255, 255, 255))
    screen.blit(sky, (0, 0))
    screen.blit(ground, (0, 500))

    # Title and description
    title_text, title_rect = font.render("Newton's Third Law: Tapping Foot to Music Free Body Diagram", (255, 255, 255))
    description_text, description_rect = font.render(
        "For every action force, there's an equal and opposite reaction force", (255, 255, 255))
    title_rect.center = (WIDTH // 2, 20)
    description_rect.center = (WIDTH // 2, 60)

    screen.blit(title_text, title_rect)
    screen.blit(description_text, description_rect)

    # Newton's Third Law equation (F_12 = -F_21)
    third_law_text, third_law_rect = equation_font.render("F_12 = -F_21", (255, 255, 255))
    third_law_rect.center = (WIDTH // 2, 100)
    screen.blit(third_law_text, third_law_rect)

    # Draw forces (foot images and arrows)
    screen.blit(planted_foot, (foot_x, foot_y))
    screen.blit(tapping_foot, (foot_x + 40, foot_y - 40 + tapping_offset))
    screen.blit(arrow_up, (foot_x + 64, foot_y - 15))
    screen.blit(arrow_down, (foot_x + 64, foot_y + 135))

    # Force labels
    normal_force_text, normal_force_rect = font.render("Fnormal", (255, 255, 255))
    gravity_force_text, gravity_force_rect = font.render("Fgravity", (255, 255, 255))

    screen.blit(normal_force_text, (foot_x + 10, foot_y + 55))
    screen.blit(gravity_force_text, (foot_x + 10, foot_y + 180))

    # Contact point for force interaction
    contact_x = foot_x + 96
    contact_y = foot_y + 139
    pygame.draw.circle(screen, (255, 255, 255), (contact_x, contact_y), 5)

    # Free body diagram description
    description_text = (
        "Object 1: The foot exerts a force on the ground (F_12).\n"
        "Object 2: The ground exerts an equal and opposite force on the foot (F_21).\n"
        "According to Newton's Third Law, these forces are equal in magnitude and opposite in direction."
    )

    description_lines = description_text.split("\n")

    desc_x = foot_x - 205
    desc_y = foot_y - 200

    for line in description_lines:
        line_text, line_rect = font.render(line, (255, 255, 255))
        line_rect.topleft = (desc_x, desc_y)
        screen.blit(line_text, line_rect)
        desc_y += 30

    # Descriptions for Obj 1 & 2
    object_1_desc, object_1_rect = font.render("Object 1(F_1): The foot exerting force", (255, 255, 255))
    object_2_desc, object_2_rect = font.render("Object 2(F_2): The ground receiving the force", (255, 255, 255))

    object_1_rect.center = (foot_x + 305, foot_y + 75)
    object_2_rect.center = (foot_x + 310, foot_y + 160)

    screen.blit(object_1_desc, object_1_rect)
    screen.blit(object_2_desc, object_2_rect)

    # Draw last notes
    for i, note in enumerate(notes):
        screen.blit(note["image"], (note["x_pos"] + (i % 4 * 40), foot_y - 35 + note["offset"]))

    pygame.display.flip()
    clock.tick(60)