import sys
import os
import cv2
import ffmpeg

def reduce_frames(input_file, output_file, frame_multiplier):
    # Get input video framerate
    input_video_info = ffmpeg.probe(input_file)
    input_video_stream = next(stream for stream in input_video_info['streams'] if stream['codec_type'] == 'video')
    input_framerate = eval(input_video_stream['r_frame_rate'])

    # Calculate output video framerate
    output_framerate = input_framerate / frame_multiplier

    input_stream = ffmpeg.input(input_file)
    output_stream = input_stream.filter('fps', fps=output_framerate).output(output_file, r=output_framerate)
    ffmpeg.run(output_stream)

def main():
    if len(sys.argv) != 3:
        print("Usage: python reduce_frames.py <input_file> <frame_multiplier>")
        sys.exit(1)

    input_file = sys.argv[1]
    frame_multiplier = int(sys.argv[2])

    if frame_multiplier <= 0:
        print("Error: frame_multiplier must be a positive integer")
        sys.exit(1)

    input_file_path = os.path.abspath(input_file)
    input_file_dir = os.path.dirname(input_file_path)
    input_file_name, input_file_ext = os.path.splitext(os.path.basename(input_file_path))
    output_file_name = f"{input_file_name}-frame-catted{input_file_ext}"
    output_file_path = os.path.join(input_file_dir, output_file_name)

    reduce_frames(input_file_path, output_file_path, frame_multiplier)

if __name__ == "__main__":
    main()
