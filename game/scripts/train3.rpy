default train3_examine_room1 = False
default train3_examine_room2 = False
default train3_examine_room3 = True
default train3_examine_post = True


default fi_train3_examine_post = True
define fi_train3_examine_room1 = 4
define fi_train3_examine_room2 = 4
define fi_train3_examine_room3 = 4

screen train3_bg_front:
    zorder 101
    add 'train3_bg_front' xpos 0 yalign 1.0 xoffset global_xoffset * 0.8

screen train3():

    tag train3

    zorder 100

    add 'train3_bg' xpos 0 xoffset global_xoffset
    if train3_burnString:
        add "train3_bg_ani" xpos 0 xoffset global_xoffset

    on 'show' action Show('mouseControl')
    on 'show' action Show('bgControl', width=3181)

    on 'show' action Show('train3_bg_front')

    imagebutton:
        idle "gui/null_mouseControll.png"
        action Show('mouseControl')



    # Door3
    imagebutton:
        activate_sound "music/item.wav"
        xoffset global_xoffset
        xpos 1184 ypos 82
        auto 'train3_door3_btn_%s'
        action [
            Hide('mouseControl'),
            Hide('bgControl'),
            Hide('train3_bg_front'),
            Hide('mainChacter'),
            Jump('train3_choice')
        ]


    # Post
    imagebutton:
        xoffset global_xoffset
        xpos 1234 ypos 201
        auto 'train3_post_btn_%s'
        action [SetVariable('train3_examine_post', False),
                SetVariable('text_i', text_i+3), SetVariable('fi_train3_examine_post', text_i)
                ]
    # on 'show' action Show('item', name="1")

    # Train2 BTN
    # # if curr_player_xpos > 1100:
    add 'train3_train2_btn' xpos 0 xoffset global_xoffset
    imagebutton:
        xpos 0 xoffset global_xoffset
        auto 'train3_train2_btn_%s'
        action [
                SetVariable('bar_xoffset', 0),
                SetVariable('global_xoffset', 0),
                SetVariable('player_xoffset', 0),
                SetVariable('curr_mouse_xpos', 150),
                SetVariable('curr_player_xpos', 150),
                SetVariable('tar_player_xpos', 150),
                        Hide('train3_bg_front'),
                        Hide('mouseControl'),
                        Hide('bgControl'),
                        Hide('bgControl_bar'),
                        Hide('mainChacter'),
                        Hide('train3'),
                        Return(2)]

    fixed:
        if not train3_examine_post:
            text str("山区列车意外脱轨发生严重爆炸"):
                ypos 75+25*fi_train3_examine_post xpos 400 color "#fff"
            text str("1名列车司机当场身亡，1名失踪。。。"):
                ypos 75+25*(fi_train3_examine_post+1) xpos 400 color "#fff"
            text str("事故现场还发现3名异教徒尸体，疑似偷渡藏匿在货仓内。"):
                ypos 75+25*(fi_train3_examine_post+2) xpos 400 color "#fff"
            timer 3 action SetVariable('train3_examine_post', True), SetVariable('text_i', text_i-1)
        if (curr_player_xpos > 315 and curr_player_xpos < 650): #and not fi_train3_examine_room1:
            # $text_i = text_i + 1
            # $fi_train3_examine_room1 = text_i
            text str("我是谁"):
                ypos 75+25*fi_train3_examine_room1 xpos 500 color "#fff"
            text str("你们是什么人？"):
                ypos 75+25*(fi_train3_examine_room1+1) xpos 500 color "#fff"
            timer 3 action SetVariable('train3_examine_room1', True)#, SetVariable('text_i', text_i-2)

        if (curr_player_xpos > 750 and curr_player_xpos < 1100): #and not train3_examine_room2:
            # $text_i = text_i + 1
            # $train3_examine_room2 = text_i
            text str("门从外面被锁住了！"):
                ypos 75+25*fi_train3_examine_room2 xpos 500 color "#fff"
            timer 3 action SetVariable('train3_examine_room2', True)#, SetVariable('text_i', text_i-1)

        if (curr_player_xpos > 1200 and curr_player_xpos < 1535): #and not train3_examine_room3:
            # $text_i = text_i + 1
            # $train3_examine_room3 = text_i
            text str("03：33 停驶3分钟 暗号：3个火柴人 Match "):
                ypos 75+25*fi_train3_examine_room3 xpos 400 color "#fff"
            timer 3 action SetVariable('train3_examine_room3', True)#, SetVariable('text_i', text_i-1)

    ############################################################################
    # dev
    fixed:
        if dev:

            text "train3_examine "+str(train3_examine) ypos 0 xpos 100
            text "train3_cloth "+str(train3_cloth) ypos 20 xpos 100
            text "train3_string "+str(train3_string) ypos 40 xpos 100
            text "train3_burnString "+str(train3_burnString) ypos 60 xpos 100
            text "train3_key "+str(train3_key) ypos 80 xpos 100
            text "train3_bone "+str(train3_bone) ypos 100 xpos 100

            text _('curr_mouse_xpos '+str(curr_mouse_xpos)) xpos 2000 ypos 100 xoffset global_xoffset
            text _('curr_player_xpos '+str(curr_player_xpos)) xpos 2000 ypos 200 xoffset global_xoffset

            text _('tar_player_xpos '+str(tar_player_xpos)) xpos 900 ypos 100 xoffset global_xoffset
            text _('global_xoffset '+str(global_xoffset)) xpos 900 ypos 200  xoffset global_xoffset
            text _('player_xoffset '+str(player_xoffset)) xpos 900 ypos 300  xoffset global_xoffset
