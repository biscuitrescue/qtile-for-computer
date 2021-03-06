set -x EDITOR nvim
set fish_greeting
set -x MANPAGER "nvim -c 'set ft=man' -"


fish_vi_key_bindings

alias ll='exa -al --color=always --group-directories-first' # my preferred listing
alias la='exa -a --color=always --group-directories-first'  # all files and dirs
alias ls='exa -l --color=always --group-directories-first'  # long format
alias lt='exa -aT --color=always --group-directories-first' # tree listing
alias l.='exa -a | egrep "^\."'
alias vim='nvim'
alias rm='rm -i'

colorscript random
