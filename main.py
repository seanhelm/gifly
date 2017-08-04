from video2gif.convert import *
from video2gif.clips import *
import json

if __name__ == '__main__':
    size = 0.2
    fps = 20
    gif_prefix = 'clips/ultra'
    video_name = 'ultra.mp4'

    # Format: (Minute, Seconds.Milliseconds)
    times = [
    [(8, 6.00), (8, 9.00)],
    [(10, 55.00), (10, 58.00)],
    [(8, 52.00), (8, 55.00)],
    ]

    clips = Clips(video_name, times, gif_prefix, size, fps)

    convert_video(clips)
