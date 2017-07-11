from video2gif.convert import *
from video2gif.clips import *


if __name__ == '__main__':
    size = 0.3
    fps = 20
    gif_prefix = 'clips/clip'
    video_name = 'video.mp4'

    # Format: (Minute, Seconds.Milliseconds)
    times = [
    [(0, 0.00), (0, 0.00)],
    [(0, 0.00), (0, 0.00)],
    [(0, 0.00), (0, 0.00)],
    [(0, 0.00), (0, 0.00)]
    ]

    clips = Clips(video_name, times, gif_prefix, size, fps)

    convert_video(clips)
