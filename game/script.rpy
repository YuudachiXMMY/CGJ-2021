# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

# The game starts here.

label start:

    # scene intro_bg:
    #     xpos 0 xoffset global_xoffset

    $ curr_mouse_xpos = renpy.get_mouse_pos()[0]

    call screen intro()

    pause

    return
