from libqtile import bar, layout, qtile, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.log_utils import logger

from qtile_extras import widget as widget_extra
from qtile_extras.widget.decorations import RectDecoration

import os
import subprocess

from colors import catppuccin
import custom_widgets

# mod = Windows key
mod = 'mod4'

# Preferred apps
terminal = os.path.expanduser('~/.local/kitty.app/bin/kitty')

# Are we running on a laptop with battery
is_laptop = os.path.exists('/sys/class/power_supply/BAT0')


#####################
# Keyboard Mappings #
#####################

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

    # Launch terminal
    Key([mod, 'shift'], 'Return', lazy.spawn(terminal)),

    # Toggle between layouts
    Key([mod], 'Tab', lazy.next_layout(), desc='Toggle between layouts'),

    # Kill current window
    Key([mod], 'w', lazy.window.kill(), desc='Kill focused window'),

    # Toggle fullscreen mode
    Key([mod], 'f', lazy.window.toggle_fullscreen(), desc='Toggle fullscreen on the focused window'),

    # Toggle floating mode for current window
    Key([mod], 't', lazy.window.toggle_floating(), desc='Toggle floating on the focused window'),

    # Reload and shutdown Qtile
    Key([mod, 'control'], 'r', lazy.reload_config(), desc='Reload the config'),
    # Key([mod, 'control'], 'q', lazy.shutdown(), desc='Shutdown Qtile'),
    Key([mod, 'control'], 'q', lazy.spawn('systemctl suspend')),

    # Run command
    Key([mod], 'r', lazy.spawncmd(), desc='Spawn a command using a prompt widget'),

    # Spawn rofi
    Key([mod], 'space', lazy.spawn('rofi -show drun')),
    Key([mod, 'shift'], 'space', lazy.spawn('rofi -dmenu')),

    # Spawn preferred app depending on active group
    Key([mod], 'Return', lazy.spawn(terminal)),

    # Control audio volume
    Key([], 'XF86AudioRaiseVolume', lazy.spawn('amixer -D pulse set Master 2%+')),
    Key([], 'XF86AudioLowerVolume', lazy.spawn('amixer -D pulse set Master 2%-')),
    Key([], 'XF86AudioMute', lazy.spawn('amixer -D pulse set Master toggle')),

    # Control monitor brightness
    Key([], 'XF86MonBrightnessUp', lazy.spawn('brightnessctl set +10%')),
    Key([], 'XF86MonBrightnessDown', lazy.spawn('brightnessctl set 10%-')),
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


##########
# Groups #
##########

groups = [Group(name = str(i), label = '\uf444') for i in range(1, 10)]

for group in groups:
    keys.extend([
        Key([mod], group.name, lazy.group[group.name].toscreen()),
        Key([mod, 'shift'], group.name, lazy.window.togroup(group.name, switch_group = True)),
    ])

keys.extend([
    Key([mod], 'Right', lazy.screen.next_group()),
    Key([mod], 'Left', lazy.screen.prev_group())
])


###########
# Layouts #
###########

BORDER_WIDTH = 2
SINGLE_BORDER_WIDTH = 0

BORDER_COLOR = catppuccin['mocha']['base']
BORDER_COLOR_FOCUS = catppuccin['mocha']['red']

WINDOW_MARGIN = 5
SINGLE_WINDOW_MARGIN = 5

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


#######
# BAR #
#######

BAR_BG = catppuccin['mocha']['base']
BAR_FG_LIGHT = catppuccin['mocha']['text']

BAR_HEIGHT = 35
BAR_MARGINS = [0, 0, 0, 0]

BAR_RIGHT_LEFT_SPACE = 10
BAR_SPACE_BETWEEN_WIDGETS = 15
BAR_WIDGET_ICON_SPACE = 3

widget_defaults = dict(
    font = 'JetBrainsMono Nerd Font Mono',
    fontsize = 14,
    padding = 5,
    foreground = BAR_FG_LIGHT
)
extension_defaults = widget_defaults.copy()

