# Colors
TEXT_FG="\[\033[1;38;2;49;50;68m\]"

SAPPHIRE_FG="\[\033[1;38;2;116;199;236m\]"
SAPPHIRE_BG="\[\033[1;48;2;116;199;236m\]"

MAUVE_FG="\[\033[1;38;2;203;166;247m\]"
MAUVE_BG="\[\033[1;48;2;203;166;247m\]"

PINK_FG="\[\033[1;38;2;245;194;231m\]"
PINK_BG="\[\033[1;48;2;245;194;231m\]"

GREEN_FG="\[\033[1;38;2;166;227;161m\]"
GREEN_BG="\[\033[1;48;2;166;227;161m\]"


# Symbols
DIVIDER=$'\ue0b4';
TICK=$'\u2714';
CROSS=$'\u2718';
CORNER=$'\u2514\u2500'


# Custom prompt
function prompt_command { 
    PS1="${debian_chroot:+($debian_chroot)}$TEXT_FG$SAPPHIRE_BG \u@\h $SAPPHIRE_FG$MAUVE_BG$DIVIDER$TEXT_FG \w ";

    NEXT_DIVIDER_FG=$MAUVE_FG;

    CURRENT_GIT_BRANCH=$(git branch --show-current 2> /dev/null);
    if [ -n "$CURRENT_GIT_BRANCH" ]; then
        PS1="$PS1$NEXT_DIVIDER_FG$PINK_BG$DIVIDER$TEXT_FG git:$CURRENT_GIT_BRANCH";

        CURRENT_GIT_CHANGES=$(git status --short | wc -l);
        if [[ $CURRENT_GIT_CHANGES -ne 0 ]]; then
            PS1="$PS1 $CURRENT_GIT_CHANGES$CROSS ";
        else
            PS1="$PS1 $TICK ";
        fi;

        NEXT_DIVIDER_FG=$PINK_FG;
    fi;

    if [ -n "$CONDA_DEFAULT_ENV" ]; then
        PS1="$PS1$NEXT_DIVIDER_FG$GREEN_BG$DIVIDER$TEXT_FG conda:$CONDA_DEFAULT_ENV ";
        NEXT_DIVIDER_FG=$GREEN_FG;
    fi;

    PS1="$PS1$NEXT_DIVIDER_FG\[\033[1;49m\]$DIVIDER";
    PS1="$PS1\[\033[1;39;49m\]\n$CORNER \$ \[\033[0m\]"
}

export PROMPT_COMMAND=prompt_command

