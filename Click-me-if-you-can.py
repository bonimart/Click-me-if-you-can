from tkinter import *
import time
import random

root = Tk()

def change_pos(maxx, maxy, btn):
	valx = random.randint(0, maxx)
	valy = random.randint(0, maxy)
	btn.place(x=valx, y=valy)

def try_again(btn, root):
	btn['text'] = 'Try Again'
	btn['command'] = root.destroy

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.title('')
root.configure(bg='black')
root.state('zoomed')
root.overrideredirect(1)
btn = Button(root, text='Click Me', command=lambda: try_again(btn, root), height=1, width=8, font=('Verdana', 12))
btn.place(x=screen_width/2-btn['width'], y=screen_height/2-btn['height'])
maxx = screen_width-11*btn['width']
maxy = screen_height-30*btn['height']

while btn['text']=='Click Me':
	root.update()

time_delta = 0.5
change_pos(maxx, maxy, btn)
now = time.time()
while True:
	try:
		if now+time_delta < time.time():
			change_pos(maxx, maxy, btn)
			now = time.time()
		root.update_idletasks()
		root.update()
	except TclError:
		break
