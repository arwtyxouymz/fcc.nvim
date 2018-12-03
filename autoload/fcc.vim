"=============================================================================
" FILE: fcc.vim
" AUTHOR: Ryutaro Matsumoto <taross0524.ss at gmail.com>
" License: MIT license
"=============================================================================

function! fcc#initialize() abort
    let g:fcc#nest_num = get(g:, 'fcc#nest_num', 5)
    let g:fcc#catkin_ws = get(g:, 'fcc#catkin_ws', $HOME . "/catkin_ws")
endfunction
