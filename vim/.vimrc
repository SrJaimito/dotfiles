" No vi compatibility
set nocompatible

""""""""""""""""""""""""""""""""""" Plugins zone
filetype off

set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

Plugin 'VundleVim/Vundle.vim'

" My list of plugins
Plugin 'ycm-core/YouCompleteMe'

call vundle#end()
filetype plugin indent on
"""""""""""""""""""""""""""""""""""

" Syntax highlighting
syntax on

" Color scheme
set background=dark
colorscheme everforest

" Related to security for some reason
set modelines=0

" Show line number in current line, others are relative
set number
set relativenumber

" Show file stats
" set ruler

" Blink cursor on error, no sound (didn't like it so I will keep it disabled)
" set visualbell

" Encoding
set encoding=utf-8

" Indentation
set tabstop=4
set shiftwidth=4
set softtabstop=4
set expandtab
set autoindent

" YouCompleteMe config
let g:ycm_autoclose_preview_window_after_completion = 1

