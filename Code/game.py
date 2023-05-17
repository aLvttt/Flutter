from ursina import *
import time
import random
import pyautogui
import win32api

game = Ursina()

win32api.LoadKeyboardLayout('00000419', 1)

player = Entity(model='assets/ship', position=(0, 3, -1000), scale=(2, 2, 2), collider='box')
camera.z = -15
camera.add_script(SmoothFollow(target=player, offset=(0, 5, -30)))

road = Entity(model='plane', scale=(50, 10, 1000000), color=color.black)
rows = [-15, -10, -5, 0, 5, 10, 15]
median_r = Entity(model='cube', collider='box', position=(25, 2, 0), scale=(5, 10, 1000000), color=color.gray)
median_l = Entity(model='cube', collider='box', position=(-25, 2, 0), scale=(5, 10, 1000000), color=color.gray)
score_board = Text(text=str(0), scale=1, x=-0.0665, y=-0.45)
speed = 150

scene.fog_density=(0, 700)
scene.fog_color=color.white

music = Audio('assets/Backsound.mp3', loop=True, autoplay=True)
music.play()

def update():
   player.z = player.z + time.dt * speed
   score_val = player.z + 600
   score = int(score_val)

   global rows
   if held_keys['d']:
       player.x = player.x + time.dt * 25
       player.rotation_z = player.rotation_z + time.dt * 50

   if held_keys['a']:
       player.x = player.x - time.dt * 25
       player.rotation_z = player.rotation_z - time.dt * 50    

   if held_keys['waaaa']:
       player.z = player.z + time.dt * 1000
       player.rotation_x = player.rotation_x + time.dt * 600

   if player.intersects().hit or median_r.intersects().hit or median_l.intersects().hit:
       destroy(game)

   score_board.text = str('Score:') + ' ' + str(score)


for i in range(0, 100000, 100):
   enemy = Entity(model='cube', collider='box', position=(random.choice(rows), 6, i), color=color.random_color())
   enemy.scale = (7, 10, 10)

window.fullscreen = 1
sky = Sky()
game.run()