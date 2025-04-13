lisq - from Polish 'foxie' is lightweight and opensource note taking app that work with .txt files <<

quit, q, exit
clear, cls   - clear screen
show, s      - show recent notes (default 10)
: show [int]   - show [integer] notes
: show [str]   - show notes containing [string]
: show all     - show all notes
: show random  - show random note
: del [str]    - delete notes containing [string]
: del last, l  - delete the last note
: del all      - delete all notes
: reiterate    - function to renumber notes ID
: path         - show the path to the notes file
: edit         - open notes file in editor

CLI: lisq [cmd] [arg] | lisq :: sample text
     alias lisq="python3 /file/path/lisq.py"

All rights reserved © funnut
