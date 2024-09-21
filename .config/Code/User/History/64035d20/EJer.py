import os
import json 


#get colors from wallust
def hex_to_rgb(hex_color):
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

with open("/home/sciencerz/.config/neofetch/ansi.json") as ansi:
    ansi = json.load(ansi).values()

def rgb_to_ansi(rgb):
    r,g,b = rgb
    min_dist = 3 * 255**2
    for i,x in enumerate(ansi):
        distance = (r-x[0])**2 + (g-x[1])**2 + (b-x[2])**2
        min_dist = distance if distance < min_dist else min_dist
        ansi = i if distance < min_dist else ansi
    
    return ansi_color_index

with open("/home/sciencerz/.config/neofetch/colors.conf" , "r") as f:
    data = [rgb_to_ansi(hex_to_rgb(x)) for x in json.load(f).values()]
    print(data)

# setting thumbnail
wallpaper_cache="/home/sciencerz/.cache/swww/eDP-1"
default="/home/sciencerz/Documents/Personal/scz.jpg"
home=os.getenv("HOME")

file = next(open(wallpaper_cache)).split('/')[-1]
if os.path.exists(f"{home}/Pictures/Thumbnails/file"):
    os.system(f'wallust run "wallpaper_cache" --palette "dark16" --quite')
    os.system(f"neofetch --kitty '{home}/Pictures/Thumbnails/{file} --colors ({data[12]} {data[12]} {data[12]} {data[12]} {data[12]} {data[12]})'")
else:
   os.system(f"neofetch --kitty '{default}'")
