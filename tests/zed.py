import sys
import pyzed.sl as sl


class ZEDCAM:
    def __init__(self):
        init_params = sl.InitParameters()
        init_params.camera_resoolation = sl.RESOLUTION.HD720
        init_params.depth_mode = sl.DEPTH_MODE.NONE

        zed = sl.Camera()
        err = zed.open(init_params)

        if err != sl.ERROR_CODE_SUCCESS:
            exit()


if __name__ == "__main__":
    try:
        pass
    
    except Exception as error:
        print(error)
        sys.exit(0)
    