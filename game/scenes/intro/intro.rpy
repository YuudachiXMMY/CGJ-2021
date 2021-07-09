
default curr_mouse_xpos = 0
default curr_player_xpos = 50
default tar_player_xpos = curr_player_xpos
default global_xoffset = 0
default bar_xoffset = global_xoffset
default local_xoffset = 0

screen mouseControl():

    zorder 300

    modal True

    text "Waling..."

    on 'show' action [  Hide('mainChacter'), Show('mainChacter'),
                        SetVariable('curr_mouse_xpos', renpy.get_mouse_pos()[0]),
                        SetVariable('tar_player_xpos', renpy.get_mouse_pos()[0]),
                        SetVariable('local_xoffset', global_xoffset)
                        ]
    timer 1.1 action Hide('mouseControl')

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

    add 'main_character_front':
        xoffset global_xoffset
        xpos curr_player_xpos - local_xoffset
        if tar_player_xpos != curr_player_xpos:
            at transform:
                xpos curr_player_xpos - local_xoffset
                linear 1.0 xpos tar_player_xpos - local_xoffset

    timer 0.01 action SetVariable('curr_player_xpos', tar_player_xpos)

screen intro():

    tag intro

    zorder 100

    add "intro_bg" xpos 0 xoffset global_xoffset

    on 'show' action Show('mouseControl')
    on 'show' action Show('bgControl')


    fixed:
        text _('curr_mouse_xpos '+str(curr_mouse_xpos)) xpos 500 ypos 100 xoffset global_xoffset
        text _('curr_player_xpos '+str(curr_player_xpos)) xpos 500 ypos 200 xoffset global_xoffset
        text _('tar_player_xpos '+str(tar_player_xpos)) xpos 500 ypos 300 xoffset global_xoffset

        text _('global_xoffset '+str(global_xoffset)) xpos 900 ypos 100  xoffset global_xoffset
        text _('local_xoffset '+str(local_xoffset)) xpos 900 ypos 200 xoffset global_xoffset


    fixed:
        imagebutton:
            idle "gui/null_mouseControll.png"
            action Show('mouseControl')