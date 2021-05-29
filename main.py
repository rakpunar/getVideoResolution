import os
from videoprops import get_video_properties
nameList = os.listdir()
props = get_video_properties
for name in nameList:
    if name[-3:] == "mp4" or name[-3:] == "mkv":
        print(f'{name}\n{props(name)["height"]}p')
