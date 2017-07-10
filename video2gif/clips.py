class Clips():
    def __init__(self, path, times, gif_prefix, size, fps):
        self.path = path
        self.times = times
        self.gif_prefix = gif_prefix
        self.size = size
        self.fps = fps

    def count_clips():
        return len(times)

    def __str__():
        return path + '> ' + gif_prefix + '[1-' + count_clips() + '].gif'
