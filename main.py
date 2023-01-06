from asyncio.windows_events import NULL
from pickle import TRUE
from random import choice
from tracemalloc import start
import pygame
from sys import exit
from background import Background
from button import ButtonFactory
from enemy import BulletEnemy, EnemyFactory
from explosion import Explosion
from player import Player
from bullet import Bullet
from life import Life
from life import LivesContainer
from popup import HiscorePopup, PausePopup
from score import Score
from score_table import ScoreTable
from starfield import Starfield
from title_card import TitleCard

def main():

    # Game Variables
    pygame.init()
    screen = pygame.display.set_mode((900, 400))
    pygame.display.set_caption('Space Guy: Blockade')
    clock = pygame.time.Clock()
    starting_lives = 2

    # Game Screen Constants
    TITLE_SCENE = 1
    GAME_SCENE = 2
    HIGHSCORE_SCENE = 3

    current_scene = TITLE_SCENE

    # Custom Events
    transition_to_title = pygame.USEREVENT + 1
    transition_to_game = pygame.USEREVENT + 2
    transition_to_hiscore = pygame.USEREVENT + 3
    bullet_timer = pygame.USEREVENT + 4
    enemy_timer = pygame.USEREVENT + 5
    player_respawn_timer = pygame.USEREVENT + 6
    player_iframes_timer = pygame.USEREVENT + 7
    text_flicker = pygame.USEREVENT + 8

    # Timers
    pygame.time.set_timer(bullet_timer, 120)
    pygame.time.set_timer(enemy_timer, 1000)
    pygame.time.set_timer(text_flicker, 400)

    # Utility Objects
    button_factory = ButtonFactory()
    enemy_factory = EnemyFactory()
    score_table = ScoreTable()

    # Scene Music
    game_scene_music = pygame.mixer.Sound('sounds/game_scene_music.wav')

    # Groups
    
    # Background Group
    bg = pygame.sprite.Group()
    bg.add(Background())
    starfield = pygame.sprite.Group()

    # Title Card Group
    title = pygame.sprite.Group()
    title.add(TitleCard('SPACE GUY: BLOCKADE', 450, 100))

    # Button Group
    buttons = pygame.sprite.Group()
    buttons.add(button_factory.create_button('start', 450, 250))
    buttons.add(button_factory.create_button('hiscore', 450, 275))
    buttons.add(button_factory.create_button('quit', 450, 300))

    # Player Group
    player = pygame.sprite.GroupSingle()
    playerExplodeGroup = pygame.sprite.GroupSingle()

    # Bullet Group
    bullets = pygame.sprite.Group()

    # Enemy Group
    enemies = pygame.sprite.Group()

    # Lives Group
    lives = LivesContainer()

    # Score Group
    score = pygame.sprite.GroupSingle()
    score.add(Score())

    # Popup Group
    initialsPopup = pygame.sprite.GroupSingle()
    pausePopup = pygame.sprite.GroupSingle()

    # Game Loop
    while True:

        # Event Loop
        for event in pygame.event.get():
            
            # Quit
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            # Mouse Events
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.rect.collidepoint(pygame.mouse.get_pos()):
                        button.on_down()
            if event.type == pygame.MOUSEBUTTONUP:
                for button in buttons:
                    if button.rect.collidepoint(pygame.mouse.get_pos()):
                        button.on_up()
            if event.type == pygame.MOUSEMOTION:
                for button in buttons:
                    if button.rect.collidepoint(pygame.mouse.get_pos()):
                        button.on_over()
                    else: button.on_up()

            # Keyboard Events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if initialsPopup.sprite != None:
                        char = ord(initialsPopup.sprite.target.text[0])
                        char += 1
                        initialsPopup.sprite.target.text = chr(char)
                        initialsPopup.update()
                        initialsPopup.draw(screen)
                if event.key == pygame.K_DOWN:
                    if initialsPopup.sprite != None:
                        char = ord(initialsPopup.sprite.target.text[0])
                        char -= 1
                        initialsPopup.sprite.target.text = chr(char)
                        initialsPopup.update()
                        initialsPopup.draw(screen)
                if event.key == pygame.K_RETURN:
                    if initialsPopup.sprite != None:
                        if initialsPopup.sprite.target == initialsPopup.sprite.init1:
                            initialsPopup.sprite.target.alpha = 255
                            initialsPopup.sprite.target = initialsPopup.sprite.init2
                            initialsPopup.update()
                            initialsPopup.draw(screen)
                        elif initialsPopup.sprite.target == initialsPopup.sprite.init2:
                            initialsPopup.sprite.target.alpha = 255
                            initialsPopup.sprite.target = initialsPopup.sprite.init3
                            initialsPopup.update()
                            initialsPopup.draw(screen)
                        elif initialsPopup.sprite.target == initialsPopup.sprite.init3:
                            initialsPopup.sprite.target.alpha = 255
                            initials = initialsPopup.sprite.init1.text + initialsPopup.sprite.init2.text + initialsPopup.sprite.init3.text
                            score_table.insertNewScore(initials, score.sprite.score)
                            initialsPopup.empty()
                            score_table.populate()
                            score_table.draw(screen)
                if event.key == pygame.K_BACKSPACE:
                    if initialsPopup.sprite != None:
                        if initialsPopup.sprite.target == initialsPopup.sprite.init2:
                            initialsPopup.sprite.target = initialsPopup.sprite.init1
                            initialsPopup.update()
                            initialsPopup.draw(screen)
                        elif initialsPopup.sprite.target == initialsPopup.sprite.init3:
                            initialsPopup.sprite.target = initialsPopup.sprite.init2
                            initialsPopup.update()
                            initialsPopup.draw(screen)
                if event.key == pygame.K_ESCAPE:
                    if current_scene == GAME_SCENE:
                        if pausePopup.sprite:
                            pausePopup.empty()
                        else:
                            pausePopup.add(PausePopup(buttons, 450, 200))
                            pausePopup.update()
                            pausePopup.draw(screen)

            # Fire Bullets 
            if event.type == bullet_timer:
                if current_scene == GAME_SCENE and player.sprite != None:
                    if pygame.mouse.get_pressed(3) == (True, False, False):
                        bullets.add(Bullet(player.sprite))

            # Spawn Enemies
            if event.type == enemy_timer:
                if current_scene == GAME_SCENE and player.sprite != None and pausePopup.sprite == None:
                    enemies.add(enemy_factory.create_enemy(choice(['basic', 'shooter', 'swerve']), choice([100, 200, 300, 400, 500, 600, 700, 800]), -100))
                    print('enemy created')

            # Respawn Player
            if event.type == player_respawn_timer:
                if current_scene == GAME_SCENE and player.sprite == None:
                    player.add(Player())

            # Flicker Text
            if event.type == text_flicker:
                if initialsPopup.sprite != None:
                    initialsPopup.sprite.target.toggleTransparency()
                    initialsPopup.update()
                    initialsPopup.draw(screen)

            # Scene Transition Events
            if event.type == transition_to_title:
                # Change the scene
                current_scene = TITLE_SCENE

                # Empty Sprite Groups
                bg.empty()
                buttons.empty()
                player.empty()
                bullets.empty()
                enemies.empty()
                title.empty()
                starfield.empty()

                # Add Scene Sprites to Groups
                bg.add(Background())
                buttons.add(button_factory.create_button('start', 450, 250))
                buttons.add(button_factory.create_button('hiscore', 450, 275))
                buttons.add(button_factory.create_button('quit', 450, 300))
                title.add(TitleCard('SPACE GUY: BLOCKADE', 450, 100))

                # Show Mouse
                pygame.mouse.set_visible(True)

                # Stop Music
                game_scene_music.stop()

                # Play BG Music

            if event.type == transition_to_game:
                # Change the scene
                current_scene = GAME_SCENE

                # Empty Sprite Groups
                bg.empty()
                buttons.empty()
                player.empty()
                bullets.empty()
                enemies.empty()
                title.empty()
                pausePopup.empty()
                starfield.empty()

                # Add Scene Sprites to Groups
                bg.add(Background())
                starfield.add(Starfield())
                player.add(Player())
                
                life_counter = 0
                while life_counter < starting_lives:
                    lives.add(Life())
                    life_counter += 1

                score.add(Score())

                # Hide Mouse
                pygame.mouse.set_visible(False)

                # Stop Music
                
                # Play BG Music
                game_scene_music.set_volume(0.2)
                game_scene_music.play(-1)

            if event.type == transition_to_hiscore:
                # Change the scene
                current_scene = HIGHSCORE_SCENE

                # Empty Sprite Groups
                bg.empty()
                buttons.empty()
                player.empty()
                bullets.empty()
                enemies.empty()
                title.empty()
                starfield.empty()

                # Add Scene Sprites to Groups
                bg.add(Background())
                buttons.add(button_factory.create_button('back', 450, 375))
                
                # Draw Title Card
                title.add(TitleCard('HIGH SCORES', 450, 25))

                # Update Scores
                score_table.populate()

                # Check for HiScore
                if score_table.isHiscore(score.sprite.score):
                    initialsPopup.add(HiscorePopup(450,200))

                # Show Mouse
                pygame.mouse.set_visible(True)

                # Stop Music
                game_scene_music.stop()

                # Play BG Music

        # Update Current Scene
        if current_scene == TITLE_SCENE:
            # Draw Background
            bg.update()
            bg.draw(screen)

            # Draw Title Card
            title.draw(screen)

            # Draw Buttons
            buttons.draw(screen)

        elif current_scene == GAME_SCENE:
            # Break if Game is Paused
            if pausePopup.sprite != None:
                pausePopup.update()
                pausePopup.sprite.contents.draw(screen)
                pygame.mouse.set_visible(True)
                pygame.display.update()
                clock.tick(60)
                continue
            else:
                pygame.mouse.set_visible(False)

            # Draw Background
            bg.update()
            bg.draw(screen)
            
            starfield.update()
            starfield.draw(screen)

            # Draw Lives
            lives.draw(screen)
            lives.update()

            # Draw Score
            score.draw(screen)
            score.update()

            # Draw Player
            player.draw(screen)
            player.update()
            playerExplodeGroup.draw(screen)
            playerExplodeGroup.update()

            # Draw Enemies
            enemies.draw(screen)
            enemies.update()

            # Draw Bullets
            bullets.draw(screen)
            bullets.update()

            # Collisions
            for bullet in bullets:
                enemies_hit = pygame.sprite.spritecollide(bullet, enemies, False)
                for enemy in enemies_hit:
                    enemy.on_hit()
                    if enemy.hitPoints <= 0:
                        score.sprite.increment_score(enemy.points)
                    if type(enemy) != BulletEnemy and type(enemy) != Explosion:
                        bullet.kill()

            if player.sprite:
                if pygame.sprite.spritecollide(player.sprite, enemies, False):
                    playerExplodeGroup.add(Explosion(player.sprite.rect.centerx, player.sprite.rect.centery))
                    player.sprite.on_hit()
                    if lives.sprites():
                        lives.remove(lives.sprites()[0])
                        pygame.time.set_timer(player_respawn_timer, 3000, 1)
                    else:
                        pygame.event.post(pygame.event.Event(transition_to_hiscore))

        elif current_scene == HIGHSCORE_SCENE:
            # Draw Background
            bg.update()
            bg.draw(screen)

            # Draw Title Card
            title.draw(screen)

            # Draw Table
            score_table.draw(screen)

            # Draw Popup
            if initialsPopup.sprite != None:
                initialsPopup.update()
                initialsPopup.sprite.contents.draw(screen)

            # Draw Buttons
            buttons.draw(screen)

        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__': main()