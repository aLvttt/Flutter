from ursina import *
import time
import random
import win32api
from pynput.keyboard import Key, Controller


game = Ursina()

win32api.LoadKeyboardLayout('00000409', 1)

medians = 100000

player = Entity(model='assets/Spaceship', position=(0, 3, -700), scale=(1, 1, 1), collider='box')
camera.z = -15
camera.add_script(SmoothFollow(target=player, offset=(0, 5, -30)))

rows = [-15, -10, -5, 0, 5, 10, 15]
median_r = Entity(model='cube', collider='box', position=(25, 2, 0), scale=(2, 2, medians), color=color.white33)
median_l = Entity(model='cube', collider='box', position=(-25, 2, 0), scale=(2, 2, medians), color=color.white33)
score_board = Text(text=str(0), scale=1, x=-0.0665, y=-0.45)
speed = 150
speedvar = speed
exit_button = Controller()

scene.fog_density=(0, 700)
scene.fog_color=color.black

music = Audio('assets/Backsound.mp3', loop=True, autoplay=True)
music.play()


def update():
    speed = 150
    speedcount = 0

    player.z = player.z + time.dt * speed
    score_data = player.z + time.dt * (speed // 2) 
    score_val = (score_data + 600) / 100
    score = int(score_val)

    global rows
    if held_keys['d'] or held_keys['right arrow']:
       player.x = player.x + time.dt * 35
       player.rotation_z = player.rotation_z + time.dt * 50

    elif held_keys['a'] or held_keys['left arrow']:
       player.x = player.x - time.dt * 35
       player.rotation_z = player.rotation_z - time.dt * 50    

    elif held_keys['w'] or held_keys['up arrow']:
       player.z = player.z + time.dt * 100

    else:
       player.rotation_z = 0

    if held_keys['escape']:
       destroy(game)

    #if player.intersects().hit or median_r.intersects().hit or median_l.intersects().hit:
       #destroy(game)

    score_board.text = str('Score:') + ' ' + str(score)
 
for i in range(0, medians, 100):
   enemy = Entity(model='cube', collider='box', position=(random.choice(rows), 6, i), color=color.random_color())
   enemy.scale = (7, 7, 7)

window.fullscreen = 1

sky_texture = load_texture('assets/stars.png')
sky = Sky(texture = sky_texture)

game.run()