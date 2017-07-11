import sys
import imageio
imageio.plugins.ffmpeg.download()

from video2gif.clips import Clips
from moviepy.editor import *
from moviepy.video.fx.all import *


def convert_video(clips):
    '''Convert a video to multiple gifs of specific clips'''
    video = VideoFileClip(clips.path).resize(clips.size)

    for i in range(0, len(clips.times)):
        clip = video.subclip(clips.times[i][0], clips.times[i][1])
        clip.write_gif(clips.gif_prefix + str(i+1) + '.gif', fps=clips.fps)
