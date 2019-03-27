#!/usr/bin/env python

import rospy
from sensehat_driver.msg import IMUOrientation
from sense_hat import SenseHat

def display_callback(data):
    rospy.loginfo("yaw: %f" % data.yaw)
    
    if (45 <= data.raw < 135):
        sense.show_letter("E")
    elif (135 <= data.yaw < 225):
        sense.show_letter("S")
    elif (225 <= data.yaw < 315):
        sense.show_letter("W")
    else:
        sense.show_letter("N")

def sub_orientation():
    rospy.init_node("display_orientation", anonymous=True)
    rospy.Subscriber("imu_orientation", IMUOrientation, display_callback)
    rospy.spin()

if __name__ == '__main__':
    sense = SenseHat()
    sense.clear()
    sub_orientation()
    