top_bar_widgets = [
    widget.Spacer(
        length = BAR_RIGHT_LEFT_SPACE
    ),

    widget.TextBox(
        text = '\uebc9',
        foreground = BAR_FG_LIGHT,
        fontsize = 38
    ),

    widget.Spacer(
        length = BAR_SPACE_BETWEEN_WIDGETS
    ),

    custom_widgets.DotGroupBox(
        fontsize = 24,
        decorations = [
            RectDecoration(
                radius = 11.5,
                padding = 6,
                colour = catppuccin['mocha']['surface_1'],
                filled = True
            )
        ]
    ),

    widget.Spacer(
        length = BAR_SPACE_BETWEEN_WIDGETS
    ),

    widget.TextBox(
        text = '\uebeb',
        foreground = BAR_FG_LIGHT,
        fontsize = 24
    ),

    widget.Spacer(
        length = BAR_WIDGET_ICON_SPACE
    ),

    widget.CurrentLayout(
        foreground = BAR_FG_LIGHT
    ),

    widget.Spacer(length = bar.STRETCH),

    widget.Systray(),

    widget.Spacer(
        length = BAR_SPACE_BETWEEN_WIDGETS
    ),

    custom_widgets.WlanIcon(
        update_interval = 3,
        fontsize = 24
    ),

    widget.Spacer(
        length = BAR_WIDGET_ICON_SPACE
    ),
    
    custom_widgets.WlanInfo(
        update_interval = 3
    ),
    
    widget.Spacer(
        length = BAR_SPACE_BETWEEN_WIDGETS
    ),

    widget.TextBox(
        text = '\uf028',
        foreground = BAR_FG_LIGHT,
        fontsize = 24
    ),

    widget.Spacer(
        length = BAR_WIDGET_ICON_SPACE
    ),

    widget.PulseVolume(
        foreground = BAR_FG_LIGHT
    ),

    widget.Spacer(
        length = BAR_SPACE_BETWEEN_WIDGETS
    ),

    custom_widgets.MacosClock(
        foreground = BAR_FG_LIGHT
    ),

    widget.Spacer(
        length = BAR_SPACE_BETWEEN_WIDGETS
    ),

    widget.QuickExit(
        foreground = BAR_FG_LIGHT,
        default_text = '\uf011',
        fontsize = 24,
        countdown_format = '{}',
        countdown_start = 3,
    ),

    widget.Spacer(
        length = BAR_RIGHT_LEFT_SPACE
    )
]

if is_laptop:
    battery_widgets = [
        widget.TextBox(
            text = '\uf241',
            foreground = BAR_FG_LIGHT,
            fontsize = 24
        ),

        widget.Spacer(
            length = BAR_WIDGET_ICON_SPACE
        ),

        widget.Battery(
            format = '{percent:2.0%}',
            foreground = BAR_FG_LIGHT,
            low_foreground = catppuccin['mocha']['red']
        ),
        
        widget.Spacer(
            length = BAR_SPACE_BETWEEN_WIDGETS
        )
    ]

    top_bar_widgets[-12:-12] = battery_widgets

secondary_top_bar_widgets = [
    widget.Spacer(
        length = BAR_RIGHT_LEFT_SPACE
    ),

    widget.TextBox(
        text = '\uebc9',
        foreground = BAR_FG_LIGHT,
        fontsize = 38
    ),

    widget.Spacer(
        length = BAR_SPACE_BETWEEN_WIDGETS
    ),

    custom_widgets.DotGroupBox(
        fontsize = 24,
        decorations = [
            RectDecoration(
                radius = 11.5,
                padding = 6,
                colour = catppuccin['mocha']['surface_1'],
                filled = True
            )
        ]
    ),

    widget.Spacer(
        length = BAR_SPACE_BETWEEN_WIDGETS
    ),

    widget.TextBox(
        text = '\uebeb',
        foreground = BAR_FG_LIGHT,
        fontsize = 24
    ),

    widget.Spacer(
        length = BAR_WIDGET_ICON_SPACE
    ),

    widget.CurrentLayout(
        foreground = BAR_FG_LIGHT
    )
]

screens = [
    Screen(
        top = bar.Bar(
            top_bar_widgets,
            BAR_HEIGHT,
            background = BAR_BG,
            margin = BAR_MARGINS
        )
    ),
    Screen(
        top = bar.Bar(
            secondary_top_bar_widgets,
            BAR_HEIGHT,
            background = BAR_BG,
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

# Floating window configuration
FLOATING_LAYOUT_BORDER_COLOR = '#f38BA8'

floating_layout = layout.Floating(
border_focus = FLOATING_LAYOUT_BORDER_COLOR,
border_normal = FLOATING_LAYOUT_BORDER_COLOR,
border_width = BORDER_WIDTH,
float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    Match(wm_class = 'org.gnome.Nautilus'),
    # Match(wm_class = 'STM32CubeIDE', title = 'Preferences ')
    Match(wm_class = 'Msgcompose'),
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

