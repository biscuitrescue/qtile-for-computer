import os
from libqtile.config import Screen 
from libqtile import layout, bar, widget, hook

colors =  [
    ["#1e1e2e90"],      # Colour 0
    ["#1e1e2e"],        # Colour 1
    ["#f28fad"],        # Colour 2
    ["#abe9b3"],        # Colour 3
    ["#fae3b0"],        # Colour 4
    ["#d6acff"],        # Colour 5
    ["#f5c2e7"],        # Colour 6
    ["#89DCEB"],        # Colour 7
    ["#F2779C"],        # Colour 8
    ["#b5e8e0"],        # Colour 9
    ["#ff6e6e"]]        # Colour 10


xx=13
xf="space mono for powerline bold"
default=[
                widget.CurrentLayoutIcon(
                    custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
                    scale=0.45,
                    padding=0,
                ),
                widget.TextBox(
                    text='|',
                    padding=0,
                    foreground=colors[5],
                ),
                widget.GroupBox(
                    font="space mono for powerline",
                    fontsize=13,
                    margin_y=3,
                    margin_x=4,
                    padding_y=5,
                    padding_x=4,
                    borderwidth=6,
                    active=colors[3],
                    inactive=colors[6],
                    rounded=True,
                    highlight_color=colors[0],
                    highlight_method="text",
                    this_current_screen_border=colors[2],
                    block_highlight_text_color=colors[0],
                ),
                widget.TextBox(
                    text='|',
                    padding=0,
                    foreground=colors[5],
                ),
                widget.Prompt(
                    background=colors[8],
                    foreground=colors[0],
                    font="Novamono for Powerline",
                    fontsize=16,
                ),


                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                        name_transform=lambda name: name.upper(),
                ),

                widget.WindowName(
                    fontsize=14,
                ),

                widget.Sep(
                    padding=6,
                    linewidth=0,
                    background=colors[0],
                ),
                widget.Systray(
                    background=colors[0],
                    icons_size=20,
                    padding=4,
                ),
                widget.Sep(
                    padding=6,
                    linewidth=0,
                    background=colors[0],
                ),
                widget.TextBox(
                    text='|',
                    fontsize='16',
                    padding=0,
                    background=colors[0],
                    foreground=colors[8],
                ),
                widget.Sep(
                    padding=6,
                    linewidth=0,
                    background=colors[0],
                ),
                widget.TextBox(
                    text="",
                    font="FontAwesome",
                    foreground=colors[8],
                    background=colors[0],
                    padding=0,
                    fontsize=16
                ),
                widget.Memory(
                    background=colors[0],
                    foreground=colors[8],
                    font="novamono for powerline",
                    fontsize=14,
                    format='{MemUsed: .0f} MB'
                ),
                widget.Sep(
                    padding=6,
                    linewidth=0,
                    background=colors[0],
                ),
                widget.TextBox(
                    text='|',
                    fontsize='16',
                    padding=0,
                    background=colors[0],
                    foreground=colors[6],
                ),
                widget.Sep(
                    padding=6,
                    linewidth=0,
                    background=colors[0],
                ),
                widget.TextBox(
                    text="  ",
                    font="FontAwesome",
                    foreground=colors[6],
                    background=colors[0],
                    padding=0,
                    fontsize=18
                ),
                widget.CPU(
                    background=colors[0],
                    foreground=colors[6],
                    font="novamono for powerline",
                    fontsize=14,
                    format='CPU: {load_percent}%'
                ),
                widget.Sep(
                    padding=6,
                    linewidth=0,
                    background=colors[0],
                ),
                widget.TextBox(
                    text='|',
                    fontsize='16',
                    padding=0,
                    background=colors[0],
                    foreground=colors[9],
                ),
                widget.Sep(
                    padding=6,
                    linewidth=0,
                    background=colors[0],
                ),
                widget.Volume(
                    background=colors[0],
                    foreground=colors[9],
                    font="novamono for powerline",
                    fontsize=14,
                    mouse_callbacks={'Button3': lambda: qtile.cmd_spawn("pavucontrol")},
                ),
                widget.Sep(
                    padding=6,
                    linewidth=0,
                    background=colors[0],
                ),
                widget.TextBox(
                    text='|',
                    fontsize='16',
                    padding=0,
                    background=colors[0],
                    foreground=colors[2],
                ),
                widget.Sep(
                    padding=6,
                    linewidth=0,
                    background=colors[0],
                ),
                widget.TextBox(
                    text='  ',
                    font="fontawesome",
                    fontsize='14',
                    padding=0,
                    background=colors[0],
                    foreground=colors[2],
                ),
                widget.Clock(
                    font="novamono for powerline",
                    foreground=colors[2],
                    background=colors[0],
                    fontsize=14,
                    format='%d %b, %A',
                ),
                widget.Sep(
                    padding=6,
                    linewidth=0,
                    background=colors[0],
                ),
                widget.TextBox(
                    text='|',
                    fontsize='16',
                    padding=0,
                    background=colors[0],
                    foreground=colors[4],
                ),
                widget.Sep(
                    padding=6,
                    linewidth=0,
                    background=colors[0],
                ),
                widget.TextBox(
                    text='   ',
                    font="fontawesome",
                    fontsize='16',
                    padding=0,
                    background=colors[0],
                    foreground=colors[4],
                ),
                widget.Clock(
                    font="novamono for powerline",
                    foreground=colors[4],
                    background=colors[0],
                    fontsize=14,
                    format='%I:%M %p'
                ),
                widget.Sep(
                    padding=6,
                    linewidth=0,
                    background=colors[0],
                ),
                widget.TextBox(
                    text='|',
                    fontsize='16',
                    padding=0,
                    background=colors[0],
                    foreground=colors[7],
                ),
                widget.Sep(
                    padding=6,
                    linewidth=0,
                    background=colors[0],
                ),
]
if len(os.listdir("/sys/class/power_supply"))==0:
    default.append(
        widget.CapsNumLockIndicator(
            fontsize=xx,
            font=xf,
            foreground=colors[0],
            background=colors[4],
        )
    )
else:
    default.append(
        widget.Battery(
            fontsize=xx,
            font=xf,
            foreground=colors[0],
            low_percentage=0.3,
            low_background="#0ee9af",
            background=colors[4],
            low_foreground=colors[0],
            update_interval=1,
            charge_char='',
            discharge_char='',
            format=' {char} {percent:2.0%} ',
        ),
    )

screens = [
    Screen(
    top=bar.Bar(
        default,
        29,
        background=colors[0],
        foreground=colors[1],
        # margin=[4,6,8,6],
    ),
    ),
]
