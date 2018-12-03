"=============================================================================
" FILE: util.vim
" AUTHOR: Ryutaro Matsumoto <taross0524.ss at gmail.com>
" License: MIT license
"=============================================================================

function! fcc#util#print_error(string) abort
    echohl Error | echomsg '[fcc.nvim] ' . a:string | echohl None
endfunction
function! fcc#util#echo(string) abort
    echohl None
    echon a:string
    echohl NONE
endfunction
