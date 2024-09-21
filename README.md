# My Dot Files For HyprLand
![Version-1.1.0](https://img.shields.io/badge/MyDots-1.1.0-red)


## Version 1

### Features
  - Waybar is customized such that it matches the Wallpaper using Wallust 
  - Kitty Terminal starts with Neofetch, which also automatically adapts to the wallpaper
  - The LockScreen is also customized with a slight blur and full background image
  - the text in the lock screen has a slight tint matching on the wallpaper

  - PNG WALLPAPERS AND THUMBNAILS ONLY
  - THE NAME OF THE WALLPAPER SHOULD MATCH ITS CORRESPONDING NEOFETCH THUMBNAIL

### Demo
![Screenshot_01-Jul_23-51-21_2211](https://github.com/Kazedaa/.MyDots/assets/120291477/c8baa8cf-5230-4bbe-a0de-119931ba4845)

![Screenshot_01-Jul_23-52-15_771](https://github.com/Kazedaa/.MyDots/assets/120291477/47768b49-ae5b-4972-86ce-9cc0e08419cc)

![Screenshot_01-Jul_23-52-46_31189](https://github.com/Kazedaa/.MyDots/assets/120291477/c5a15c5a-e9e1-4b30-a0fe-9e99745b40ac)

![Screenshot_01-Jul_23-53-19_4922](https://github.com/Kazedaa/.MyDots/assets/120291477/0d02b409-025b-4ef3-83dc-3f2991bdaa7e)

![Screenshot_01-Jul_23-53-48_9375](https://github.com/Kazedaa/.MyDots/assets/120291477/3e88d1a3-4b0b-496b-9250-311509db2f48)

![Screenshot_01-Jul_23-56-13_18138](https://github.com/Kazedaa/.MyDots/assets/120291477/baaccbf2-f9ae-4d36-bcce-1bd8ea335787)

![Screenshot_05-Jul_21-29-36_1583](https://github.com/Kazedaa/.MyDots/assets/120291477/4a9f427c-627e-4599-b62b-09412b5b31f6)

![Screenshot_05-Jul_21-30-03_32331](https://github.com/Kazedaa/.MyDots/assets/120291477/1807d86b-3363-4ff3-a7c1-ddb90a8fdb50)

![Screenshot_05-Jul_21-30-18_29427](https://github.com/Kazedaa/.MyDots/assets/120291477/c40dddbd-4ec9-4be5-a19a-41b6de0cd284)


## Version 1.1.0 

### Features
  - Added Spotify
  - Added CAVA
  - Cava color scheme matches the wallpaper
  - Automatically update cava color when wallpaper changes
    
### Demo
![image](https://github.com/user-attachments/assets/cb9e9617-308c-40c0-9109-d474cfd7ef76)

![image](https://github.com/user-attachments/assets/4c31bd3b-8caf-4a80-9c80-7b7b2af385b4)

### SetUp
1. **Check Dependencies**
```bash
  cava -v
  pavucontrol -v
```
2. **Get Dependencies (Ignore if already installed)**
```bash
  sudo apt install cava
  sudo apt install pulseaudio
```
3. **Create AudioSink for Spotify**
```bash
  pactl load-module module-null-sink sink_name=SpotifySink sink_properties=device.description="SpotifySink"
```
4. **Route Spotify to New Sink**
   - Open PulseAudio Volume Control.
    ```bash
      pauvcontrol
    ```
   - Navigate to Playback.
   - Open Spotify in the background and play something for pauvcontrol to recognise is.
   - Change Spotify output to SpotifySink.
5. **Configure CAVA Source**
   - Set source in wallust template and make sure the wallust config has the spotify-cava template.
```ini
  [input]
  method = pulse
  source = SpotifySink.monitor
```
6. **Create Loopback from Sink to Default Output**
```bash
  pactl load-module module-loopback source=SpotifySink.monitor
```

