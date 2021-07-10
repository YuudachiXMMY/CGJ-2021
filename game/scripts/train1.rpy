default train1_examine0 = False
default train1_examine1 = False
default train1_examine2 = False
default train1_examine_window = False
default train1_examine_string = True
default train1_examine_burnString = False
default train1_examine_bone = False

default fi_train1_examine0 = 0
default fi_train1_examine1 = 0
default fi_train1_examine2 = 0
default fi_train1_examine_window = 0
default fi_train1_examine_string = 0
default fi_train1_examine_burnString = 0
default fi_train1_examine_bone = 0

screen train1_bg_front:
    zorder 101
    add 'train1_bg_front' xpos 0 yalign 1.0 xoffset global_xoffset * 0.8

screen train1():

    tag train1

    zorder 100

    add 'train1_bg' xpos 0 xoffset global_xoffset
    if train1_burnString:
        add "train1_bg_ani" xpos 0 xoffset global_xoffset

    on 'show' action Show('mouseControl')
    on 'show' action Show('bgControl', width=2500)

    on 'show' action Show('train1_bg_front')

    imagebutton:
        idle "gui/null_mouseControll.png"
        action Show('mouseControl')

    fixed:
        if train1_burnString and not train1_examine_burnString:
            text str("用手擦拭祷告桌，桌上堆叠着破损的餐具，书籍的残骸，在一片狼藉中，找到一把破旧的铁钥匙。"):
                ypos 75 xpos 200 color "#fff"
            timer 3 action SetVariable('train1_examine_burnString', True)
        if train1_bone and not train1_examine_bone:
            text str("车厢变亮了一些 ，桌下盖着厚厚的幕布。"):
                ypos 75 xpos 200 color "#fff"
            text str("揭开后，发现是一具骸骨，和残留的绳絮。"):
                ypos 75 xpos 200 color "#fff"
            timer 3 action SetVariable('train1_examine_bone', True)
        if train1_examine == 0 and not train1_examine0:
            text str("拿起蜡烛，墙上的文字辨别不清是涂鸦还是什么文字。"):
                ypos 75 xpos 200 color "#fff"
            text str("一个祷告桌，盖满了黑色的粉尘。"):
                ypos 75 xpos 200 color "#fff"
            timer 3 action SetVariable('train1_examine0', True)
        if train1_examine == 1 and not train1_examine1:
            text str("发现了一件破损衣服，看似有些眼熟。。。好像是件制服。"):
                ypos 75 xpos 200 color "#fff"
            timer 3 action SetVariable('train1_examine1', True)
        if (curr_player_xpos > 1425 and curr_player_xpos < 1990) and not train1_examine_window:
            text str("车窗被钢条焊斯，透过玻璃窗户向外看去，黑漆漆的一片，没有点光。"):
                ypos 75 xpos 200 color "#fff"
            timer 3 action SetVariable('train1_examine_window', True)
        if not train1_examine_string:
            text str("断了一截的麻绳 或许可以拿来燃烧"):
                ypos 75 xpos 200 color "#fff"
            timer 3 action SetVariable('train1_examine_string', True)



    # Candle
    imagebutton:
        xoffset global_xoffset
        xpos 521 ypos 260
        auto 'train1_candle_btn_%s'
        action [
            Hide('mouseControl'),
            Hide('bgControl'),
            Hide('train1_bg_front'),
            Hide('mainChacter'),
            Jump('train1_choice')
        ]

    if not train1_string:
        imagebutton:
            xoffset global_xoffset
            xpos 1585 ypos 584
            auto "train1_string_btn_%s"
            action SetVariable("train1_examine_string", False), SetVariable("train1_string", True), SetVariable("string_number", string_number+1)

    if train1_burnString and not train1_key_popped:
        timer 0.1 action [SetVariable('train1_key_popped', True), Show("item", name='bg/train1/key.png', log="一把钥匙")]

    # on 'show' action Show('item', name="1")

    # Train2 BTN
    # # if curr_player_xpos > 1100:
    add 'train1_train2_btn' xpos 2500 - 197 xoffset global_xoffset
    imagebutton:
        xpos 2500 - 197 xoffset global_xoffset
        auto 'train1_train2_btn_%s'
        action [
                SetVariable('bar_xoffset', 0),
                SetVariable('global_xoffset', 0),
                SetVariable('player_xoffset', 0),
                SetVariable('curr_mouse_xpos', 150),
                SetVariable('curr_player_xpos', 150),
                SetVariable('tar_player_xpos', 150),
                        Hide('train1_bg_front'),
                        Hide('mouseControl'),
                        Hide('bgControl'),
                        Hide('bgControl_bar'),
                        Hide('mainChacter'),
                        Hide('train1'),
                        Return(2)]


    ############################################################################
    # dev
    fixed:
        if dev:

            text "train1_examine "+str(train1_examine) ypos 0 xpos 100
            text "train1_cloth "+str(train1_cloth) ypos 20 xpos 100
            text "train1_string "+str(train1_string) ypos 40 xpos 100
            text "train1_burnString "+str(train1_burnString) ypos 60 xpos 100
            text "train1_key "+str(train1_key) ypos 80 xpos 100
            text "train1_bone "+str(train1_bone) ypos 100 xpos 100

            text _('curr_mouse_xpos '+str(curr_mouse_xpos)) xpos 2000 ypos 100 xoffset global_xoffset
            text _('curr_player_xpos '+str(curr_player_xpos)) xpos 2000 ypos 200 xoffset global_xoffset

            text _('tar_player_xpos '+str(tar_player_xpos)) xpos 900 ypos 100 xoffset global_xoffset
            text _('global_xoffset '+str(global_xoffset)) xpos 900 ypos 200  xoffset global_xoffset
            text _('player_xoffset '+str(player_xoffset)) xpos 900 ypos 300  xoffset global_xoffset
