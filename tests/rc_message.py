import sys
import logging
import time
from pymavlink import mavutil

logging.basicConfig(level=logging.DEBUG)


# vehicle = mavutil.mavlink_connection('tcp:192.168.137.248:14550')
vehicle = mavutil.mavlink_connection('/dev/ttyACM0')
vehicle.wait_heartbeat()


if __name__ == "__main__":

    try:
        while True:
            time.sleep(0.1)
            message = vehicle.recv_match(type='RC_CHANNELS')
            if message != None:
                logging.info('Message on channel 7: {}'.format(
                    message.to_dict()['chan7_raw']))

    except Exception as error:
        print(error)
        sys.exit(0)
