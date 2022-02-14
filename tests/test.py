import configparser, traceback, sys

class Mavlink():
    def __init__(self, config) -> None:

        self.cam_power_channel = config['RC_CHANNEL']['cam_power_channel']
        self.cam_record_channel = config['RC_CHANNEL']['cam_record_channel']


config = configparser.ConfigParser()
config.read('config/config.ini')

def main():

    try:
        mavlink = Mavlink(config)
        print(mavlink.cam_power_channel)

    except Exception:
        print(traceback.format_exc())
        sys.exit(0)

if __name__ == "__main__":

    main()
