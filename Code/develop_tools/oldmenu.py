from ursina import *
import win32api
import subprocess

app = Ursina(title='Flutter-Menu')

win32api.LoadKeyboardLayout('00000409', 1)

def play_game():
    subprocess.Popen(["python", "game.py"])
    destroy(MenuMenu)


class MenuMenu(Entity):
   def __init__(self, **kwargs):
       super().__init__(parent=camera.ui, ignore_paused=True)

       self.main_menu = Entity(parent=self, enabled=True)
       self.background = Sky(model = "cube", double_sided = True, texture = Texture("assets/backgroung.png"), rotation = (0, 90, 0))

       Text("Flutter", parent = self.main_menu, y=0.4, x=0, origin=(0,0), color = color.black)

       def switch(menu1, menu2):
           menu1.enable()
           menu2.disable()

       ButtonList(button_dict={
           "Start": Func((play_game)),
           "Settings": Func((print(5))),
           "Exit": Func(lambda: application.quit())
       }, y=00,parent=self.main_menu)

main_menu = MenuMenu()
window.fullscreen = 1
app.run()