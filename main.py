import cv2
import os
import sys

def export_frames_to_jpeg(video_file):
    # 動画ファイルの名前を取得
    video_name = os.path.splitext(os.path.basename(video_file))[0]

    # 動画ファイル名のディレクトリが存在しない場合、作成する
    if not os.path.exists(video_name):
        os.makedirs(video_name)

    # 動画ファイルを開く
    cap = cv2.VideoCapture(video_file)
    if not cap.isOpened():
        print("Could not open the video file.")
        return

    frame_count = 0
    while True:
        # フレームを読み込む
        ret, frame = cap.read()

        # フレームが存在しない場合、ループを抜ける
        if not ret:
            break

        # フレームをJPEGファイルとして保存する
        cv2.imwrite(f'{video_name}/frame_{frame_count:04d}.jpeg', frame)
        frame_count += 1

    # 動画ファイルを閉じる
    cap.release()
    print(f'Exported {frame_count} frames from {video_name} to JPEG images.')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python main.py <video_file_name>")
        sys.exit(1)

    video_file = sys.argv[1]
    export_frames_to_jpeg(video_file)
