from signal import signal, SIGINT
from unittest import result
import pyzed.sl as sl
from distutils.log import debug
import sys
import time
from pymavlink import mavutil
import scipy as sio
import threading
import zed
import logging

import sys
import pyzed.sl as sl
from signal import signal, SIGINT

logging.basicConfig(level=logging.DEBUG)


cam = sl.Camera()


def handler(signal_received, frame):
    cam.disable_recording()
    cam.close()
    sys.exit(0)


signal(SIGINT, handler)

# vehicle = mavutil.mavlink_connection('tcp:192.168.137.248:14550')
vehicle = mavutil.mavlink_connection('/dev/ttyACM0')
vehicle.wait_heartbeat()


# import threading


# class ThreadWithResult(threading.Thread):
#     def __init__(self, group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None):
#         def function():
#             self.result = target(*args, **kwargs)
#         super().__init__(group=group, target=function, name=name, daemon=daemon)


def get_command(keys):
    while True:
        time.sleep(0.1)
        try:
            message = vehicle.recv_match(type='RC_CHANNELS')
            if message != None:
                logging.info(message.to_dict()['chan7_raw'])
                keys = message.to_dict()['chan7_raw']
        except Exception as error:
            print(error)
            sys.exit(0)


if __name__ == "__main__":

    filename = time.strftime("%Y%m%d-%H%M%S.svo")

    # command=ThreadWithResult(target=get_command)
    # command.start()
    # command.join()
    # keys=command.result()
    # print(keys)

    keys = 0
    get_command(keys)
    print(keys)

    # init = sl.InitParameters()
    # init.camera_resolution = sl.RESOLUTION.HD720
    # init.depth_mode = sl.DEPTH_MODE.NONE

    # status = cam.open(init)
    # if status != sl.ERROR_CODE.SUCCESS:
    #     print(repr(status))
    #     exit(1)

    # recording_param = sl.RecordingParameters(
    #     filename, sl.SVO_COMPRESSION_MODE.H264)
    # err = cam.enable_recording(recording_param)
    # if err != sl.ERROR_CODE.SUCCESS:
    #     print(repr(status))
    #     exit(1)

    # runtime = sl.RuntimeParameters()
    # print("SVO is Recording, use Ctrl-C to stop.")
    # frames_recorded = 0

    # while True:
    #     if cam.grab(runtime) == sl.ERROR_CODE.SUCCESS:
    #         frames_recorded += 1
    #         print("Frame count: " + str(frames_recorded), end="\r")

    #     if
