return {
    'catppuccin/nvim',
    name = 'catppuccin',
    priority = 1000,

    config = function(opts)
        require('catppuccin').setup {
            flavour = 'mocha',
            transparent_background = true
        }

        vim.opt.background = 'dark'
        vim.cmd.colorscheme 'catppuccin'
    end
}

