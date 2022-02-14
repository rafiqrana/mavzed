import configparser
import logging
from pymavlink import mavutil
from configparser import ConfigParser

class ZED:
    class RECORDING:
        STOP = 982
        START = 1495
        PAUSE = 2006

    class POWER:
        OFF = 982
        ON = 1495


class COMMAND:
    POWER = 'POWER'
    RECORDING = 'RECORDING'


class Mavlink():
    def __init__(self, config = None) -> None:

        self.cam_power_channel = config['RC_CHANNEL']['cam_power_channel']
        self.cam_record_channel = config['RC_CHANNEL']['cam_record_channel']

        self.device_path = config['DEVICE_CONFIG']['device_path']

        self.mav = mavutil.mavlink_connection(self.device_path)
        self.mav.wait_heartbeat()

        self.command = {'POWER': 982, 'RECORDING': 982}

        logging.basicConfig(level=logging.ERROR,
                    format="%(asctime)s:%(levelname)s:%(message)s")


    def new_message(self):
        message = self.mav.recv_match(type='RC_CHANNELS')
        if message != None:
            self.command['POWER'] = message.to_dict()[self.cam_power_channel]
            self.command['RECORDING'] = message.to_dict()[
                self.cam_record_channel]
            logging.debug("Cam PWR Command: {}".format(self.command['POWER']))
            logging.debug('Cam REC Command: {}'.format(self.command['POWER']))
        return self.command
