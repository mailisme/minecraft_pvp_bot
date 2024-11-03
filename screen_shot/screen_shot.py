import pygetwindow
from PIL import ImageGrab

path = r'C:\Users\jack2\CODE\minecraft_pvp_bot\output\im\a.png'
titles = pygetwindow.getAllTitles()

window = pygetwindow.getWindowsWithTitle('小算盤')[0]
left, top = window.topleft
right, bottom = window.bottomright

im = ImageGrab.grab(bbox = (left+10, top, right-10, bottom-10))
im.save(path)
im.show()