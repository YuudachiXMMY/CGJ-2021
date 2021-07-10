
screen map1_front:
    zorder 101
    add 'map1_bg_front' xpos 0 xoffset global_xoffset * 0.8

screen map1():

    tag map1

    zorder 100

    add "map1_bg" xpos 0 xoffset global_xoffset

    on 'show' action Show('mouseControl')
    on 'show' action Show('bgControl', width=2500)

    on 'show' action Show('map1_front')

    imagebutton:
        idle "gui/null_mouseControll.png"
        action Show('mouseControl')

    # # if curr_player_xpos > 1100:
    # add 'train1_btn' xpos 1081 ypos 720-698
    # imagebutton:
    #     xpos 1081 ypos 720-698
    #     auto 'train1_btn_%s'
    #     action [
    #                     Hide('mouseControl'),
    #                     Hide('bgControl'),
    #                     Hide('bgControl_bar'),
    #                     Hide('mainChacter'),
    #                     Hide('intro'),
    #                     Return()]


    ############################################################################
    # dev
    fixed:
        if dev:

            text _('curr_mouse_xpos '+str(curr_mouse_xpos)) xpos 500 ypos 100 xoffset global_xoffset
            text _('curr_player_xpos '+str(curr_player_xpos)) xpos 500 ypos 200 xoffset global_xoffset

            text _('tar_player_xpos '+str(tar_player_xpos)) xpos 900 ypos 100 xoffset global_xoffset
            text _('global_xoffset '+str(global_xoffset)) xpos 900 ypos 200  xoffset global_xoffset
            text _('player_xoffset '+str(player_xoffset)) xpos 900 ypos 300  xoffset global_xoffset
