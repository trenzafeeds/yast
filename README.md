# Split Timer

## Usage
`python3 yast.py <timer_name>`

If `<timer_name>` does not yet exist, creates a new timer with the given name.
Otherwise, opens an existing save file with the name `timer_name.yast`, and resumes
from last save.

## Functionality
Default hotkeys as follows:

`insert` - Start/pause/resume timer.

`home` - Split timer

`end` - Unsplit timer (remove most recent split)

`f12` - Save current timer state to `timer_name.yast`, overwriting existing files with
the same name.

`f11` - Quit and close the timer, DOES NOT SAVE STATE. Note that this only works while the timer
is paused.

## Config

Hotkeys can be changed in `config.py`. Check pynput docs for correct formatting of keycodes.