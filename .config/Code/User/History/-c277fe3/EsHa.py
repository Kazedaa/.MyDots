import os
wallpaper_cache="/home/sciencerz/.cache/swww/eDP-1"
default="/home/sciencerz/Documents/Personal/scz.jpg"
home=os.getenv("HOME")
file = next(open(wallpaper_cache))
if os.path.exists(f"{home}/Pictures/Thumbnails"):
    print("exists")