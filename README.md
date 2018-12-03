# fcc.nvim

> The plugin for ROS that copy compile_commands.json to package directory


## Install
**Note:** fcc.nvim requires Neovim (0.3.0+ and of course, **latest** is
recommended).

For vim-plug

```viml
if has('nvim')
  Plug 'arwtyxouymz/fcc.nvim', { 'do': ':UpdateRemotePlugins' }
endif

For dein.vim

```viml
if has('nvim')
call dein#add('arwtyxouymz/fcc.nvim')
endif
```

For manual installation(not recommended)

1. Extract the files and put them in your Neovim or .vim directory
   (usually `$XDG_CONFIG_HOME/nvim/`).

### Requirements

fcc.nvim requires Neovim.

If `:echo has("python3")` returns `1`, then you have python 3 support; otherwise, see below.

You can enable Python3 interface with pip:

    pip3 install --user pynvim


## Configuration

```vim
" Settings catkin_ws.
let g:fcc#catkin_ws = <your workspace path>
let g:fcc#nest_num = 5  " the number of recursive
nmap <Leader><C-p> :<C-u>FindCompileCommands<CR>
```
