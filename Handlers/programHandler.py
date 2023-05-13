import cv2
import numpy as np
import threading
import time
import win32api

from captureHandler import Capture
from mouseHandler import Mouse
from settingsHandler import GetSettings


class Program:
    LOWER_COLOR = np.array([140, 120, 180])
    UPPER_COLOR = np.array([160, 200, 255])

    settings = GetSettings()
    ARDUINO_MOUSE = Mouse()

    def __init__(self, CENTER_X, CENTER_Y):

        self.SETTINGS_TARGET_BONE = self.settings.GetSettingsTargetBone()
        self.SETTINGS_X_FOV = self.settings.GetSettingsXFov()
        self.SETTINGS_Y_POV = self.settings.GetSettingsYFov()

        self.AIMBOT_ENABLED = self.settings.GetAimbotEnabled()
        self.AIMBOT_KEY_BIND = self.settings.GetAimbotKeyBind()
        self.AIMBOT_X_SPEED = self.settings.GetAimbotXSpeed()
        self.AIMBOT_Y_SPEED = self.settings.GetAimbotYSpeed()

        self.TRIGGERBOT_ENABLED = self.settings.GetTriggerbotEnabled()
        self.TRIGGERBOT_KEY_BIND = self.settings.GetTriggerbotKeyBind()
        self.TRIGGERBOT_X_THRESHOLD = self.settings.GetTriggerbotXThreshold()
        self.TRIGGERBOT_Y_THRESHOLD = self.settings.GetTriggerbotYThreshold()
        self.TRIGGERBOT_DELAY_BEFORE = self.settings.GetTriggerbotDelayBefore()
        self.TRIGGERBOT_DELAY_AFTER = self.settings.GetTriggerbotDelayAfter()

        self.SILENTBOT_ENABLED = self.settings.GetSilentbotEnabled()
        self.SILENTBOT_KEY_BIND = self.settings.GetSilentbotKeyBind()
        self.SILENTBOT_ONLY_FLICK = self.settings.GetSilentbotOnlyFlick()
        
        self.FLICKSPEED = self.settings.GetFlickSpeed()
        self.GRABBER = Capture(CENTER_X - self.SETTINGS_X_FOV // 2, CENTER_Y - self.SETTINGS_Y_POV // 2, self.SETTINGS_X_FOV, self.SETTINGS_Y_POV)

        threading.Thread(target=self.listen, daemon=True).start()
        
        self.TOGGLED = False

        if self.SETTINGS_TARGET_BONE == 'HEAD':
            self.y_offset = 6
        elif self.SETTINGS_TARGET_BONE == 'NECK':
            self.y_offset = 12
        elif self.SETTINGS_TARGET_BONE == 'BODY':
            self.y_offset = 25
        else:
            self.y_offset = 6

    def toggle(self):
        self.TOGGLED = not self.TOGGLED
        time.sleep(0.2)

    def listen(self):
        while True:
            if win32api.GetAsyncKeyState(self.AIMBOT_KEY_BIND) < 0 and self.TOGGLED and self.AIMBOT_ENABLED:
                self.process("move")
            elif win32api.GetAsyncKeyState(self.TRIGGERBOT_KEY_BIND) < 0 and self.TOGGLED and self.TRIGGERBOT_ENABLED:
                self.process("click")
            elif win32api.GetAsyncKeyState(self.SILENTBOT_KEY_BIND) < 0 and self.TOGGLED and self.SILENTBOT_ENABLED:
                self.process("flick")

    def process(self, action):
        hsv = cv2.cvtColor(self.GRABBER.get_screen(), cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, self.LOWER_COLOR, self.UPPER_COLOR)
        kernel = np.ones((3, 3), np.uint8)
        dilated = cv2.dilate(mask, kernel, iterations=5)
        thresh = cv2.threshold(dilated, 60, 255, cv2.THRESH_BINARY)[1]
        contours, _ = cv2.findContours(
            thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        if contours:
            max_contour = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(max_contour)
            center = (x + w // 2, y + h // 2)

            cX = center[0]
            cY = y + self.y_offset
            cYcenter = center[1] - self.GRABBER.YFOV // 2
            x_diff = cX - self.GRABBER.XFOV // 2
            y_diff = cY - self.GRABBER.YFOV // 2

            if action == "move":
                self.ARDUINO_MOUSE.move(
                    x_diff * self.X_SPEED, y_diff * self.Y_SPEED)

            elif action == "click":
                x_threshold = self.settings.get_int(
                    'TRIGGERBOT', 'X_THRESHOLD')
                y_threshold = self.settings.get_int(
                    'TRIGGERBOT', 'Y_THRESHOLD')
                if abs(x_diff) <= x_threshold and abs(cYcenter) <= y_threshold:
                    time.sleep(self.settings.get_float(
                        'TRIGGERBOT', 'DELAY-BEFORE-SHOOT'))
                    self.ARDUINO_MOUSE.click()
                    time.sleep(self.settings.get_float(
                        'TRIGGERBOT', 'DELAY-AFTER-SHOOT'))

            elif action == "flick":
                flickx = x_diff * self.FLICKSPEED
                flicky = y_diff * self.FLICKSPEED
                self.ARDUINO_MOUSE.move(flickx, flicky)
                self.ARDUINO_MOUSE.click()
                if not self.SILENTBOT_ONLYFLICK:
                    self.ARDUINO_MOUSE.move(-(flickx), -(flicky))
