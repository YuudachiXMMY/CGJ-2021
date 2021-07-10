init offset = -999

define config.pad_bindings = {
    "pad_leftshoulder_press" : [ ],
    "pad_lefttrigger_pos" : [ ],
    "pad_back_press" : [ ],

    "pad_guide_press" : [ ],
    "pad_start_press" : [ ],

    "pad_y_press" : [ ],

    "pad_rightshoulder_press" : [ ],

    "pad_righttrigger_pos" : [ ],
    "pad_a_press" : [ ],
    "pad_b_press" : [ ],

    "pad_dpleft_press" : [ ],
    "pad_leftx_neg" : [ ],
    "pad_rightx_neg" : [ ],

    "pad_dpright_press" : [ ],
    "pad_leftx_pos" : [ ],
    "pad_rightx_pos" : [ ],

    "pad_dpup_press" : [ ],
    "pad_lefty_neg" :  [ ],
    "pad_righty_neg" : [ ],

    "pad_dpdown_press" : [ ],
    "pad_lefty_pos" : [ ],
    "pad_righty_pos" : [ ],
}

define config.keymap = dict(

    # Bindings present almost everywhere, unless explicitly
    # disabled.
    rollback = [ ],
    screenshot = [ 's' ],
    toggle_afm = [ ],
    toggle_fullscreen = [ ],
    game_menu = [ ],
    hide_windows = [ ],
    launch_editor = [ ],
    dump_styles = [ ],
    reload_game = [ 'R' ],
    inspector = [ ],
    full_inspector = [ ],
    developer = [ ],
    quit = [ ],
    iconify = [ ],
    help = [ ],
    choose_renderer = [ ],
    progress_screen = [ ],
    # Accessibility.
    self_voicing = [ ],
    clipboard_voicing = [ ],
    debug_voicing = [ ],

    # Say.
    rollforward = [ 'mousedown_5', 'K_PAGEDOWN', 'repeat_K_PAGEDOWN' ],
    dismiss = [ 'mouseup_1', 'K_RETURN', 'K_SPACE', 'K_KP_ENTER', 'K_SELECT' ],
    dismiss_unfocused = [ ],

    # Pause.
    dismiss_hard_pause = [ ],

    # Focus.
    focus_left = [ ],
    focus_right = [ ],
    focus_up = [ ],
    focus_down = [ ],

    # Button.
    button_ignore = [ 'mousedown_1' ],
    button_select = [ 'mouseup_1', 'K_RETURN', 'K_KP_ENTER', 'K_SELECT' ],
    button_alternate = [ 'mouseup_3' ],
    button_alternate_ignore = [ 'mousedown_3' ],

    # Input.
    input_backspace = [ ],
    input_enter = [ ],
    input_left = [ ],
    input_right = [ ],
    input_up = [ ],
    input_down = [ ],
    input_delete = [ ],
    input_home = [ ],
    input_end = [ ],
    input_copy = [ ],
    input_paste = [ ],

    # Viewport.
    viewport_leftarrow = [ ],
    viewport_rightarrow = [ ],
    viewport_uparrow = [ ],
    viewport_downarrow = [ ],
    viewport_wheelup = [ ],
    viewport_wheeldown = [ ],
    viewport_drag_start = [ ],
    viewport_drag_end = [ ],

    # These keys control skipping.
    skip = [ ],
    stop_skipping = [ ],
    toggle_skip = [ ],
    fast_skip = [ ],

    # Bar.
    bar_activate = [ ],
    bar_deactivate = [ ],
    bar_left = [ ],
    bar_right = [ ],
    bar_up = [ ],
    bar_down = [ ],

    # Delete a save.
    save_delete = [ ],

    # Draggable.
    drag_activate = [ ],
    drag_deactivate = [ ],

    # Debug console.
    console = [ 'shift_O' ],
    console_older = [ 'K_UP', 'repeat_K_UP' ],
    console_newer = [ 'K_DOWN', 'repeat_K_DOWN'],

    # Ignored (kept for backwards compatibility).
    toggle_music = [ ],
    viewport_up = [ ],
    viewport_down = [ ],

    # Profile commands.
    profile_once = [ 'K_F8' ],
    memory_profile = [ 'K_F7' ],


    )