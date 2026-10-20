import json,sys
from faster_whisper import WhisperModel
m=WhisperModel("small",device="cpu",compute_type="int8")
segs,_=m.transcribe(sys.argv[1],language="en",word_timestamps=True)
W=[]
for s in segs:
    for w in s.words: W.append([w.word.strip(),round(w.start,2),round(w.end,2)])
json.dump(W,open(sys.argv[2],"w"))
print(" ".join(f"{w[0]}@{w[1]}" for w in W))
