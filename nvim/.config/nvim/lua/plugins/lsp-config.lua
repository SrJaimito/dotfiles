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
                    'vhdl_ls',                      -- VHDL
                    'bashls',                       -- Bash
                    'ltex',                         -- LaTeX
                    'marksman',                     -- Markdown
                    'verible',                      -- Verilog/SystemVerilog
                    'zls'                           -- Zig
                }
            }
        end
    },
    {
        'neovim/nvim-lspconfig',
        lazy = false,

        config = function()
            local capabilities = require('cmp_nvim_lsp').default_capabilities()
            local lspconfig = require('lspconfig')

            lspconfig.clangd.setup({
                capabilities = capabilities
            })
            lspconfig.jedi_language_server.setup({
                capabilities = capabilities
            })
            lspconfig.rust_analyzer.setup({
                capabilities = capabilities
            })
            lspconfig.vhdl_ls.setup({
                capabilities = capabilities
            })
            lspconfig.verible.setup({
                capabilities = capabilities
            })
            lspconfig.bashls.setup({
                capabilities = capabilities
            })
            lspconfig.ltex.setup({
                capabilities = capabilities
            })
            lspconfig.marksman.setup({
                capabilities = capabilities
            })
            lspconfig.zls.setup({
                capabilities = capabilities
            })

            vim.g.zig_fmt_autosave = 0

            local opts = { noremap = true, silent = true }
            vim.keymap.set('n', 'gD', vim.lsp.buf.declaration, opts)
            vim.keymap.set('n', 'gd', vim.lsp.buf.definition, opts)
            vim.keymap.set('n', 'K', vim.lsp.buf.hover, opts)
            vim.keymap.set('n', 'gi', vim.lsp.buf.implementation, opts)
            vim.keymap.set('n', '<leader>e', vim.diagnostic.open_float, opts)
        end
    }
}

