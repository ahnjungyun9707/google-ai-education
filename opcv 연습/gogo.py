import cv2
import os
import shutil
import time
from datetime import datetime


width, height = 640, 480
fps = 30

MAX_STORAGE = 3 * 1024 * 1024 * 1024

base_dir = "blackbox_recordings"

if not os.path.exists(base_dir):
    os.makedirs(base_dir)

def get_current_folder():
    current_time = datetime.now().strftime("%Y%m%d-%H")
    folder_name = f"{base_dir}/{current_time}"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    return folder_name

def check_and_cleanup_storage():
    total_size = 0
    folders = sorted(os.listdir(base_dir))
    for folder in folders:
        folder_path = os.path.join(base_dir, folder)
        folder_size = sum(os.path.getsize(os.path.join(folder_path, f)) for f in os.listdir(folder_path))
        total_size += folder_size
        if total_size > MAX_STORAGE:
            shutil.rmtree(folder_path)
            total_size -= folder_size

def record_video():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("카메라를 열 수 없습니다.")
        return

    while True:
        folder_path = get_current_folder()
        current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{folder_path}/{current_time}.avi"

        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(filename, fourcc, fps, (width, height))

        start_time = time.time()
        while time.time() - start_time < 60:  
            ret, frame = cap.read()
            if ret:
                out.write(frame)
            else:
                break

        out.release()
        check_and_cleanup_storage()

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    record_video()
