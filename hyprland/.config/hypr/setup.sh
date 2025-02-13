#!/bin/bash

HYPRLAND_CONF_DIR="$HOME/dotfiles/hyprland/.config/hypr"

SINGLE_CONF_DIR="$HYPRLAND_CONF_DIR/single_monitor"
TWO_CONF_DIR="$HYPRLAND_CONF_DIR/two_monitors"

NUM_MONITORS=$(hyprctl monitors | grep -i "Monitor" | wc -l)

if [ "$NUM_MONITORS" -eq 2 ]; then
    cp "$TWO_CONF_DIR/hyprland.conf" "$HYPRLAND_CONF_DIR/hyprland.conf"
    cp "$TWO_CONF_DIR/hyprlock.conf" "$HYPRLAND_CONF_DIR/hyprlock.conf"
else
    cp "$SINGLE_CONF_DIR/hyprland.conf" "$HYPRLAND_CONF_DIR/hyprland.conf"
    cp "$SINGLE_CONF_DIR/hyprlock.conf" "$HYPRLAND_CONF_DIR/hyprlock.conf"
fi

hyprctl reload

