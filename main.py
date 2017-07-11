from video2gif.convert import *
from video2gif.clips import *


if __name__ == '__main__':
    size = 0.3
    fps = 20
    gif_prefix = 'clips/clip'
    video_name = 'slow.mp4'

    times = [
    [(0, 7.00), (0, 9.00)],
    [(0, 2.00), (0, 4.00)],
    [(3, 16.00), (3, 18.00)],
    [(9, 0.00), (9, 02.00)]
    ]

    clips = Clips(video_name, times, gif_prefix, size, fps)

    convert_video(clips)
