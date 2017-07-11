from flask import Flask, json, request, jsonify
from video2gif import app
from video2gif.convert import  *
from video2gif.clips import *


@app.route('/convert', methods=['POST'])
def convert():
    json_data = request.get_json()

    times = [[tuple(time[0]), tuple(time[1])] for time in json_data['times']]

    path = json_data['path']
    gif_prefix = json_data['gif_prefix']
    size = json_data['size']
    fps = json_data['fps']

    clips = Clips(path, times, gif_prefix, size, fps)

    gif_files = convert_video(clips)

    return jsonify(gif_files)
