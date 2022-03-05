colors =  [

        ["#292d3e", "#292d3e"], # color 0
        ["#A8A8A8", "#A8A8A8"], # color 1
        ["#f99db3", "#f99db3"], # color 2
        ["#b1b6ff", "#b1b6ff"], # color 3
        ["#f984a0", "#f984a0"], # color 4
        ["#ffffff", "#ffffff"], # color 5
        ["#B9BCDF", "#B9BCDF"], # color 6
        ["#f9678a", "#f9678a"], # color 7
        ["#c6c9ef", "#c6c9ef"], # color 8
        ["#bbebca", "#bbebca"]] # color 9

widget_defaults = dict(
    font='novamono for Powerline',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
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
                    # hide_unused=True,
                    margin_y=3,
                    margin_x=4,
                    padding_y=5,
                    padding_x=4,
                    borderwidth=6,
                    active=colors[9],
                    inactive=colors[1],
                    rounded=True,
                    highlight_color=colors[0],
                    highlight_method="text",
                    this_current_screen_border=colors[4],
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
                widget.CapsNumLockIndicator(
                    background=colors[0],
                    foreground=colors[7],
                    font="novamono for powerline bold",
                    fontsize=14,
                ),
                widget.Sep(
                    padding=6,
                    linewidth=0,
                    background=colors[0],
                ),
            ],
        31,
            opacity=0.9,
            background=colors[0],
            # margin=[4,4,0,4]
            ),
       ),
    ]
#############################################
############# AUTOSTART #####################
#############################################
@hook.subscribe.startup_once
def autostart():
    processes = [
        ['nm-applet'],
        ['picom'],
    ]

    for p in processes:
        subprocess.Popen(p)


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(

    border_focus="#ffffff",
    border_width=0,
    float_rules=[
    *layout.Floating.default_float_rules,
    Match(title='Confirmation'),      # tastyworks exit box
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
    {'wmclass': 'About Tor - Tor Browser'},
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
