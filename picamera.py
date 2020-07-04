#!/usr/bin/env python
# -*- coding: utf-8 -*-

#모듈 로딩
import picamera as camera
import time


def main(args):
    cam = camera.PiCamera()
    cam.start_preview()
    time.sleep(3)
    cam.capture("/home/pi/Pictures/cam01.jpg")
    cam.stop_preview()
    cam.close()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
