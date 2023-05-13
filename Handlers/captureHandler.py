import numpy as np
import threading
from mss import mss
from PIL import Image
import time

class Capture:
    def __init__(self, x, y, xfov, yfov, monitor_index=1):
        self.x, self.y, self.xfov, self.yfov = x, y, xfov, yfov
        self.monitor_index = monitor_index
        self.screen = np.zeros((xfov, yfov, 3), np.uint8)
        self.pillow = None
        self.lock = threading.Lock()
        self.frame_count = 0
        self.start_time = time.time()
        self.start()

    def start(self):
        thread = threading.Thread(target=self.update, daemon=True)
        thread.start()

    def update(self):
        while True:
            with mss() as sct, self.lock:
                monitor = sct.monitors[self.monitor_index]
                monitor["top"] = self.y
                monitor["left"] = self.x
                monitor["width"] = self.xfov
                monitor["height"] = self.yfov
                self.pillow = sct.grab(monitor)
                self.screen = np.array(self.pillow)
                self.frame_count += 1
                elapsed_time = time.time() - self.start_time
                if elapsed_time >= 1:
                    fps = self.frame_count / elapsed_time
                    print(f" FPS: {fps:.0f} ", end="\r")
                    self.frame_count = 0
                    self.start_time = time.time()

    def get_screen(self):
        with self.lock:
            return self.screen

    def get_pillow(self):
        with self.lock:
            return Image.frombytes("RGB", self.pillow.size, self.pillow.bgra, "raw", "BGRX")
