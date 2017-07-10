from flask import Flask, json, request
from video2gif import app
from video2gif.convert import convert_video


@app.route('/convert', methods=['POST'])
def convert_video():
    json_data = request.get_json(silent=True)

    path = json_data['path']
    times = json_data['times']
    gif_prefix = json_data['gif_prefix']
    size = json_data['size']
    fps = json_data['fps']

    clips = Clips(video_name, times, gif_prefix, size, fps)

    try:
        convert_video(clips)
    except:
        return False

    return True
