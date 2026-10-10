#!/bin/bash
cd /workspace/latoon/longform/2026-10-08-icecube-catching-a-ghost
ffmpeg -v error -y -progress /tmp/mux.progress -i video_noaudio.mp4 -i audio/mix.wav -map 0:v -map 1:a -c:v libx264 -preset veryfast -crf 21 -pix_fmt yuv420p -c:a aac -b:a 192k -shortest -movflags +faststart /tmp/icecube_final.mp4 2> /tmp/mux.err && cp /tmp/icecube_final.mp4 icecube-catching-a-ghost_final.mp4 && echo MUXDONE >> /tmp/mux.err
mkdir -p /workspace/work/upload
ffmpeg -v error -y -i /tmp/icecube_final.mp4 -vf "hqdn3d=3:3:6:6,scale=1280:720:flags=lanczos" -c:v libx264 -preset slow -b:v 220k -pass 1 -an -f mp4 -passlogfile /tmp/up2p /dev/null 2>>/tmp/mux.err && \
ffmpeg -v error -y -i /tmp/icecube_final.mp4 -vf "hqdn3d=3:3:6:6,scale=1280:720:flags=lanczos" -c:v libx264 -preset slow -b:v 220k -pass 2 -passlogfile /tmp/up2p -c:a aac -b:a 96k -movflags +faststart /tmp/icecube_long.mp4 2>>/tmp/mux.err && cp /tmp/icecube_long.mp4 /workspace/work/upload/icecube_long.mp4 && echo UPDONE >> /tmp/mux.err
