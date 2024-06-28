-- Encoding
vim.opt.encoding = 'utf-8'
vim.opt.fileencoding = 'utf-8'

-- Cursor style
vim.opt.guicursor = 'n-v-i-c:block'

-- Line numbers
vim.opt.number = true
vim.opt.relativenumber = true

-- Indentation
vim.opt.tabstop = 4
vim.opt.shiftwidth = 4
vim.opt.expandtab = true

-- Wrap lines
vim.opt.wrap = true
vim.opt.linebreak = true
vim.opt.breakindent = true

-- Highlight cursor line
vim.opt.cursorline = true

-- Search options
vim.opt.ignorecase = true
vim.opt.hlsearch = false

-- Leader key
vim.g.mapleader = ' '

-- Common mappings
vim.keymap.set('n', '<leader>o', 'O<Esc>o')
vim.keymap.set('n', '<leader>{', 'A {}<Esc>i<cr><Esc>O')

vim.keymap.set('n', '<A-j>', 'ddp')
vim.keymap.set('n', '<A-k>', 'ddkkp')

    -------------
    -- Plugins --
    -------------

local lazypath = vim.fn.stdpath('data') .. '/lazy/lazy.nvim'
if not vim.loop.fs_stat(lazypath) then
    vim.fn.system({
        'git',
        'clone',
        '--filter=blob:none',
        'https://github.com/folke/lazy.nvim.git',
        '--branch=stable',
        lazypath
    })
end
vim.opt.rtp:prepend(lazypath)

require('lazy').setup('plugins')

vim.api.nvim_create_user_command(
    "ToggleDiagnostic",
    function()
        local config = vim.diagnostic.config
        local vt = config().virtual_text
        config {
            virtual_text = not vt,
            underline = not vt,
            signs = not vt,
        }
    end,
    {
        desc = "Toggle diagnostics"
    }
)

