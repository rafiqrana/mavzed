import configparser
import os, sys, time

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from src.mavzed.mavlink import COMMAND, ZED, Mavlink
from src.mavzed.mavzed import Mavzed
from signal import signal, SIGINT

config = configparser.ConfigParser()
config.read('config/config.ini')

def main():

    try:
        mavlink = Mavlink(config)
        mavzed = Mavzed(config)

        while True:
            time.sleep(0.02)

            message = mavlink.new_message()

            if message[COMMAND.POWER] == ZED.POWER.ON:
                mavzed.on()
            elif message[COMMAND.POWER] == ZED.POWER.OFF:
                mavzed.off()
                continue

            if message[COMMAND.RECORDING] == ZED.RECORDING.START:
                mavzed.start()
            elif message[COMMAND.RECORDING] == ZED.RECORDING.STOP:
                mavzed.stop()
            elif message[COMMAND.RECORDING] == ZED.RECORDING.PAUSE:
                mavzed.pause()
                
    except Exception as error:
        print(error)
        sys.exit(0)

if __name__ == "__main__":

    def handler(self):
        self.camera.disable_recording()
        self.camera.close()
        sys.exit(0)
    signal(SIGINT, handler)

    main()
