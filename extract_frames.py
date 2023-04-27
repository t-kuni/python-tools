import argparse
import os
import cv2


def extract_frames(input_file, multiple_of_x):
    video = cv2.VideoCapture(input_file)

    # 入力ファイル名から拡張子を削除し、フォルダ名を作成
    output_folder = os.path.splitext(input_file)[0]

    # フォルダが存在しない場合、作成
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    frame_number = 0
    while True:
        ret, frame = video.read()

        # 動画が終わった場合、ループを抜ける
        if not ret:
            break

        # Xの倍数フレームの画像を書き出す
        if frame_number % multiple_of_x == 0:
            output_path = os.path.join(output_folder, f"{frame_number}.png")
            cv2.imwrite(output_path, frame)
            print(f"Extracted frame {frame_number} and saved as {output_path}")

        frame_number += 1

    video.release()
    print("Extraction completed.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract every X multiple frames from a video.")
    parser.add_argument("input_file", type=str, help="Input video file (mp4)")
    parser.add_argument("multiple_of_x", type=int, help="Multiple of X to extract frames")

    args = parser.parse_args()

    extract_frames(args.input_file, args.multiple_of_x)
