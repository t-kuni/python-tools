import sys
from moviepy.editor import *


def trim_video(input_file, start_time, end_time, output_file):
    video = VideoFileClip(input_file)
    trimmed_video = video.subclip(start_time, end_time)
    trimmed_video.write_videofile(output_file)


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python trim_video.py [input_file] [start_time] [end_time] [output_file]")
        sys.exit(1)

    input_file = sys.argv[1]
    start_time = float(sys.argv[2])
    end_time = float(sys.argv[3])
    output_file = sys.argv[4]

    trim_video(input_file, start_time, end_time, output_file)