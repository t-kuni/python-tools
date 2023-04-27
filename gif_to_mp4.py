import os
import sys
from moviepy.editor import *

def convert_gif_to_mp4(input_file):
    # 入力ファイルのパスと同じ場所に出力ファイルを作成
    output_file = os.path.splitext(input_file)[0] + ".mp4"

    # GIFファイルを読み込み
    clip = VideoFileClip(input_file)

    # 読み込んだGIFファイルをMP4ファイルに変換
    clip.write_videofile(output_file, codec="libx264")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python gif_to_mp4.py <input_gif_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    if not input_file.lower().endswith(".gif"):
        print("Error: Input file must be a GIF file.")
        sys.exit(1)

    convert_gif_to_mp4(input_file)
