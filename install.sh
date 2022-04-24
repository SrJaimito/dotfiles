# This script installs all the dotfiles in their corresponding locations

# Vim
echo -n "Vim configuration... "
if ln -sf $(pwd)/vim/.vimrc $HOME/.vimrc &> /dev/null ; then
    echo "OK"
else
    echo "FAIL"
fi

