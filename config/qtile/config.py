# Qtile's configuration.

import os
from typing import List  # noqa: F401
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = "kitty"

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    #Key([mod], "tab", lazy.layout.next(),
        #desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the righ"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    #Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    #Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    #Key([mod], "r", lazy.spawncmd(),
        #desc="Spawn a command using a prompt widget"),

    # My custom keybindings.

    # To take screenshots, fullscreen
    Key([], "Print", lazy.spawn("flameshot full --path /home/user")),

    # To take screenshots, GUI
    Key(["Shift"], "Print", lazy.spawn("flameshot gui")),

    # To open Rofi
    Key([mod], "r", lazy.spawn("rofi -show drun")),

    # To open Nemo
    Key([mod], "e", lazy.spawn("nemo")),

    # To open Vivaldi
    Key([mod], "v", lazy.spawn("vivaldi-stable")),

    # To toggle full screen
    Key([mod], "f", lazy.window.toggle_fullscreen()),

    # To toggle bars
    Key([mod], "b", lazy.hide_show_bar(position='all')),

    # To switch window focus
    Key(["mod1"], "Tab", lazy.layout.next()),

    # To suspend linux
    Key([mod], "F9", lazy.spawn("systemctl suspend -i")),

    # To reboot linux
    Key([mod], "F10", lazy.spawn("systemctl reboot")),

    # To shutdown computer
    Key([mod], "F11", lazy.spawn("systemctl poweroff")),
]



groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])



layouts = [
    layout.Columns(
        border_width = 0,
        border_focus = '#ffffff',
        border_focus_stack = 'ffffff',
        border_normal = '#000000',
        change_size = 10,
        margin = 16
        ),
    # layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=3,
)

extension_defaults = widget_defaults.copy()

screens = [
    # Primary screen
    Screen(
        wallpaper='~/.config/qtile/background.jpg',
        wallpaper_mode='stretch',
        top=bar.Bar(
            [
                #widget.CurrentLayout(),
                widget.Spacer(length=6),
                widget.GroupBox(
                    background='#181815',
                    active='ffffff',
                    inactive='5d5f4f',
                    #this_current_screen_border='794cca',
                    #this_current_screen_border='bfbfbd',
                    this_current_screen_border='59595c',
                    this_screen_border='5d5f4f',
                    highlight_color='ffffff',
                    borderwidth=1,
                    foreground='#000000',
                    margin=2,
                ),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Systray(),
                widget.Volume(),
                #widget.Volume(volume_app="pavucontrol", background=soft, padding=0),
                #widget.Clock(format='%Y-%m-%d %a %H:%M'),   # 2022-12-30 18:30
                widget.Clock(format='-  %a, %b %d - %H:%M'),   # Sun, Dec 30 18:30
                #widget.QuickExit(),
                widget.Spacer(length=6),
            ],
            24,
            # Nort, East, South, West
            margin = [5, 5, 2, 5],
            # border_width=[1, 1, 1, 1], # Draw top and bottom borders
            # border_color=["#ffffff", "#ffffff", "#ffffff", "#ffffff"],  # Borders are magenta
            background = "130e0e"
        ),
    ),
    # Second screen
    Screen(
        top=bar.Bar(
            [
                #widget.CurrentLayout(),
                widget.Spacer(length=6),
                widget.GroupBox(
                    background='#181815',
                    active='ffffff',
                    inactive='5d5f4f',
                    this_current_screen_border='794cca',
                    this_screen_border='5d5f4f',
                    highlight_color='ffffff',
                    borderwidth=1,
                    foreground='#000000',
                    margin=2,
                    ),
                widget.Prompt(),
                widget.WindowName(),
                widget.Volume(device = 'default'),
                widget.Clock(format='%Y-%m-%d %a %I:%M %p'),
                widget.QuickExit(),
                widget.Spacer(length=6),
            ],
            24,
            # Nort, East, South, West
            margin = [5, 5, 2, 5],
            # border_width=[1, 1, 1, 1],  # Draw top and bottom borders
            # border_color=["#ffffff", "#ffffff", "#ffffff", "#ffffff"],  # Borders are magenta
            background = "130e0e"
        ),
    ),
    # Third screen
    Screen(
        top=bar.Bar(
            [
                #widget.CurrentLayout(),
                widget.Spacer(length=6),
                widget.GroupBox(
                    background='#181815',
                    active='ffffff',
                    inactive='5d5f4f',
                    this_current_screen_border='794cca',
                    this_screen_border='5d5f4f',
                    highlight_color='ffffff',
                    borderwidth=1,
                    foreground='#000000',
                    margin=2,
                    ),
                widget.Prompt(),
                widget.WindowName(),
                widget.Volume(device = 'default'),

                widget.Clock(format='%Y-%m-%d %a %I:%M %p'),
                widget.QuickExit(),
                widget.Spacer(length=6),
            ],
            24,
            # Nort, East, South, West
            margin = [5, 5, 2, 5],
            # border_width=[1, 1, 1, 1],  # Draw top and bottom borders
            # border_color=["#ffffff", "#ffffff", "#ffffff", "#ffffff"],  # Borders are magenta
            background = "130e0e"
        ),
    )
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

# Floating windows layout
floating_layout = layout.Floating(
        border_width=1,
        border_focus = '#000000',
        border_normal = '#000000',
# Define what windows should always be floating
# Run the utility of `xprop` to see the wm class and name of an X client.
        float_rules=[
    #*layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    Match(title='KeePassXC'), # KeePassXC
    Match(title='LibreOffice'), # LibreOffice
])

# Configuration variables
dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wmname = "qtile"

list_commands = [
        "setxkbmap -layout es",
        #"setxkbmap us",
        "picom --config ~/.config/picom/picom.conf &",
    ]

# Here I execute each command
for c in list_commands:
    os.system(c)

