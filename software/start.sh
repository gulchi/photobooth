#!/bin/bash
pushd `dirname $0` > /dev/null
SCRIPTPATH=`pwd -P`

echo $SCRIPTPATH
cancel -a Canon_CP1000
sleep 5

python photobooth.py --printhook=./print-hook.py
#python photobooth.py --printhook=./upload-hook.py
