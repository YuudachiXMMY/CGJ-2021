
screen intro():

    tag test

    zorder 100

    add "intro_bg" xpos 0 xoffset global_xoffset

    on 'show' action Show('mouseControl')
    on 'show' action Show('bgControl', width=1280)

    imagebutton:
        idle "gui/null_mouseControll.png"
        action Show('mouseControl')


    # Train1 BTN
    # if curr_player_xpos > 1100:
    add 'intro_train1_btn' xpos 1081 ypos 720-698
    imagebutton:
        xpos 1081 ypos 720-698
        auto 'intro_train1_btn_%s'
        if (curr_player_xpos > 1081 - x_obj and curr_player_xpos < 1081 + 193 + x_obj):
            action [
                    SetVariable('bar_xoffset', 0),
                    SetVariable('global_xoffset', 0),
                    SetVariable('player_xoffset', 0),
                    SetVariable('curr_mouse_xpos', 100),
                    SetVariable('curr_player_xpos', 100),
                    SetVariable('tar_player_xpos', 100),
                            Hide('mouseControl'),
                            Hide('bgControl'),
                            Hide('bgControl_bar'),
                            Hide('mainChacter'),
                            Hide('intro'),
                            Return()]
        else:
            action NullAction()


    ############################################################################
    # dev
    fixed:
        if dev:

            text _('curr_mouse_xpos '+str(curr_mouse_xpos)) xpos 500 ypos 100 xoffset global_xoffset
            text _('curr_player_xpos '+str(curr_player_xpos)) xpos 500 ypos 200 xoffset global_xoffset

            text _('tar_player_xpos '+str(tar_player_xpos)) xpos 900 ypos 100 xoffset global_xoffset
            text _('global_xoffset '+str(global_xoffset)) xpos 900 ypos 200  xoffset global_xoffset
            text _('player_xoffset '+str(player_xoffset)) xpos 900 ypos 300  xoffset global_xoffset
