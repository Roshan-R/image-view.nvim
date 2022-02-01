# image-view.nvim
A neovim plugin to preview images from the terminal using ueberzug

# Development

```
git clone https://github.com/Roshan-R/image-view.nvim
cd image-view.nvim
cp ~/.config/nvim/init.vim .
echo "let &runtimepath.=','.escape(expand('<sfile>:p:h'), '\,')" >> init.vim 
nvim -u init.vim
```
