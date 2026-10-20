#!/bin/bash
# concat 3D segments -> crossfade into the engine end card (57.05 s, 0.45 s) -> mux mix_en.wav -> watermark -> delivery encode
set -e; cd "$(dirname "$0")"; rm -f /tmp/aidk_fin_done
ls three/segs/f*.mp4 | sort | sed "s#three/segs/#file '#; s#\$#'#" > three/segs/list.txt
(cd three/segs && ffmpeg -y -loglevel error -f concat -safe 0 -i list.txt -c copy /tmp/aidk_3d.mp4)
ffmpeg -y -loglevel error -i /tmp/aidk_3d.mp4 -i endcard/endcard.mp4 -filter_complex "[0:v][1:v]xfade=transition=fade:duration=0.45:offset=57.05,format=yuv420p[v]" -map "[v]" -c:v libx264 -preset veryfast -crf 12 /tmp/aidk_v.mp4
ffmpeg -y -loglevel error -i /tmp/aidk_v.mp4 -i mix_en.wav -map 0:v -map 1:a -c:v copy -c:a pcm_s24le -t 59.5 /tmp/aidk_master.mov
python3 wm_local.py /tmp/aidk_master.mov /tmp/aidk_wm.mov --corners tl,tr > /tmp/aidk_wm.log 2>&1
ffmpeg -y -loglevel error -i /tmp/aidk_wm.mov -c:v libx264 -preset slow -crf 20 -maxrate 4.2M -bufsize 8.4M -pix_fmt yuv420p -profile:v high -r 30 -c:a aac -b:a 192k -ar 48000 -movflags +faststart /tmp/AI_I_Dont_Know_sample.mp4
cp /tmp/AI_I_Dont_Know_sample.mp4 AI_I_Dont_Know_sample.mp4
echo OK > /tmp/aidk_fin_done
