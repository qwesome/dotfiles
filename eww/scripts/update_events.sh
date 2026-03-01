#!/usr/bin/env bash
source /home/orson/.config/eww/venv/bin/activate

events_text=$(/home/orson/.config/eww/venv/bin/python /home/orson/.config/eww/scripts/parse_ics.py)

eww update events="$events_text"

deactivate