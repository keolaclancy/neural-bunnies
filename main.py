#!/usr/bin/env python3

import sys
import pygame
import time
from src.display import Display
from src.player import Player
from genetic.genetic import Genetic

# Load classes.
pygame.init()
clock = pygame.time.Clock()
display = Display()

# Create a collection of players.
# Enable or disable genetic selection.
gen = Genetic(display.screen, display.size)

# Optional argument to allow playing.
if len(sys.argv) == 2:
    if sys.argv[1] == 'play':
        gen.toggle_training(False)
else:
    gen.toggle_training(True)

if gen.training_enabled:
    gen.init()

if gen.training_enabled:
    players = gen.pool
else:
    players = [Player(display.height - 30)]

sprites_list = pygame.sprite.Group()

# Run.
while 1:

    # Manage exit event.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # Check for pressed keys.
        if not gen.training_enabled:
            player = players[0]
            if event.type == pygame.KEYDOWN:
                if player.dead:
                    display.reset(player)
                if not player.falling:
                    player.jumping = True

    # For each players (individuals) in the population
    for player in players:

        sprites_list.add(player)

        # When player is alive.
        if not player.dead:

            player.player_jump()
            # Display the background.
            display.show_background()

            # Display player score if not in training
            if not gen.training_enabled:
                display.show_score(player)
            # Display the genetic infos.
            else:
                # Use bunny brain.
                player.score_counter()
                gen.think(player, display)

                # Display genetic data.
                gen.gen_watcher()

            # Check for collisions.
            display.check_collision(player)

        # When all players from the population are dead, end the game.
        if player.dead:

            # Another one bites the dust x_x
            if len(players) > 1:
                player.move_corpse()
                if player.rect.x < -20:
                    players.remove(player)
                    sprites_list.remove(player)

            # Last player died.
            else:
                if gen.training_enabled:
                    display.show_end_screen(player)
                    gen.next_pop()
                    gen.reset_obstacles(display)

                    time.sleep(1)
                else:
                    display.show_end_screen(player)
                    time.sleep(0.5)

    # Show the obstacles.
    display.show_obstacles()
    # Update sprites
    sprites_list.update()

    sprites_list.draw(display.screen)

    # Refresh the display.
    pygame.display.flip()

    clock.tick(60)
    time.sleep(0)

