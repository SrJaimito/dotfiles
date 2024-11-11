return {
    'nvim-telescope/telescope.nvim',
    branch = '0.1.x',
    dependencies = {
        'nvim-lua/plenary.nvim',
        'BurntSushi/ripgrep'
    },

    config = function()
        require('telescope').setup {
            pickers = {
                find_files = {
                    hidden = true,
                    file_ignore_patterns = { 'node_modules', '.git', '.venv' }
                },
                live_grep = {
                    additional_args = { '--hidden' },
                    file_ignore_patterns = { 'node_modules', '.git', '.venv' }
                }
            }
        }

        local builtin = require('telescope.builtin')
        vim.keymap.set('n', '<leader>ff', builtin.find_files)
        vim.keymap.set('n', '<leader>fg', builtin.live_grep)
        vim.keymap.set('n', '<leader>fb', builtin.buffers)
        vim.keymap.set('n', '<leader>fh', builtin.help_tags)
    end
}

