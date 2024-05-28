#!/bin/bash


function ask_install {
    echo -n "[*] $1 [Y/n]"
    read -n 1 -r -s ANSWER

    echo -e -n "\r [*] $1 "

    if [[ $ANSWER =~ ^[Yy]$ || -z $ANSWER ]]
    then
        echo -e "\xE2\x9C\x94    "
        return 0
    else
        echo -e "\xE2\x9D\x8C    "
        return 1
    fi
}


echo "Select updates:"

if ask_install Neovim
then
    rm -rf .config/nvim
    cp -r ~/.config/nvim .config/.
fi

