# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define dev = False

define e = Character("Eileen")

default firstShowed = True

default c = 0

default failExamin = False

# Train 1
default train1_examine = -1
default train1_cloth = False
default train1_string = False
default train1_burnString = False
default train1_key = False
default train1_key_popped = False
default train1_bone = False

# Train 2
default first_train2 = True
default train2_examine = -1
default train2_string = False
default train2_burnString = False
default train2_box = False
default train2_box_popped = False
default train2_unlock =False

# Train 3
default train3_burnString = False

# String
default string_number = 0

# Text Index
default text_i = 0

# The game starts here.

label start:
    stop sound

    $string_number = 0

    # Train1
    $train1_examine = -1
    $train1_cloth = False
    $train1_string = False
    $train1_burnString = False
    $train1_key = False
    $train1_key_popped = False
    $train1_bone = False

    $train1_examine0 = False
    $train1_examine1 = False
    $train1_examine_window = False
    $train1_examine_string = True
    $train1_examine_burnString = False
    $train1_examine_bone = False

    $fi_train1_examine_burnString = 0
    $fi_train1_examine_bone = 0
    $fi_train1_examine0 = 0
    $fi_train1_examine1 = 0
    $fi_train1_examine_string = 0

    # Train2
    $first_train2 = True
    $train2_examine = -1
    $train2_string = False
    $train2_burnString = False
    $train2_box = False
    $train2_box_popped = False
    $train2_unlock =False

    $train2_examine0 = False
    $train2_examine1 = False
    $train2_examine2 = False
    $train2_examine_string = False
    $train2_examine_train = False
    $train2_examine_burngString = False
    $train2_examine_ske0 = True
    $train2_examine_ske1 = True
    $train2_examine_ske2 = True
    $train2_examine_ske_bs = False
    $train2_examine_box = False

    $fi_first_train2 = 0
    $fi_train2_examine_string = 0
    $fi_train2_examine_burngString = 0
    $fi_train2_examine_ske1 = 0
    $fi_train2_examine_ske2 = 0
    $fi_trani2_examine_ske_bs = 0

    # Else
    $string_number = 0
    $text_i = 0

    jump intro

label intro:
    stop sound
    play music 'music/bgm1.mp3'

    $firstShowed = True

    $bar_xoffset = 0
    $global_xoffset = 0
    $curr_mouse_xpos = 150
    $curr_player_xpos = curr_mouse_xpos
    $tar_player_xpos = curr_mouse_xpos

    call screen intro()

    '站在锈迹斑斑的列车轨道中央，这里空无一物。'
    '\"我怎么会在这里，看了看手中的绳子。\"'
    '\"这火车上还有人吗？\"'

    jump train1

label train1:
    stop sound

    $firstShowed = True

    jump _train1

label _train1():
    stop sound
    if failExamin:
        "摸索失败"
    call screen train1()

    if _return == 2:
        $text_i = 0
        if first_train2:
            jump train2
        else:
            jump _train2

label train1_choice:
    stop sound
    if train1_examine >= 1 and train1_string and string_number > 0:
        menu:
            "太黑了，什么也看不见，要点燃绳子吗?"

            '摸索摸索':
                $train1_examine = train1_examine + 1
                if train1_examine == 0:
                    $text_i = text_i + 2
                    $fi_train1_examine0 = text_i
                    jump _train1
                if train1_examine == 1:
                    $text_i = text_i + 1
                    $fi_train1_examine1 = text_i
                    $train1_cloth = True
                if train1_examine == 2:
                    $train1_bone = True
                    $text_i = text_i + 2
                    $fi_train1_examine_bone = text_i
                if train1_examine >= 1 and train1_burnString:
                    $train1_key = True
                jump _train1
            "点燃绳子":
                $string_number = string_number - 1
                $train1_burnString = True
                jump _train1
            "返回":
                jump _train1
    else:
        menu:
            '摸索摸索':
                $train1_examine = train1_examine + 1
                if train1_examine == 0:
                    $text_i = text_i + 2
                    $fi_train1_examine0 = text_i
                    jump _train1
                if train1_examine == 1:
                    $text_i = text_i + 1
                    $fi_train1_examine1 = text_i
                    $train1_cloth = True
                if train1_examine == 2:
                    $train1_bone = True
                    $text_i = text_i + 2
                    $fi_train1_examine_bone = text_i
                if train1_examine >= 1 and train1_burnString:
                    $train1_key = True
                jump _train1
            "返回":
                jump _train1

label train2:
    stop sound
    play music "music/bgm2.wav"

    $firstShowed = True

    if train1_key:
        "车门从外面被锁住了。。。刚才的钥匙或许可以试试。"
        menu:
            "从口袋中摸到了两把钥匙"

            "刚才找到的铁钥匙":
                jump train2_key1

            "一把没见过的钥匙，是从哪儿来的。":
                jump train2_key2

label train2_key1:
    stop sound
    $train2_unlock = True
    "试着用它打开车门，钥匙被掰断了。"
    jump _train2

label train2_key2:
    stop sound
    "车门被打开了。。。"
    jump _train2

label _train2:
    stop sound
    if failExamin:
        $failExamin=False
        "摸索失败"

    if first_train2:
        $text_i = text_i + 1
        $fi_first_train2 = text_i
    $first_train2 = False

    call screen train2()

    if _return == 1:
        $text_i = 0
        jump train1

    if _return == 3:
        if train2_box:
            '这个铁盒是谁的呢？'
        $text_i = 0
        jump train3

label train2_choice:
    stop sound
    if train2_string and string_number > 0:
        menu:
            "要点燃它吗?"

            "点燃绳子":
                $string_number = string_number - 1
                $train2_burnString = True
                $text_i = text_i + 2
                $fi_train2_examine_burngString = text_i
                jump _train2

            "不点燃绳子":
                $train2_burnString = False
                jump _train2


label train3:
    stop sound
    play music "music/bgm3.wav"

    $firstShowed = True

    window hide
    pause 2

    '一扇黑色的铁门挡在我的面前。'

    jump _train3

label _train3:
    stop sound
    if failExamin:
        "摸索失败"
    call screen train3()

    if _return == 2:
        $text_i = 0
        if first_train2:
            jump train2
        else:
            jump _train2


label train3_choice:
    stop sound
    if string_number == 2:
        menu:
            "走进房间":
                jump train3_c1

            "走向绳索":
                jump train3_c2

            "返回":
                jump _train3
    else:
        menu:
            "走进房间":
                jump train3_c1

            "返回":
                jump _train3

label train3_c1:
    stop sound
    play music "music/end.mp3"

    scene end1_1 with dissolve
    pause 2
    scene end1_2 with dissolve
    pause 2
    scene end1_3 with dissolve
    pause 2
    scene end1_4 with dissolve
    pause 2
    "火柴人的灵魂 永远停留在车上。"
    window hide
    pause 1

    stop sound
    stop music
    stop voice
    return

label train3_c2:
    stop sound
    play music "music/end.mp3"

    scene end2_1 with dissolve
    pause 1
    scene end2_2 with dissolve
    pause 1
    scene end2_3 with dissolve
    pause 1
    scene end2_4 with dissolve
    pause 1
    scene end2_5 with dissolve
    pause 0.8
    scene end2_6 with dissolve
    pause 1
    "列车的大门被关上，车缓缓发动起来，火柴人，消失了。"
    window hide
    pause 1

    stop sound
    stop music
    stop voice
    return




# label map1:
#     $firstShowed = True

#     jump _map1

# label _map1:
#     call screen map1()

#     if _return == 1:
#         "Finish Map1"
#         jump map1