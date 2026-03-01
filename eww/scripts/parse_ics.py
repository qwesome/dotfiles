#!/usr/bin/env python3
import json
from ics import Calendar
from datetime import datetime

with open("/home/orson/.config/eww/calendar.ics") as f:
    c = Calendar(f.read())

# Get the current time in your local timezone
now = datetime.now().astimezone()

events_list = []
for e in c.events:
    # Convert the event time to your local timezone to avoid UTC mismatch
    event_time = e.begin.astimezone()
    
    # Check if the event is TODAY and hasn't happened yet
    if event_time.date() == now.date() and event_time > now:
        events_list.append({
            "time_str": event_time.strftime('%H:%M'),
            "name": e.summary,
            "timestamp": event_time.timestamp() # True chronological value
        })

# Sort events by their actual timestamp, not their formatted text string
events_list.sort(key=lambda x: x["timestamp"])

# Build the final clean list to send to Eww
final_output = []
for ev in events_list:
    final_output.append({
        "time": ev["time_str"],
        "name": ev["name"]
    })

# Output the JSON array
print(json.dumps(final_output))