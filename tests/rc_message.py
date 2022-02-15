import sys
import logging
import time
from pymavlink import mavutil

logging.basicConfig(level=logging.DEBUG)


# vehicle = mavutil.mavlink_connection('tcp:192.168.137.248:14550')

serial_list = mavutil.auto_detect_serial()
serial_list.sort(key=lambda x: x.device)

# remove OTG2 ports for dual CDC
if len(serial_list) == 2 and serial_list[0].device.startswith("/dev/serial/by-id"):
    if serial_list[0].device[:-1] == serial_list[1].device[0:-1]:
        serial_list.pop(1)

print('Auto-detected serial ports are:')
for port in serial_list:
        print("%s" % port)

vehicle = mavutil.mavlink_connection(serial_list[0].device)
# vehicle = mavutil.mavlink_connection('/dev/ttyACM0')

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
