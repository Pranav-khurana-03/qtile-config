#  ___ _____ ___ _     _____    ____ ___  _   _ _____ ___ ____ 
# / _ \_   _|_ _| |   | ____|  / ___/ _ \| \ | |  ___|_ _/ ___|
#| | | || |  | || |   |  _|   | |  | | | |  \| | |_   | | |  _ 
#| |_| || |  | || |___| |___  | |__| |_| | |\  |  _|  | | |_| |
# \__\_\|_| |___|_____|_____|  \____\___/|_| \_|_|   |___\____|

# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import os
import re
import socket
import subprocess
from libqtile import qtile
from libqtile.config import Click, Drag, Group, KeyChord, Key, Match, Screen, ScratchPad, DropDown
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import warnings
from libqtile.config import Match
from libqtile.layout.base import Layout
from libqtile.log_utils import logger
from libqtile.dgroups import simple_key_binder
from typing import List  # noqa: F401from typing import List  # noqa: F401
mod = "mod4"
myTerm = "alacritty"
myBrowser = "brave"

ScratchPad_options = {
        "height" : 0.8,
        "width" : 0.6,
        "x" : 0.2,
        "y" : 0.1,
        "on_focus_lost_hide" :False,
}
"""











"""
groups  = [
        ScratchPad("scratchpad", [
            DropDown(
                "term", 
                "alacritty",
                opacity = 0.95,
                **ScratchPad_options,
                ),
            DropDown(
                "qconf",
                "alacritty -e vim /home/pranavk/.config/qtile/config.py",
                opacity = 1,
                **ScratchPad_options
                )
            ]),
        Group("DEV", layout="monadtall"),
        Group("WWW", layout="max"),
        Group("ZOM", layout="floating", matches=[Match(wm_class=["zoom"])]),
        Group("CODE", layout="max", matches=[Match(wm_class=["code-oss"])]),
        Group("MAIL" , layout="monadtall", matches=[Match(wm_class=["mailspring"])]),
        Group("STU", layout="monadtall", matches=[Match(wm_class=["okular"])]),
        Group("NMP", layout="max"),
        Group("MISC", layout="max"),
        Group("GFX", layout="max"),
]

dgroups_key_binder = simple_key_binder("mod4")

#call("~/.config/startup.sh")
keys = [
    ### Scratchpad Keybindings ###
    Key([mod], "t", lazy.group['scratchpad'].dropdown_toggle('term')),
    Key([mod], "q", lazy.group['scratchpad'].dropdown_toggle('qconf')),
    

    ### Switch between windows ###
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),

    ### Change the placement of a Window ###
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),

    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),

    Key([mod, "shift"], "k", lazy.layout.shuffle_up(),
        desc="Move window down"),

    Key([mod, "shift"], "j", lazy.layout.shuffle_down()
        , desc="Move window up"),



    ### Change the size of Windows ###
    Key([mod, "control"], "h", lazy.layout.shrink(),
        desc="Grow window to the left"),

    Key([mod, "control"], "l", lazy.layout.grow(),
        desc="Grow window to the right"),

    Key([mod], "n", lazy.layout.normalize()
        , desc="Reset all window sizes"),
   

    #Key([mod], "f" )
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    #Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
     #   desc="Toggle between split and unsplit sides of stack"),
    
    ###Important Applications/Scripts ### 
    Key([mod], "Return", lazy.spawn(myTerm), desc="Launch terminal"),
    Key([mod], "b", lazy.spawn(myBrowser)),
    Key([mod], "s", lazy.group["NMP"].toscreen(), lazy.spawn("brave"), lazy.spawn("brave open.spotify.com")),
    Key([mod], "n", lazy.group["NMP"].toscreen(), lazy.spawn("brave"), lazy.spawn("brave netflix.com")),
    Key([mod], "i", lazy.spawn("infinity")),
    Key([mod], "r", lazy.spawn("rockerz")),
    Key([mod], "d", lazy.spawn("bluetoothctl power off")),
    Key([mod], "x", lazy.spawn("xscreensaver-command -lock")),
    Key([mod], "m", lazy.spawn("mailspring")),

    ### Toggle between different layouts ###
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "Tab", lazy.prev_layout(), desc="Toggle between layouts"),
    

    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"), #Kill a window

    ### Restarting and shutting down qtile ###
    Key([mod, "control"], "r", lazy.reload_config(), desc="Restart Qtile"), #Restart replaced with reload_config to prevent hanging error
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    


    ### Essential key-bindings for volume/brightness/play-pause ###
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer sset Master unmute"), lazy.spawn("amixer -q sset Master 5%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer sset Master unmute"), lazy.spawn("amixer -q sset Master 5%+")),
    #Key([], "XF86AudioPause", lazy.spawn("playerctl pause")),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86MonBrightnessUp", lazy.spawn("light -A 10")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("light -U 10")),
    

    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod, "shift"], "f", lazy.window.toggle_floating()),
    Key([mod], "Up", lazy.screen.next_group()),
    Key([mod], "Down", lazy.screen.prev_group()),

    ### Dmenu Scripts ###
    Key([mod, "shift"], "Return", 
            lazy.spawn("dmenu_run -i -l 0 -p 'Run: '")),
    Key([mod,"shift"], "e",
            lazy.spawn("dm-confedit")),
    Key([mod,"shift"], "c",
            lazy.spawn("dm-currencies")),
    Key([mod,"shift"], "x",
            lazy.spawn("dm-logout")),
    Key([mod,"shift"], "m",
            lazy.spawn("dm-man")),
    Key([mod,"shift"], "n",
            lazy.spawn("dm-note")),
    Key([mod,"shift"], "w",
            lazy.spawn("dm-wifi")
            ),
    Key([mod], "space", lazy.spawn("krunner")),
    ### Screenshot ###
    Key([mod, "shift"], "s", 
            lazy.spawn("flameshot gui"),
            desc="Screenshot"),

    Key([mod, "shift"], "p", 
            lazy.spawn("spectacle"),
            desc="Screenshot"),
    Key([mod, "control"], "s",
        lazy.spawn("shutter -f")),
]


