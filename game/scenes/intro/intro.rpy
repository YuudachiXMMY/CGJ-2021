
default curr_mouse_xpos = 0
default curr_player_xpos = 0
default global_xoffset = 0
default bar_xoffset = global_xoffset
default local_xoffset = 0

screen mouseControl():

    zorder 110

    imagebutton:
        idle "gui/null_mouseControll.png"
        action [SetVariable('curr_mouse_xpos', renpy.get_mouse_pos()[0]),
                SetVariable('local_xoffset', global_xoffset)]

screen bgControl():

    zorder 111

    fixed:
        bar value VariableValue('bar_xoffset', 2560, action=SetVariable('global_xoffset', -bar_xoffset))

screen mainChacter():

    zorder 101

    add 'main_character_front':
        if curr_mouse_xpos != curr_player_xpos:
            transform:
                linear 1 xpos curr_mouse_xpos - local_xoffset
        else:
            xpos curr_player_xpos - local_xoffset

    on 'show' action SetVariable('curr_player_xpos', curr_mouse_xpos)

screen intro():

    tag intro

    zorder 100

    on 'show' action Show('mouseControl')
    on 'show' action Show('bgControl')
    on 'show' action Show('mainChacter')

    add "intro_bg" xpos 0 xoffset global_xoffset

    fixed:
        text _('curr_mouse_xpos '+str(curr_mouse_xpos)) xpos 500 ypos 100 xoffset global_xoffset
        text _('curr_player_xpos '+str(curr_player_xpos)) xpos 500 ypos 200 xoffset global_xoffset

        text _('global_xoffset '+str(global_xoffset)) xpos 900 ypos 100  xoffset global_xoffset
        text _('local_xoffset '+str(local_xoffset)) xpos 900 ypos 200 xoffset global_xoffset