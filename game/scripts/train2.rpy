default train2_examine0 = False
default train2_examine1 = False
default train2_examine2 = False
default train2_examine_string = False
default train2_examine_train = False
default train2_examine_burngString = False
default train2_examine_ske0 = True
default train2_examine_ske1 = True
default train2_examine_ske2 = True
default train2_examine_ske_bs = False
default train2_examine_box = False

default fi_first_train2 = 0
define fi_train2_examine_train = 7
default fi_train2_examine_string = 0
default fi_train2_examine_burngString = 0
default fi_train2_examine_ske1 = 0
default fi_train2_examine_ske2 = 0
default fi_trani2_examine_ske_bs = 0

screen train2_bg_front:
    zorder 101
    add 'train2_bg_front' xpos 0 yalign 1.0 xoffset global_xoffset * 0.8
    add 'train2_bg_front_ani' xpos 0 yalign 1.0 xoffset global_xoffset * 0.8

screen train2():

    tag train2

    zorder 100

    add 'train2_bg' xpos 0 xoffset global_xoffset
    if train2_burnString:
        add "train2_bg_ani" xpos 0 xoffset global_xoffset

    on 'show' action Show('mouseControl')
    on 'show' action Show('bgControl', width=2500)

    on 'show' action Show('train2_bg_front')

    imagebutton:
        idle "gui/null_mouseControll.png"
        action Show('mouseControl')

    # Ske
    imagebutton:
        xoffset global_xoffset
        xpos 1190 ypos 316
        auto 'train2_ske_btn_%s'
        if not train2_burnString:
            action [SetVariable('train2_examine_ske0', False),
                SetVariable('text_i', text_i+1), SetVariable('fi_train2_examine_ske1', text_i), SetVariable('fi_trani2_examine_ske_bs', text_i)]
        elif train2_burnString:
            action [SetVariable('train2_examine_ske1', False),
                SetVariable('train2_examine_ske2', False),
                SetVariable('text_i', text_i+5), SetVariable('fi_train2_examine_ske1', text_i), SetVariable('fi_trani2_examine_ske_bs', text_i)
                ]


    if not train2_string:
        imagebutton:
            xoffset global_xoffset
            xpos 382 ypos 641
            auto "train2_string_btn_%s"
            if (curr_player_xpos > 382 - x_obj and curr_player_xpos < 382 + 308 + x_obj):
                action [SetVariable("train2_string", True),
                    SetVariable('text_i', text_i+1),
                    SetVariable('fi_train2_examine_string', text_i),
                    SetVariable("string_number", string_number+1),
                    Hide('mouseControl'),
                    Hide('bgControl'),
                    Hide('train2_bg_front'),
                    Hide('mainChacter'),
                    Jump('train2_choice')]

    if train2_box and not train2_box_popped:
        timer 0.1 action [SetVariable('train2_box_popped', True), Show("item", name='bg/train2/box.png', log="一个盒子")]

    # on 'show' action Show('item', name="1")

    # Train2 BTN
    # # if curr_player_xpos > 1100:
    add 'train2_train2_btn' xpos 0 xoffset global_xoffset
    imagebutton:
        xpos 0 xoffset global_xoffset
        auto 'train2_train2_btn_%s'
        action [
                SetVariable('bar_xoffset', 0),
                SetVariable('global_xoffset', 0),
                SetVariable('player_xoffset', 0),
                SetVariable('curr_mouse_xpos', 150),
                SetVariable('curr_player_xpos', 150),
                SetVariable('tar_player_xpos', 150),
                        Hide('train2_bg_front'),
                        Hide('mouseControl'),
                        Hide('bgControl'),
                        Hide('bgControl_bar'),
                        Hide('mainChacter'),
                        Hide('train2'),
                        Return(1)]

    # Train3 BTN
    # # if curr_player_xpos > 1100:
    add 'train2_train3_btn' xpos 2500 - 197 xoffset global_xoffset
    imagebutton:
        xpos 2500 - 197 xoffset global_xoffset
        auto 'train2_train3_btn_%s'
        action [
                SetVariable('bar_xoffset', 0),
                SetVariable('global_xoffset', 0),
                SetVariable('player_xoffset', 0),
                SetVariable('curr_mouse_xpos', 150),
                SetVariable('curr_player_xpos', 150),
                SetVariable('tar_player_xpos', 150),
                        Hide('train2_bg_front'),
                        Hide('mouseControl'),
                        Hide('bgControl'),
                        Hide('bgControl_bar'),
                        Hide('mainChacter'),
                        Hide('train2'),
                        Return(3)]

    fixed:
        if first_train2:
            $text_i = text_i + 1
            $fi_first_train2 = text_i
            text str("这里仿佛发生过火灾。"):
                ypos 75+25*fi_first_train2 xpos 200 color "#fff"
            timer 3 action SetVariable('first_train2', False), SetVariable('text_i', text_i-1)
        if (curr_player_xpos > 500 and curr_player_xpos < 1050): #and not train2_examine_train:
            # $text_i = text_i + 1
            # $fi_train2_examine_train = text_i
            text str("这是一辆运送煤炭的火车。"):
                ypos 75+25*fi_train2_examine_train xpos 200 color "#fff"
            timer 3 action SetVariable('train2_examine_train', True)#, SetVariable('text_i', text_i-1)
        if train2_string and not train2_examine_string:
            if not train1_string:
                text str("断了一截的麻绳 或许可以拿来燃烧"):
                    ypos 75+25*fi_train2_examine_string xpos 200 color "#fff"
                timer 3 action SetVariable('train2_examine_string', True), SetVariable('text_i', text_i-1)
            else:
                text str("又是这根绳子"):
                    ypos 75+25*fi_train2_examine_string xpos 200 color "#fff"
                timer 3 action SetVariable('train2_examine_string', True), SetVariable('text_i', text_i-1)
        if train2_burnString and not train2_examine_burngString:
            text str("点燃了绳子 红色的火焰窜起起 我在它背后看到了几具实体的残骸。\n他们的结局与这节车厢一样，被大火吞噬。"):
                ypos 75+25*fi_train2_examine_burngString xpos 200 color "#fff"
            timer 3 action SetVariable('train2_examine_burngString', True), SetVariable('text_i', text_i-2)
        if not train2_examine_ske0 and not train2_burnString:
            text str("我阴影中看到了几具实体的残骸 他们的结局与这节车厢一样，被大火吞噬。"):
                ypos 75+25*fi_train2_examine_ske1 xpos 200 color "#fff"
            timer 3 action SetVariable('train2_examine_ske0', True), SetVariable('text_i', text_i-1)
        if not train2_examine_ske1 and train2_burnString and not train2_examine_ske_bs:
            text str("轻轻翻动残骸，找到一个发黑的铁盒子，被锁住了。"):
                ypos 75+25*fi_trani2_examine_ske_bs xpos 200 color "#fff"
            timer 3 action SetVariable('train2_examine_ske1', True), SetVariable('train2_examine_ske_bs', True), SetVariable('train2_box', True), SetVariable('text_i', text_i-1)
            if not train2_unlock:
                text str("盒子上的花纹似乎与刚才的铁钥匙有些相似。"):
                    ypos 75+25*(fi_train2_examine_ske2+1) xpos 200 color "#fff"
                text str("试了好几下，钥匙插进去了，转动钥匙"):
                    ypos 75+25*(fi_train2_examine_ske2+2) xpos 200 color "#fff"
                text str("慢慢打开盒子，里面装着几枚钱币，和几张身份证明，\n上面签名的字迹模糊不清。"):
                    ypos 75+25*(fi_train2_examine_ske2+3) xpos 200 color "#fff"
                timer 3 action SetVariable('train2_examine_ske2', True),SetVariable('train2_examine_box', True), SetVariable('text_i', text_i-4)

    ############################################################################
    # dev
    fixed:
        if dev:

            # text "train2_examine "+str(train2_examine) ypos 0 xpos 100
            # text "train2_cloth "+str(train2_cloth) ypos 20 xpos 100
            # text "train2_string "+str(train2_string) ypos 40 xpos 100
            # text "train2_burnString "+str(train2_burnString) ypos 60 xpos 100
            # text "train2_key "+str(train2_key) ypos 80 xpos 100
            # text "train2_bone "+str(train2_bone) ypos 100 xpos 100

            text _('curr_mouse_xpos '+str(curr_mouse_xpos)) xpos 2000 ypos 100 xoffset global_xoffset
            text _('curr_player_xpos '+str(curr_player_xpos)) xpos 2000 ypos 200 xoffset global_xoffset

            text _('tar_player_xpos '+str(tar_player_xpos)) xpos 900 ypos 100 xoffset global_xoffset
            text _('global_xoffset '+str(global_xoffset)) xpos 900 ypos 200  xoffset global_xoffset
            text _('player_xoffset '+str(player_xoffset)) xpos 900 ypos 300  xoffset global_xoffset
