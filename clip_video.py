import os
import sys
from moviepy.editor import *

def clip_video(input_file, width_percent, height_percent):
    # ビデオファイルを読み込む
    video = VideoFileClip(input_file)

    # 元の幅と高さを取得
    original_width, original_height = video.size

    # クリッピングする幅と高さを計算
    clip_width = int(original_width * (width_percent / 100))
    clip_height = int(original_height * (height_percent / 100))

    # クリッピングの開始座標を計算
    start_x = (original_width - clip_width) // 2
    start_y = (original_height - clip_height) // 2

    # クリッピングを実行
    clipped_video = video.crop(x1=start_x, y1=start_y, width=clip_width, height=clip_height)

    # 出力ファイル名を作成
    output_file = os.path.splitext(input_file)[0] + "-clipped" + os.path.splitext(input_file)[1]

    # クリッピングされたビデオを出力
    clipped_video.write_videofile(output_file)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python clip_video.py <input_file> <width_percent> <height_percent>")
        sys.exit(1)

    input_file = sys.argv[1]
    width_percent = float(sys.argv[2])
    height_percent = float(sys.argv[3])

    if 1 <= width_percent <= 100 and 1 <= height_percent <= 100:
        clip_video(input_file, width_percent, height_percent)
    else:
        print("Width and height percentages must be between 1 and 100.")
        sys.exit(1)
