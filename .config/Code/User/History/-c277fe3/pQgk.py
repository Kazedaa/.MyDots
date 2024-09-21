import os
wallpaper_cache="/home/sciencerz/.cache/swww/eDP-1"
command="neofetch --kitty"
default="/home/sciencerz/Documents/Personal/scz.jpg"
home=os.getenv("HOME")
file = open(wallpaper_cache)
print(next(file))