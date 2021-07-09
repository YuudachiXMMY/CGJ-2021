
default curr_mouse_position = (0, 0)
default curr_player_position = (0, 0)
default global_xoffset = 0
default bar_xoffset = global_xoffset
default local_xoffset = 0

screen mouseControl():

    zorder 110

    imagebutton:
        idle "gui/null_mouseControll.png"
        action [SetVariable('curr_mouse_position', renpy.get_mouse_pos()),
                SetVariable('local_xoffset', global_xoffset)]

screen bgControl():

    zorder 111

    fixed:
        bar value VariableValue('bar_xoffset', 2560, action=SetVariable('global_xoffset', -bar_xoffset))

screen intro():

    tag intro

    zorder 100

    on 'show' action Show('mouseControl')
    on 'show' action Show('bgControl')

    add "intro_bg" xpos 0 xoffset global_xoffset

    fixed:
        text _('mos pos '+str(curr_mouse_position)) xpos 500 ypos 100 xoffset global_xoffset
        text _('cur pos '+str(curr_player_position)) xpos 500 ypos 200 xoffset global_xoffset

        text _('global xoffset '+str(global_xoffset)) xpos 900 ypos 100  xoffset global_xoffset
        text _('cur xoffset '+str(local_xoffset)) xpos 900 ypos 200 xoffset global_xoffset