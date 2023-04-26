import cv2
import sys

def extract_first_frame(input_video, output_image):
    # 動画を読み込む
    video = cv2.VideoCapture(input_video)

    # 最初のフレームを読み込む
    ret, frame = video.read()

    # フレームが読み込まれた場合、画像を保存する
    if ret:
        cv2.imwrite(output_image, frame)
    else:
        print("Failed to read the video file.")

    # 動画を解放する
    video.release()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python extract_first_frame.py <input_video> <output_image>")
        sys.exit(1)

    input_video = sys.argv[1]
    output_image = sys.argv[2]

    extract_first_frame(input_video, output_image)