layout_theme = {"border_width": 2,
                "margin": 5,
                "border_focus": "#30bbff",
                "border_normal": "#1D2330"
                }
class Floating(Layout):
    """
    Floating layout, which does nothing with windows but handles focus order
    """
    default_float_rules = [
        Match(wm_type="zoom"),
        Match(wm_type='utility'),
        Match(wm_type='notification'),
        Match(wm_type='toolbar'),
        Match(wm_type='splash'),
        Match(wm_type='dialog'),
        Match(wm_class='file_progress'),
        Match(wm_class='confirm'),
        Match(wm_class='dialog'),
        Match(wm_class='download'),
        Match(wm_class='error'),
        Match(wm_class='notification'),
        Match(wm_class='splash'),
        Match(wm_class='toolbar'),
    ]

    
floating_layout = {
            "border_width" : 0,
            "border_focus": "#30bbff",
            "border_normal": "#30bbff"
        }
colors = [ "#222222", # 0
           "#aaaaaa", # 1 background for current screen tab
           "#ffffff", # 2 font color for group names
           "#efaf00", # 3 Not used
           "#bf3f3f", # 4 border line color for 'other tabs' and color for 'odd widgets'
           "#1f2f5f", # 5 
           "#d75f5f", # 6 not used 
           "#4f76c7", # 7
           "#363636", # 8 color for the 'even widgets'
           "#30bbff", # 9
           "#8080fa", # 10
           "#1f0f2f"] # 11


layouts = [
    #layout.Columns(**layout_theme),
    layout.Max(**layout_theme),
    # Try more layouts by unleashing below layouts.
     layout.Stack(num_stacks=2, **layout_theme),
     #layout.Bsp(**layout_theme),
     #layout.Matrix(**layout_theme),
     layout.MonadTall(**layout_theme),
     layout.MonadWide(**layout_theme),
     layout.RatioTile(**layout_theme),
     #layout.Tile(**layout_theme),
     #  layout.TreeTab(**layout_theme,
     #                 active_bg = colors[4],
     #                 bg_color = colors[11],
     #     ),"""
    layout.VerticalTile(**layout_theme),
     #layout.Zoomy(**layout_theme),
    layout.Floating(**floating_layout),
]

widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(
                       linewidth = 0,
                       padding = 10,
                       foreground = colors[2],
                       background = colors[0]
                       ),
                widget.Image(
                    filename = "~/.config/qtile/icons/Manjaro-orange.png",
                    background = colors[0],
                    mouse_callbacks = {'Button1': lambda :qtile.cmd_spawn(myTerm + " -e killall qtile")},
                    scale = True,
                    padding = 5,
                    margin=2.5,
                    ),
                widget.Sep(
                    linewidth = 3,
                    foreground = colors[1],
                    background = colors[0],
                    padding = 15 
                    ),
                widget.GroupBox(
                       font = "ReadexPro Bold",
                       fontsize = 12,
                       #margin_y = 3,
                       #margin_x = 0,
                       #padding_y = 5,
                       #padding_x = 3,
                       #borderwidth = 3,
                       active = colors[9],
                       inactive = colors[1],
                       rounded = True,
                       highlight_color = colors[8],
                       highlight_method = "line",
                       this_current_screen_border = colors[4],
                       foreground = colors[1],
                       background = colors[0]
                    ),
                #widget.Prompt(),
                widget.Sep(
                    linewidth = 3,
                    foreground = colors[1],
                    background = colors[0],
                    padding = 15
                    ),
                widget.WindowName(
                    font = "ReadexPro",
                    fontsize = 12,
                    foreground = colors[9],
                    background = colors[0]
                    ),
                widget.TextBox(
                    text =  ' ',
                    fontsize = 46,
                    padding = -7,
                    background = colors[0],
                    foreground = colors[5]
                    ),
                widget.CurrentLayoutIcon(
                        background = colors[5],
                        foreground = colors[2],
                        scale = 0.75,
                        padding =3
                        ),
                widget.CurrentLayout(
                    background = colors[5],
                    foreground = colors[2],
                    fontsize = 12,
                    font = "ReadexPro"
                    ),
                widget.TextBox(
                       text = '',
                       background = colors[5],
                       foreground = colors[4],
                       padding = -7,
                       fontsize = 46,
                       ),
                widget.Memory(
                        foreground = colors[2],
                        background = colors[4],
                        fontsize = 12,
                        font = "ReadexPro",
                        format = 'Memory : {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
                        mouse_callbacks = {'Button1' : lambda : qtile.cmd_spawn(myTerm + " -e bashtop")}
                        ),
                widget.TextBox(
                        text = '',
                        fontsize = 46,
                        padding = -7,
                        foreground = colors[5],
                        background = colors[4],
                        ),
                widget.CPU(
                        foreground = colors[2],
                        background = colors[5],
                        fontsize = 12,
                        font = "ReadexPro",
                        format ='CPU {freq_current} GHz | {load_percent}%',
                        padding = 6,
                        mouse_callbacks = {'Button1' : lambda : qtile.cmd_spawn(myTerm + " -e bashtop")}
                        ),
                widget.TextBox(
                        foreground = colors[4],
                        background = colors[5],
                        text = '',
                        fontsize = 46,
                        padding = -7,
                        ),
                widget.BatteryIcon(
                        background = colors[4],
                        update_interval = 1,
                        ),
                widget.Battery(
                        foreground = colors[2],
                        background = colors[4],
                        charge_char = "↑",
                        full_char = "✓",
                        discharge_char = "↓",
                        unknown_char = "?",
                        format = '{percent:2.0%} ({char})',
                        fontsize = 12,
                        font = "ReadexPro",
                        padding = 6,
                        low_percentage = 0.1,
                        low_foreground = colors[2],
                        update_interval = 1,
                        notify_below = 0.2,
                        show_short_text = False,
                        ),
                widget.TextBox(
                        foreground = colors[5],
                        background = colors[4],
                        text = '',
                        fontsize = 46,
                        padding = -7,
                        ),
                widget.TextBox(
                        text = "Vol : ",
                        fontsize = 12,
                        font = "ReadexPro",
                        background = colors[5],
                        foreground = colors[2]
                        ),
                widget.Volume(
                        fontsize = 12,
                        font = "ReadexPro",
                        foreground = colors[2],
                        background = colors[5],
                        padding = 5
                        ),
                widget.TextBox(
                        fontsize = 46,
                        text = '',
                        foreground = colors[4],
                        background = colors[5],
                        padding = -7
                        ),
                widget.Wttr(
                        location = {'Noida': 'Noida'},
                        fontsize = 12,
                        font = "ReadexPro",
                        mouse_callbacks = {'Button1' : lambda : qtile.cmd_spawn("brave https://www.accuweather.com/en/in/noida/3146227/weather-forecast/3146227")},
                        format="%C%c %t",
                        foreground = colors[2],
                        background = colors[4],
                        update_interval = 1,
                        ),
                widget.TextBox(
                        fontsize = 46,
                        text = '',
                        foreground = colors[5],
                        background = colors[4],
                        padding = -7
                        ),
                widget.Wlan(
                        background = colors[5],
                        foreground = colors[2],
                        interface = 'wlp2s0',
                        font = "ReadexPro",
                        fontsize = 12,
                        padding = 5,
#                        margin_y = 10,
                    format="Wifi : {percent:2.0%}",
                        mouse_callbacks = {'Button1' : lambda : qtile.cmd_spawn("gnome-control-center")}
                        ),
                widget.TextBox(
                        fontsize = 46,
                        text = '',
                        foreground = colors[4],
                        background = colors[5],
                        padding = -7
                        ),
                widget.Clock(
                        fontsize = 12,
                        font = "ReadexPro",
                        foreground = colors[2],
                        background = colors[4],
                        format="%A %D %H:%M:%S",
                        padding = 5,
                        mouse_callbacks = {'Button1' : lambda : qtile.cmd_spawn("gnome-calendar")}
                        ),
                widget.Sep(
                    linewidth=3,
                    padding = 6,
                    foreground = colors[1],
                    background = colors[0]
                    ),
                widget.QuickExit(
                    font = "ReadexPro",
                    foreground = colors[6],
                    background = colors[0],
                    fontsize = 16,
                    default_text="⏻ ",
                    countdown_format='[ {} ]'
                ),
                widget.Sep(
                        background= colors[0],
                        padding = 0,
                        linewidth= 0,
                        ),
                #widget.TextBox("default config", name="default"),
                #widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                #widget.Systray(),
                #widget.Clock(format='%Y-%m-%d %a %I:%M %p'),
                #widget.QuickExit(),
            ],
            23,
        ),
    ),
]

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])
# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

#dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
bring_front_click = True
# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
