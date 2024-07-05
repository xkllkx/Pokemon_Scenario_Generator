from PIL import Image, ImageDraw, ImageFont
import numpy as np
import cv2

# Settings
#W, H = (224, 224)

# Font
font = ImageFont.truetype("Silver.ttf",60)
#font = ImageFont.load_default()

im = Image.open("w_g_model.jpg")
#im=Image.new("RGBA", (500,250),(248,247,216)) # white page

draw = ImageDraw.Draw(im)

def blood_lengh1_decrease(image,start_XY,end_XY,full_blood,current_blood):
    thick=2

    shape = [(end_XY[0] + ((start_XY[0] - end_XY[0]) * (current_blood / full_blood)),end_XY[1]) , (start_XY[0] , start_XY[1]+thick)]  #用扣血的
    ImageDraw.Draw(image).rectangle(shape, fill = (66,62,63))

    shape = [(end_XY[0] + ((start_XY[0] - end_XY[0]) * (current_blood / full_blood)),end_XY[1]+thick) , (start_XY[0] , start_XY[1]+thick*2)]  #用扣血的
    ImageDraw.Draw(image).rectangle(shape, fill = (65,77,67))

    shape = [(end_XY[0] + ((start_XY[0] - end_XY[0]) * (current_blood / full_blood)),end_XY[1]+thick*2) , (start_XY[0] , start_XY[1]+10)]  #用扣血的
    ImageDraw.Draw(image).rectangle(shape, fill = (79,108,86))

def blood_lengh2_decrease(image,start_XY,end_XY,full_blood,current_blood):
    
    thick=2
    shape = [(end_XY[0] + ((start_XY[0] - end_XY[0]) * (current_blood / full_blood)),end_XY[1]) , (start_XY[0] , start_XY[1]+thick)]  #用扣血的
    ImageDraw.Draw(image).rectangle(shape, fill = (66,62,63))

    shape = [(end_XY[0] + ((start_XY[0] - end_XY[0]) * (current_blood / full_blood)),end_XY[1]+thick) , (start_XY[0] , start_XY[1]+thick*2)]  #用扣血的
    ImageDraw.Draw(image).rectangle(shape, fill = (65,77,67))

    shape = [(end_XY[0] + ((start_XY[0] - end_XY[0]) * (current_blood / full_blood)),end_XY[1]+thick*2) , (start_XY[0] , start_XY[1]+8)]  #用扣血的
    ImageDraw.Draw(image).rectangle(shape, fill = (79,108,86))

def blood_num(image,start_XY,full_blood,current_blood,font):
    ImageDraw.Draw(image).text((start_XY[0],start_XY[1]), f'{current_blood}/ {full_blood}' ,(71,68,53), font=font,align = "left")


player1_start_XY = [976,268] # XY # main character HP left-coor
player1_end_XY = [751,268] # left

player2_start_XY = [403,63] # XY # opponent character HP left-coor
player2_end_XY = [180,63] # left

num_start_XY = [868,279] # left top

# HP
player1_full_blood = 20
player1_current_blood = 10

player2_full_blood = 20
player2_current_blood = 10

blood_lengh1_decrease(im,player1_start_XY,player1_end_XY,player1_full_blood,player1_current_blood)
blood_lengh2_decrease(im,player2_start_XY,player2_end_XY,player2_full_blood,player2_current_blood)

# animation_fps
picture_num = 50
twinkle_num = 4 # slash on/off * 2

picture_name = 0

# folder name
filename = "w_g_bb_2"

# slash twice
black = Image.open("black.jpg")
twinkle = 0

while twinkle <= twinkle_num:
    stay = 5 # wait in 5 seconds
    if twinkle % 2 != 0:
        for j in range(stay):
            black.save(f"{filename[0:3]}/{filename}/{picture_name}.png","png")
            picture_name+=1
        twinkle+=1
    else:
        for j in range(stay):
            im.save(f"{filename[0:3]}/{filename}/{picture_name}.png","png")
            picture_name+=1
        twinkle+=1


# -HP
player1_current_blood = 0
# player2_current_blood = 10

blood_num(im,num_start_XY,player1_full_blood,player1_current_blood,font)

i = 0
while i <= picture_num:
    player1_blood_decrease = (player1_full_blood - player1_current_blood)/picture_num
    # player2_blood_decrease = (player2_full_blood - player2_current_blood)/picture_num

    blood_lengh1_decrease(im,player1_start_XY,player1_end_XY,player1_full_blood,player1_full_blood-player1_blood_decrease*i)
    # blood_lengh2_decrease(im,player2_start_XY,player2_end_XY,player2_full_blood,player2_full_blood-player2_blood_decrease*i)

    im.save(f"{filename[0:3]}/{filename}/{picture_name+i}.png","png")
    i+=1
    # im.show()

# final picture
picture_name = picture_name+i
for j in range(stay):
    im.save(f"{filename[0:3]}/{filename}/{picture_name}.png","png")
    picture_name+=1

# animation
size = (1009,348) # image size
print(size)

# Complete the creation of the write object.
videowrite = cv2.VideoWriter(f'{filename[0:3]}/{filename}/test.mp4',-1,20,size) # animation name, encoder(-1:default), animation_fps, image size
img_array=[]

for filename in [f'{filename[0:3]}/{filename}/{k}.png' for k in range(picture_name)]:
    img = cv2.imread(filename)
    if img is None:
        print(filename + " is error!")
        continue
    img_array.append(img)

for k in range(picture_name):
    videowrite.write(img_array[k])
print('end!')