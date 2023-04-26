import sys
import os
from moviepy.editor import *

def cut_video(input_file, start_time, end_time):
    # Load video
    video = VideoFileClip(input_file)

    # Cut video
    short_video = video.subclip(start_time, end_time)

    # Generate output file name
    input_dir, input_file_name = os.path.split(input_file)
    input_file_base, input_file_ext = os.path.splitext(input_file_name)
    output_file_name = f"{input_file_base}-shortened{input_file_ext}"
    output_file = os.path.join(input_dir, output_file_name)

    # Write the output file
    short_video.write_videofile(output_file)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python cut_video.py <input_file> <start_time> <end_time>")
        sys.exit(1)

    input_file = sys.argv[1]
    start_time = float(sys.argv[2])
    end_time = float(sys.argv[3])

    cut_video(input_file, start_time, end_time)
