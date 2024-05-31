from libqtile import bar, layout, qtile, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

import os
import subprocess

# mod = Windows key
mod = 'mod4'

# Terminal
terminal = os.path.expanduser('~/.local/kitty.app/bin/kitty')

keys = [
    # Switch between windows
    Key([mod], 'h', lazy.layout.left(), desc='Move focus to left'),
    Key([mod], 'l', lazy.layout.right(), desc='Move focus to right'),
    Key([mod], 'j', lazy.layout.down(), desc='Move focus down'),
    Key([mod], 'k', lazy.layout.up(), desc='Move focus up'),

    # Move windows
    Key([mod, 'shift'], 'h', lazy.layout.shuffle_left(), desc='Move window to the left'),
    Key([mod, 'shift'], 'l', lazy.layout.shuffle_right(), desc='Move window to the right'),
    Key([mod, 'shift'], 'j', lazy.layout.shuffle_down(), desc='Move window down'),
    Key([mod, 'shift'], 'k', lazy.layout.shuffle_up(), desc='Move window up'),

    # Resize windows
    Key([mod, 'control'], 'h', lazy.layout.grow_left(), desc='Grow window to the left'),
    Key([mod, 'control'], 'l', lazy.layout.grow_right(), desc='Grow window to the right'),
    Key([mod, 'control'], 'j', lazy.layout.grow_down(), desc='Grow window down'),
    Key([mod, 'control'], 'k', lazy.layout.grow_up(), desc='Grow window up'),
    Key([mod], 'n', lazy.layout.normalize(), desc='Reset all window sizes'),

    # ???
    Key([mod, 'shift'], 'Return', lazy.layout.toggle_split(), desc='Toggle between split and unsplit sides of stack'),

    # Launch terminal
    Key([mod], 'Return', lazy.spawn(terminal), desc='Launch terminal'),

    # Toggle between layots
    Key([mod], 'Tab', lazy.next_layout(), desc='Toggle between layouts'),

    # Kill current window
    Key([mod], 'w', lazy.window.kill(), desc='Kill focused window'),

    # Toggle fullscreen mode
    Key([mod], 'f', lazy.window.toggle_fullscreen(), desc='Toggle fullscreen on the focused window'),

    # Toggle floating mode for current window
    Key([mod], 't', lazy.window.toggle_floating(), desc='Toggle floating on the focused window'),

    # Reload and shutdown Qtile
    Key([mod, 'control'], 'r', lazy.reload_config(), desc='Reload the config'),
    Key([mod, 'control'], 'q', lazy.shutdown(), desc='Shutdown Qtile'),

    # Run command
    Key([mod], 'r', lazy.spawncmd(), desc='Spawn a command using a prompt widget'),

    # Spawn rofi
    Key([mod], 'space', lazy.spawn('rofi -show drun'))
]

# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ['control', 'mod1'],
            f'f{vt}',
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == 'wayland'),
            desc=f'Switch to VT{vt}',
        )
    )


groups = [
    Group('1', label = '\uf121'),   # Dev
    Group('2', label = '\uf120'),   # Terminal
    Group('3', label = '\uf269'),   # Firefox
    Group('4', label = '\uf42f'),   # Mail
    Group('5', label = '\uf198'),   # Slack
    Group('6', label = '\uf1bc')    # Spotify
]

for i in groups:
    keys.extend(
        [
            # mod + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc='Switch to group {}'.format(i.name),
            ),
            # mod + shift + group number = switch to & move focused window to group
            Key(
                [mod, 'shift'],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc='Switch to & move focused window to group {}'.format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod + shift + group number = move focused window to group
            # Key([mod, 'shift'], i.name, lazy.window.togroup(i.name),
            #     desc='move focused window to group {}'.format(i.name)),
        ]
    )

BORDER_WIDTH = 2
SINGLE_BORDER_WIDTH = 2

BORDER_COLOR = '#24273A'
BORDER_COLOR_FOCUS = '#FAB387'

WINDOW_MARGIN = 10
SINGLE_WINDOW_MARGIN = 20

COMMON_LAYOUT_SETTINGS = {
    'border_width': BORDER_WIDTH,
    'single_border_width': SINGLE_BORDER_WIDTH,
    'border_normal': BORDER_COLOR,
    'border_focus': BORDER_COLOR_FOCUS,
    'margin': WINDOW_MARGIN,
    'single_margin': SINGLE_WINDOW_MARGIN
}

layouts = [
    layout.MonadTall(**COMMON_LAYOUT_SETTINGS)
]

widget_defaults = dict(
    font = 'JetBrainsMono Nerd Font Mono',
    fontsize = 14,
    padding = 3
)
extension_defaults = widget_defaults.copy()


BAR_FOREGROUND_LIGHT = '#CDD6f4'
BAR_FOREGROUND_DARK = '#1E1E2E'

BAR_BACKGROUND = '#585B70'

BAR_MARGINS = [0, 0, 0, 0]

GROUP_SELECT_BACKGROUND = '#FAB387'

COMMON_WIDGET_SETTINGS = {
    'foreground': '#000000'
}

screens = [
    Screen(
        top = bar.Bar(
            [
                widget.TextBox(
                    text = '\uebc9',
                    foreground = GROUP_SELECT_BACKGROUND,
                    fontsize = 36,
                    padding = 10
                ),
                widget.Spacer(length = 20),
                widget.GroupBox(
                    highlight_method = 'block',
                    this_current_screen_border = GROUP_SELECT_BACKGROUND,
                    this_screen_border = GROUP_SELECT_BACKGROUND,
                    other_current_screen_border = None,
                    other_screen_border = None,
                    foreground = BAR_FOREGROUND_LIGHT,
                    inactive = BAR_FOREGROUND_LIGHT,
                    active = BAR_FOREGROUND_LIGHT,
                    block_highlight_text_color = BAR_FOREGROUND_DARK,
                    fontsize = 36,
                    margin_x = 0,
                    padding_x = 10
                ),
                widget.WindowName(foreground = BAR_FOREGROUND_LIGHT),
                # widget.Systray(),
                widget.TextBox(
                    text = '\uf017',
                    foreground = BAR_FOREGROUND_LIGHT,
                    fontsize = 24
                ),
                widget.Clock(
                    format = '%H:%M',
                    foreground = BAR_FOREGROUND_LIGHT,
                    padding = 10
                ),
                widget.Spacer(length = 20),
                widget.TextBox(
                    text = '\uf455',
                    foreground = BAR_FOREGROUND_LIGHT,
                    fontsize = 24
                ),
                widget.Clock(
                    format = '%d/%m/%Y',
                    foreground = BAR_FOREGROUND_LIGHT,
                    padding = 10
                ),
                widget.Spacer(length = 20),
                widget.QuickExit(**COMMON_WIDGET_SETTINGS),
            ],
            36,
            background = BAR_BACKGROUND,
            margin = BAR_MARGINS
        )
    )
]


# Drag floating layouts.
mouse = [
    Drag([mod], 'Button1', lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], 'Button3', lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], 'Button2', lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),  # gitk
        Match(wm_class='makebranch'),  # gitk
        Match(wm_class='maketag'),  # gitk
        Match(wm_class='ssh-askpass'),  # ssh-askpass
        Match(title='branchdialog'),  # gitk
        Match(title='pinentry'),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = 'smart'
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 24

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = 'LG3D'


@hook.subscribe.startup_once
def startup_once():
    script = os.path.expanduser('~/.config/qtile/startup_once.sh')
    subprocess.run([script])


@hook.subscribe.startup
def startup():
    script = os.path.expanduser('~/.config/qtile/startup.sh')
    subprocess.run([script])

