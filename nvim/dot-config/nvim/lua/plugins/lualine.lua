return {
    'nvim-lualine/lualine.nvim',

    dependencies = {
        'nvim-tree/nvim-web-devicons'
    },

    options = {
        theme = '16color'
    },

    config = function()
        require('lualine').setup()
    end
}

