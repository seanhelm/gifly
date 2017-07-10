import sys
import imageio
imageio.plugins.ffmpeg.download()

from video2gif.clips import Clips
from moviepy.editor import *
from moviepy.video.fx.all import *


def convert_video(clips):
    video = VideoFileClip(clips.path).resize(size)

    for i in range(0, len(clips.times)):
        clip = video.subclip(clips.times[i][0], clips.times[i][1])
        clip.write_gif(clips.gif_prefix + str(i+1) + '.gif', fps=clips.fps)


if __name__ == '__main__':
    size = 0.3
    fps = 20
    gif_prefix = 'clips/clip'
    video_name = 'video.mp4'

    times = [
    [(1, 20.00), (1, 22.00)],
    [(8, 27.00), (8, 29.00)],
    [(1, 45.00), (1, 47.00)],
    [(7, 34.00), (7, 36.00)]
    ]

    clips = Clips(video_name, times, gif_prefix, size, fps)

    convert_video(clips)
