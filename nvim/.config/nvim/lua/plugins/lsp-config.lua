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
                    'clangd',               -- C/C++
                    'jedi_language_server', -- Python
                    'rust_analyzer',        -- Rust
                    'vhdl_ls',              -- VHDL
                    'bashls',               -- Bash
                    'ltex',                 -- LaTeX
                    'marksman',             -- Markdown
                    'verible',              -- Verilog/SystemVerilog
                }
            }
        end
    },
    {
        'neovim/nvim-lspconfig',
        lazy = false,

        config = function()
            vim.lsp.config('*', {
                capabilities = require('cmp_nvim_lsp').default_capabilities()
            })

            vim.lsp.enable({
                'clangd',
                'jedi_language_server',
                'rust_analyzer',
                'vhdl_ls',
                'verible',
                'bashls',
                'ltex',
                'marksman',
            })

            vim.api.nvim_create_autocmd('LspAttach', {
                callback = function(ev)
                    local opts = { noremap = true, silent = true, buffer = ev.buf }
                    vim.keymap.set('n', 'gD', vim.lsp.buf.declaration, opts)
                    vim.keymap.set('n', 'gd', vim.lsp.buf.definition, opts)
                    vim.keymap.set('n', 'gri', vim.lsp.buf.implementation, opts)
                    vim.keymap.set('n', '<leader>e', vim.diagnostic.open_float, opts)
                end
            })
        end
    }
}

