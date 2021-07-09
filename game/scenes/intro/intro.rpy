
default curr_mouse_xpos = 0
default curr_player_xpos = 50
default tar_player_xpos = curr_mouse_xpos
default global_xoffset = 0
default player_xoffset = global_xoffset
default bar_xoffset = global_xoffset

define dev = True

default TwalkSpeed = 0.2
default diff = (tar_player_xpos - player_xoffset) - curr_player_xpos

screen mouseControl():

    zorder 300

    modal True

    text "Waling...":
        xpos 493 ypos 20

    on 'show' action [  Hide('mainChacter'),
                        Show('mainChacter'),
                        SetVariable('player_xoffset', global_xoffset),
                        SetVariable('curr_mouse_xpos', renpy.get_mouse_pos()[0]),
                        SetVariable('tar_player_xpos', renpy.get_mouse_pos()[0])
                        ]

    $ diff = (tar_player_xpos - player_xoffset) - curr_player_xpos
    if abs(diff) > 1500:
        timer 0.0001 action SetVariable('walkSpeed', 0.01)
        $TwalkSpeed = 0.01
    if abs(diff) > 1000:
        timer 0.0001 action SetVariable('walkSpeed', 0.05)
        $TwalkSpeed = 0.05
    if abs(diff) > 800:
        timer 0.0001 action SetVariable('walkSpeed', 0.08)
        $TwalkSpeed = 0.08
    if abs(diff) > 400:
        timer 0.0001 action SetVariable('walkSpeed', 0.1)
        $TwalkSpeed = 0.1
    elif abs(diff) > 100:
        timer 0.0001 action SetVariable('walkSpeed', 0.2)
        $TwalkSpeed = 0.2
    else:
        timer 0.0001 action SetVariable('walkSpeed', 0.3)
        $TwalkSpeed = 0.3

    timer (10/(TwalkSpeed+1)-7)  action Hide('mouseControl')

screen bgControl():

    zorder 111

    fixed:
        style_prefix 'bgControl'
        xpos 493
        bar value VariableValue('bar_xoffset', 2560, action=SetVariable('global_xoffset', -bar_xoffset))

style bgControl_bar:
    xysize(294, 19)
    base_bar "bgControl_slider_idle"
    thumb "bgControl_slider_btn_idle"

screen mainChacter():

    zorder 101

    $ diff = (tar_player_xpos - player_xoffset) - curr_player_xpos
    if abs(diff) > 1500:
        $TwalkSpeed = 0.01
    if abs(diff) > 1000:
        $TwalkSpeed = 0.05
    if abs(diff) > 800:
        $TwalkSpeed = 0.08
    if abs(diff) > 400:
        $TwalkSpeed = 0.1
    elif abs(diff) > 100:
        $TwalkSpeed = 0.2
    else:
        $TwalkSpeed = 0.3

    # Stable
    if diff == 0:
        add 'main_character_front':
            xoffset global_xoffset
            xpos tar_player_xpos - player_xoffset
    # Move Right
    if diff > 0:
        add 'main_cahracter_walk_right':
            xoffset global_xoffset
            at transform:
                xpos curr_player_xpos
                linear (10/(TwalkSpeed+1)-7) xpos tar_player_xpos - global_xoffset
    # Move Left
    elif diff < 0:
        add 'main_cahracter_walk_left':
            xoffset global_xoffset
            at transform:
                xpos curr_player_xpos
                linear (10/(TwalkSpeed+1)-7) xpos tar_player_xpos - global_xoffset

    timer 0.01 action SetVariable('curr_player_xpos', tar_player_xpos - player_xoffset)

screen intro():

    tag intro

    zorder 100

    add "intro_bg" xpos 0 xoffset global_xoffset

    on 'show' action Show('mouseControl')
    on 'show' action Show('bgControl')


    fixed:
        if dev:

            text str(10/(TwalkSpeed+1)-7) xpos 200 ypos 100 xoffset global_xoffset

            text _('curr_mouse_xpos '+str(curr_mouse_xpos)) xpos 500 ypos 100 xoffset global_xoffset
            text _('curr_player_xpos '+str(curr_player_xpos)) xpos 500 ypos 200 xoffset global_xoffset

            text _('tar_player_xpos '+str(tar_player_xpos)) xpos 900 ypos 100 xoffset global_xoffset
            text _('global_xoffset '+str(global_xoffset)) xpos 900 ypos 200  xoffset global_xoffset
            text _('player_xoffset '+str(player_xoffset)) xpos 900 ypos 300  xoffset global_xoffset

    fixed:
        imagebutton:
            idle "gui/null_mouseControll.png"
            action Show('mouseControl')