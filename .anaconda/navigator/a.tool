#!/usr/bin/osascript
tell application "Terminal"
    activate
    do script ". /Users/yi-ruding/opt/anaconda3/bin/activate && conda activate /Users/yi-ruding/opt/anaconda3/envs/NLP; "
end tell
