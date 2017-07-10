import sys
import imageio
imageio.plugins.ffmpeg.download()

from moviepy.editor import *
from moviepy.video.fx.all import *


if __name__ == '__main__':
    size = 0.2
    fps = 20
    gif_prefix = 'clip'
    video_name = '~/Downloads/video.mp4'

    times = [
    [(0, 20.00), (0, 21.00)],
    [(0, 30.00), (0, 31.00)]
    ]

    video = VideoFileClip(video_name).resize(size)

    for i in range(0, len(times)):
        clip = video.subclip(times[i][0], times[i][1])
        clip.write_gif(gif_prefix + str(i) + '.gif', fps=fps)
