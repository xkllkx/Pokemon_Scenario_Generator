# Pokemon_Scenario_Generator
This repository demonstrates using PIL and OpenCV to create a Pokémon game scenario generator.
The application is divided into two main parts:

### Character Info Edit [^1].
Allows users to edit the character's name and HP.
![image](https://github.com/xkllkx/Pokemon_Scenario_Generator/blob/main/character_info_edit/f_w_model.jpg)![image](https://github.com/xkllkx/Pokemon_Scenario_Generator/blob/main/character_info_edit/f_w.png)

### Animation Generate [^2]
Continues from the first part to progressively generate multiple game scenes and create a game animation.
![animation](https://github.com/xkllkx/Pokemon_Scenario_Generator/blob/main/animation_generate/test.gif)

# Installation
```bash
pip install pillow opencv-python
```

# How to use this repo
## [^1]:Character Info Edit
### User define variable
- Font
```python
font = ImageFont.truetype("Silver.ttf", 60)
```

- Character model pick
```python
im = Image.open("f_w_model.jpg")
```

- Character HP
```python
player1_start_XY = [976,268] # XY # main character HP left-coor
player1_end_XY = [751,268] # left

player2_start_XY = [403,63] # XY # opponent character HP left-coor
player2_end_XY = [180,63] # left

# only player1 need HP num
num_start_XY = [868,279] # left top

player1_full_blood = 20
player1_current_blood = 10

player2_full_blood = 20
player2_current_blood = 15
```

- Output Scenario (png)
```python
im.save("f_w.png","png")
```

### Run T2P_PIL_finish.py to generate single Pokémon game scenario.
```bash
python T2P_PIL_finish.py
```

## [^2]:Animation Generate
### User define variable
- As mentioned above

- animation_fps
```python
picture_num = 50
twinkle_num = 4 # slash on/off * 2

picture_name = 0
```

- output folder
```python
filename = "w_g_bb_2"
```

- slash twice
```python
black = Image.open("black.jpg")
twinkle = 0
```

- animation
```python
size = (1009,348) # image size
print(size)
```

###  Run picture_2_movie_final.py to generate scenarios and Pokémon game Animation.
```bash
python picture_2_movie_final.py
```
