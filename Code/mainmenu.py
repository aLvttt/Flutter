from ursina import *
import win32api
import subprocess

app = Ursina()

win32api.LoadKeyboardLayout('00000409', 1)

#music = Audio('assets/Space.mp3', loop=True, autoplay=True)
#music.play()

Text.size = .020

Text("Flutter", y=0.1, origin=(0,0), color = color.black, font='VeraMono.ttf')

def settings_warning():
    Text("Sorry, it's not working yet", y=-0.2, origin=(0,0), color = color.black, font='VeraMono.ttf')

def start_game():
    subprocess.Popen(["python", "game.py"])
    quit('mainmenu.py')

Text.size = .015

background = Sky(model = "cube", double_sided = True, texture = Texture("assets/backgroung.png"), rotation = (0, 90, 0))

button_dict = {}
buttons = ButtonList(button_dict, button_height=1.5, width=.3, font='VeraMono.ttf', y=00)
buttons.button_dict = {
    "Start": Func(start_game),
    "Settings": Func(settings_warning),
    "Quit": Func(lambda: application.quit())
}

def update():
    if held_keys['escape']:
       quit()

window.fullscreen = 1
app.run()
