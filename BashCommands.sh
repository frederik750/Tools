#!/bin/bash
function init(){
    cd /mnt/c/Users/frede/Documents/GitHub/
    python3 /mnt/c/Users/frede/Documents/GitHub/Tools/AutomateProjectMod/ProjectInit.py $1 #Path to script to run
}

function delete(){
    cd /mnt/c/Users/frede/Documents/GitHub/
    python3 /mnt/c/Users/frede/Documents/GitHub/Tools/AutomateProjectMod/ProjectRm.py $1
}