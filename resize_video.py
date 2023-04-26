import sys
import os
from moviepy.editor import VideoFileClip

def resize_video(input_file, new_width):
    # 入力ファイルを読み込む
    clip = VideoFileClip(input_file)

    # アスペクト比を保持して横幅を変更する
    aspect_ratio = float(clip.h) / float(clip.w)
    new_height = int(new_width * aspect_ratio)
    resized_clip = clip.resize(width=new_width, height=new_height)

    # 出力ファイル名を生成する
    output_file = os.path.splitext(input_file)[0] + "-resized" + os.path.splitext(input_file)[1]

    # リサイズした動画を出力する
    resized_clip.write_videofile(output_file)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python resize_video.py <input_file> <new_width>")
        sys.exit(1)

    input_file = sys.argv[1]
    new_width = int(sys.argv[2])

    resize_video(input_file, new_width)
