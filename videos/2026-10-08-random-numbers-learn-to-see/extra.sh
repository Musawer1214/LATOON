#!/bin/bash
export PYTHONPATH=/workspace/work/pylib
cd /workspace/latoon/longform/2026-10-08-random-numbers-learn-to-see/src
for k in 4 2 3; do a=$((k*900)); b=$((a+900)); python3 render.py chunk $a $b ../chunks/c$(printf %03d $k).mp4 >> ../chunks/log_x.txt 2>&1; done
echo finished >> ../chunks/log_x.txt
