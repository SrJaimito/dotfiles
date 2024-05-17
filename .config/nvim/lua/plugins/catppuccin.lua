return {
    'catppuccin/nvim',
    name = 'catppuccin',
    priority = 1000,

    config = function(opts)
        require('catppuccin').setup {
            flavour = 'macchiato',
            transparent_background = false
        }

        vim.opt.background = 'dark'
        vim.cmd.colorscheme 'catppuccin'
    end
}

