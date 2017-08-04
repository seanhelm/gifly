import sys
import imageio
imageio.plugins.ffmpeg.download()

from .clips import Clips
from moviepy.editor import *
from moviepy.video.fx.all import *


def convert_video(clips):
    '''Convert a video to multiple gifs of specific clips'''
    video = VideoFileClip(clips.path).resize(clips.size)

    gif_files = []

    for i in range(0, len(clips.times)):
        filename = clips.gif_prefix + str(i+1) + '.gif'
        gif_files.append(filename)

        clip = video.subclip(clips.times[i][0], clips.times[i][1])
        clip.write_gif(filename, fps=clips.fps)

    return gif_files
