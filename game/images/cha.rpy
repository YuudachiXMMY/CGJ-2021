init offset = -2

default walkSpeed = 0.2

image main_character_front:
    xanchor 0.5 ypos 303
    'images/cha/f.png'

image main_cahracter_back:
    xanchor 0.5 ypos 303
    'images/cha/b.png'

image main_cahracter_walk_left:
    xanchor 0.5 ypos 303
    'images/cha/l/1.png'
    linear walkSpeed/2
    'images/cha/l/2.png'
    linear walkSpeed/2
    'images/cha/l/3.png'
    linear walkSpeed/2
    'images/cha/l/4.png'
    linear walkSpeed/2
    repeat

image main_cahracter_walk_right:
    xanchor 0.5 ypos 303
    'images/cha/r/1.png'
    linear walkSpeed/2
    'images/cha/r/2.png'
    linear walkSpeed/2
    'images/cha/r/3.png'
    linear walkSpeed/2
    'images/cha/r/4.png'
    linear walkSpeed/2
    repeat