#!/bin/bash


function ask_install {
    echo -n " [*] $1 [Y/n]"
    read -n 1 -r -s ANSWER

    echo -e -n "\r [*] $1 "

    if [[ $ANSWER =~ ^[Yy]$ || -z $ANSWER ]]
    then
        echo $'\u2714    '
        return 0
    else
        echo $'\u2718    '
        return 1
    fi
}


echo "Select installation:"

if ask_install Neovim; then
    cp -r .config/nvim ~/.config/.
fi

if ask_install "Custom bash prompt"; then
    echo -e "\n# Custom bash prompt" >> ~/.bashrc
    echo -e "source $(pwd)/.bashrc.prompt\n" >> ~/.bashrc
fi

if ask_install Qtile; then
    rm -rf ~/.config/qtile
    cp -r .config/qtile ~/.config/qtile
fi

if ask_install Kitty; then
    rm -rf ~/.config/kitty
    cp -r .config/kitty ~/.config/kitty
fi


