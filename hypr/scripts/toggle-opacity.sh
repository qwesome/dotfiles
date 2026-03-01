#!/bin/bash

current=$(hyprctl activewindow -j | grep -o '"opacity":[0-9.]*' | cut -d: -f2)

case "$current" in
    0.05*) hyprctl dispatch setprop active opacity 1.0 ;;
    *)     hyprctl dispatch setprop active opacity 0.05 ;;
esac
