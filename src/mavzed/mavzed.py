import sys
import time
import logging

import pyzed.sl as sl

class Mavzed:
    def __init__(self) -> None:

        self.frame_count = 0

        self.camera = sl.Camera()
        self.init_param = sl.InitParameters(camera_fps=30)
        self.init_param.camera_resolution = sl.RESOLUTION.HD720
        self.init_param.depth_mode = sl.DEPTH_MODE.NONE

        self.runtime_param = sl.RuntimeParameters()

        self.file_path = "/home/nito/Desktop/SVO-Recording/%Y%m%d-%H%M%S.svo"

        self.recording_status = sl.RecordingStatus()
        self.error_code = 0

    def update_status(self):
        self.recording_status = self.camera.get_recording_status()

    def on(self):
        if not self.camera.is_opened():
            self.error_code = self.camera.open(self.init_param)
            if self.error_code != sl.ERROR_CODE.SUCCESS:
                print(repr(self.error_code))
                exit(1)
            self.update_status()

    def off(self):
        if self.camera.is_opened():
            self.camera.disable_recording()
            self.frame_count = 0
            self.camera.close()

    def start(self):
        if not self.recording_status.is_recording:
            filename = time.strftime(self.file_path)
            recording_param = sl.RecordingParameters(
                filename, sl.SVO_COMPRESSION_MODE.H264)
            self.error_code = self.camera.enable_recording(recording_param)
            self.recording_status.is_recording = True

            if self.error_code != sl.ERROR_CODE.SUCCESS:
                print(repr())
                exit(1)
        if self.recording_status.is_recording:
            if self.camera.grab(self.runtime_param) == sl.ERROR_CODE.SUCCESS:
                self.frame_count += 1
                print("Frame count: " + str(self.frame_count), end="\r")
        self.update_status()

    def stop(self):
        if self.recording_status.is_recording:
            self.camera.disable_recording()
            self.frame_count = 0

    def pause(self):
        # if not self.recording_status.is_paused:
        #     self.error_code = self.camera.pause_recording(False)
        #     self.recording_status.is_paused = True
        logging.debug('Recording paused!')
