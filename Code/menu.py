from ursina import *
import win32api
import subprocess

app = Ursina(title='Flutter-Menu')

win32api.LoadKeyboardLayout('00000419', 1)

def play_game():
    subprocess.call(["python", "game.py"])

class MenuMenu(Entity):
   def __init__(self, **kwargs):
       super().__init__(parent=camera.ui, ignore_paused=True)

       self.main_menu = Entity(parent=self, enabled=True)
       self.background = Entity(parent=self, color=color.white)

       Text("Flutter", parent = self.main_menu, y=0.4, x=0, origin=(0,0))

       def switch(menu1, menu2):
           menu1.enable()
           menu2.disable()


       ButtonList(button_dict={
           "Start": Func((play_game)),
           "Exit": Func(lambda: application.quit())
       },y=0,parent=self.main_menu)

main_menu = MenuMenu()
window.fullscreen = 0
app.run()