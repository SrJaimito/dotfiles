return {
    {
        'williamboman/mason.nvim',

        config = function()
            require('mason').setup()
        end
    },
    {
        'williamboman/mason-lspconfig.nvim',

        config = function()
            require('mason-lspconfig').setup {
                ensure_installed = {
                    'clangd',                       -- C/C++
                    'jedi_language_server',         -- Python
                    'rust_analyzer',                -- Rust
                    'svlangserver',                 -- SystemVerilog
                    'bashls',                       -- Bash
                    'ltex',                         -- LaTeX
                    'autotools_ls',                 -- Make
                    'marksman',                     -- Markdown
                }
            }
        end
    },
    {
        'neovim/nvim-lspconfig',

        config = function()
            local lspconfig = require('lspconfig')

            lspconfig.clangd.setup({})
            lspconfig.jedi_language_server.setup({})
            lspconfig.rust_analyzer.setup({})
            lspconfig.svlangserver.setup({})
            lspconfig.bashls.setup({})
            lspconfig.ltex.setup({})
            lspconfig.autotools_ls.setup({})
            lspconfig.marksman.setup({})
        end
    }
}

