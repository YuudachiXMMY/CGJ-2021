init offset = -2

default walkSpeed = 0.2

image main_character_front:
    zoom 0.4 xanchor 0.5
    ypos 50
    'images/cha/f.png'

image main_cahracter_back:
    zoom 0.4 xanchor 0.5
    ypos 50
    'images/cha/b.png'

image main_cahracter_walk_left:
    zoom 0.4 xanchor 0.5
    ypos 50
    'images/cha/l/01.png'
    linear walkSpeed
    'images/cha/l/02.png'
    linear walkSpeed
    'images/cha/l/03.png'
    linear walkSpeed
    'images/cha/l/04.png'
    linear walkSpeed
    'images/cha/l/05.png'
    linear walkSpeed
    'images/cha/l/06.png'
    linear walkSpeed
    'images/cha/l/07.png'
    linear walkSpeed
    'images/cha/l/08.png'
    linear walkSpeed
    repeat

image main_cahracter_walk_right:
    zoom 0.4 xanchor 0.5
    ypos 50
    'images/cha/r/01.png'
    linear walkSpeed
    'images/cha/r/02.png'
    linear walkSpeed
    'images/cha/r/03.png'
    linear walkSpeed
    'images/cha/r/04.png'
    linear walkSpeed
    'images/cha/r/05.png'
    linear walkSpeed
    'images/cha/r/06.png'
    linear walkSpeed
    'images/cha/r/07.png'
    linear walkSpeed
    'images/cha/r/08.png'
    linear walkSpeed
    repeat