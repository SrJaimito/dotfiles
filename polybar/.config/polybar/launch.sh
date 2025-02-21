#!/usr/bin/env bash


polybar-msg cmd quit

echo "---" | tee -a /tmp/polybar_primary.log
polybar primary 2>&1 | tee -a /tmp/polybar_primary.log & disown

