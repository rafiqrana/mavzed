from signal import signal, SIGINT
from unittest import result
# import pyzed.sl as sl
from distutils.log import debug
import sys
import time
from pymavlink import mavutil
import scipy as sio
import threading
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

vehicle = mavutil.mavlink_connection('/dev/ttyACM0')
vehicle.wait_heartbeat()


def main():
    init = sl.InitParameters(camera_fps=30)
    init.camera_resolution = sl.RESOLUTION.HD720
    init.depth_mode = sl.DEPTH_MODE.NONE

    runtime = sl.RuntimeParameters()

    frames_recorded = 0
    button_pwm = 982
    cam_switch = 982

    # thrad1 = threading.Thread(target=get_command)

    record_status = cam.get_recording_status()

    while True:

        # time.sleep(0.1)
        message = vehicle.recv_match(type='RC_CHANNELS')
        if message != None:
            #     continue
            # else:
            button_pwm = message.to_dict()['chan7_raw']
            cam_switch = message.to_dict()['chan8_raw']
            logging.info(button_pwm)
            logging.info(cam_switch)

        # thrad1.start()
        # thrad1.join()

        if cam_switch == 982 and cam.is_opened():
            cam.disable_recording()
            cam.close()

        if cam_switch == 982 and not cam.is_opened():
            continue

        if cam_switch == 1495 and not cam.is_opened():
            status = cam.open(init)
            if status != sl.ERROR_CODE.SUCCESS:
                print(repr(status))
                exit(1)
        record_status = cam.get_recording_status()
        if button_pwm == 982 and record_status.is_recording:
            err = cam.disable_recording()
            frames_recorded = 0
            # cam.close()
            # sys.exit(0)
        if button_pwm == 1495 and not record_status.is_recording:
            filename = time.strftime(
                "/home/nito/Desktop/SVO-Recording/%Y%m%d-%H%M%S.svo")
            recording_param = sl.RecordingParameters(
                filename, sl.SVO_COMPRESSION_MODE.H264)
            err = cam.enable_recording(recording_param)
            logging.info('Enabling camera.')
            if err != sl.ERROR_CODE.SUCCESS:
                print(repr(status))
                exit(1)
        record_status = cam.get_recording_status()

        if button_pwm == 1495:
            if cam.grab(runtime) == sl.ERROR_CODE.SUCCESS:
                frames_recorded += 1
                print("Frame count: " + str(frames_recorded), end="\r")
        if button_pwm == 2006 and record_status.is_paused:
            # err = cam.pause_recording(False)
            logging.info('Puased recording!')
        # if button_pwm == 1495 and not record_status.is_paused:
        #     err = cam.pause_recording(True)


if __name__ == "__main__":

    try:
        main()

    except Exception as error:
        print(error)
        sys.exit(0)
