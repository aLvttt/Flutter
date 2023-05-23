from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

from ursina import *
import time
import random
import win32api
from pynput.keyboard import Key, Controller

game = Ursina()

win32api.LoadKeyboardLayout('00000419', 1)

speedcount = 0 
player = Entity(model='assets/Spaceship', position=(0, 3, -700), scale=(1, 1, 1), collider='box')
camera.z = -15
camera.add_script(SmoothFollow(target=player, offset=(0, 5, -30)))

road = Entity(model='plane', scale=(50, 10, 1000000), color=color.black)
rows = [-15, -10, -5, 0, 5, 10, 15]
median_r = Entity(model='cube', collider='box', position=(25, 2, 0), scale=(5, 10, 1000000), color=color.gray)
median_l = Entity(model='cube', collider='box', position=(-25, 2, 0), scale=(5, 10, 1000000), color=color.gray)
score_board = Text(text=str(0), scale=1, x=-0.0665, y=-0.45)
speed = 150
speedvar = speed
exit_button = Controller()

scene.fog_density=(0, 700)
scene.fog_color=color.white

music = Audio('assets/Backsound.mp3', loop=True, autoplay=True)

def update():
    player.z = player.z + time.dt * speed
    score_val = player.z + 600
    score = int(score_val)

    global rows
    if held_keys['d'] or held_keys['right arrow']:
       player.x = player.x + time.dt * 25
       player.rotation_z = player.rotation_z + time.dt * 50

    if held_keys['a'] or held_keys['left arrow']:
       player.x = player.x - time.dt * 25
       player.rotation_z = player.rotation_z - time.dt * 50    

    if held_keys['w'] or held_keys['up arrow']:
       player.z = player.z + time.dt * 100

    if held_keys['escape']:
       destroy(game)

    if score_val >= 10000:
       player.z = player.z + time.dt * 250

    if player.intersects().hit or median_r.intersects().hit or median_l.intersects().hit:
       destroy(game)

    score_board.text = str('Score:') + ' ' + str(score)
 
def ty():
    if speedcount <= 10000:
        speedcount = speedcount + time.dt
    else:
        speedcount = 0
        speedvar = speedvar + 300

for i in range(0, 100000, 100):
   enemy = Entity(model='cube', collider='box', position=(random.choice(rows), 6, i), color=color.random_color())
   enemy.scale = (7, 10, 10)

def pox():
   root.destroy()


window.fullscreen = 1
sky = Sky()


ttk.Label(frm, text="Главное меню").grid(column=0, row=0)
ttk.Button(frm, text="Новая игра", command=lambda:{game.run(), music.play()}).grid(column=0, row=1)
ttk.Button(frm, text="Настройки", command='').grid(column=0, row=2)
ttk.Button(frm, text="Выход", command=root.destroy).grid(column=0, row=3)

root.mainloop()
