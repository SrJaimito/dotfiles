# Custom prompt
function prompt_command { 
    DIVIDER=$'\ue0b4';
    TICK=$'\u2714';
    CROSS=$'\u2718';
    # CORNER=$'\u2570\u2500';
    CORNER=$'\u2514\u2500'

    BLACK_FG="\[\033[38;2;30;30;46m\]";
    PEACH_FG="\[\033[1;38;2;250;179;135m\]";
    PEACH_BG="\[\033[1;48;2;250;179;135m\]";
    BLUE_FG="\[\033[1;34m\]";
    BLUE_BG="\[\033[1;44m\]";
    PINK_FG="\[\033[1;35m\]";
    PINK_BG="\[\033[1;45m\]";
    GREEN_FG="\[\033[1;32m\]";
    GREEN_BG="\[\033[1;42m\]";

    PS1="${debian_chroot:+($debian_chroot)}$BLACK_FG$PEACH_BG \u@\h $PEACH_FG$BLUE_BG$DIVIDER$BLACK_FG \w ";

    NEXT_DIVIDER_FG=$BLUE_FG;

    if [ -n "$CONDA_DEFAULT_ENV" ]; then
        PS1="$PS1$NEXT_DIVIDER_FG$GREEN_BG$DIVIDER$BLACK_FG conda:$CONDA_DEFAULT_ENV ";
        NEXT_DIVIDER_FG=$GREEN_FG;
    fi;

    CURRENT_GIT_BRANCH=$(git branch --show-current 2> /dev/null);
    if [ -n "$CURRENT_GIT_BRANCH" ]; then
        PS1="$PS1$NEXT_DIVIDER_FG$PINK_BG$DIVIDER$BLACK_FG git:$CURRENT_GIT_BRANCH";

        CURRENT_GIT_CHANGES=$(git status --short | wc -l);
        if [[ $CURRENT_GIT_CHANGES -ne 0 ]]; then
            PS1="$PS1 $CURRENT_GIT_CHANGES$CROSS ";
        else
            PS1="$PS1 $TICK ";
        fi;

        NEXT_DIVIDER_FG=$PINK_FG;
    fi;

    PS1="$PS1$NEXT_DIVIDER_FG\[\033[1;49m\]$DIVIDER";
    PS1="$PS1\[\033[1;39;49m\]\n$CORNER \$ \[\033[0m\]"
}

export PROMPT_COMMAND=prompt_command

