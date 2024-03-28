import cv2
import random
import os

def random_file(folder_path):
    files = os.listdir(folder_path)
    random_file = random.choice(files)
    return os.path.join(folder_path, random_file)

def select_random_frame(video_file, output_file):
    cap = cv2.VideoCapture(video_file)

    # 获取视频帧数
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # 随机选择一个帧索引
    random_frame_index = random.randint(0, frame_count - 1)

    # 设置帧索引
    cap.set(cv2.CAP_PROP_POS_FRAMES, random_frame_index)

    # 读取并返回随机选择的帧
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(output_file, frame)
    else:
        print("Error: 无法读取视频帧")
        return None
