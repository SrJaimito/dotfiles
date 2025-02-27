#!/usr/bin/env bash


polybar-msg cmd quit

echo "---" | tee -a /tmp/polybar_workspace.log
polybar workspace_bar 2>&1 | tee -a /tmp/polybar_workspace.log & disown

echo "---" | tee -a /tmp/polybar_info.log
polybar info_bar 2>&1 | tee -a /tmp/polybar_info.log & disown

