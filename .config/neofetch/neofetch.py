import os
import json 
home=os.getenv("HOME")

#get colors from wallust
def hex_to_rgb(hex_color):
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

with open(f"{home}/.config/neofetch/ansi.json") as ansi:
    ansi = json.load(ansi).values()

def rgb_to_ansi(rgb):
    r,g,b = rgb
    min_dist = 3*(255**2)
    ansi_color=12
    for i,x in enumerate(ansi):
        distance = ((r-x[0])**2 + (g-x[1])**2 + (b-x[2])**2)**0.5
        ansi_color = i if distance < min_dist else ansi_color
        min_dist = distance if distance < min_dist else min_dist
    
    return ansi_color + 16

with open(f"{home}/.config/neofetch/colors.conf" , "r") as f:
    colors = [rgb_to_ansi(hex_to_rgb(x)) for x in json.load(f).values()]

# setting thumbnail
wallpaper_cache=f"{home}/.cache/swww/eDP-1"
default=f"{home}/Documents/Personal/scz.jpg"

file = next(open(wallpaper_cache)).split('/')[-1]
if os.path.exists(f"{home}/Pictures/Thumbnails/{file}"):
    os.system(f"neofetch --kitty --source '{home}/Pictures/Thumbnails/{file}' --colors '{colors[4]}' '231' '0' '{colors[5]}' '0' '{colors[3]}'")
else:
   os.system(f"neofetch --kitty '{default}' --colors '{colors[4]}' '231' '0' '{colors[5]}' '0' '{colors[3]}'")
