#!/usr/bin/env python
import rospy
from random import *
from geometry_msgs.msg import Point
from common_msg.msg import TimePose

rospy.init_node('sensor_publisher.py')
pub = rospy.Publisher('custom_msg', TimePose, queue_size=1)
msg = TimePose()
rate = rospy.Rate(1)
while not rospy.is_shutdown():
  msg.timestamp = rospy.get_rostime()
  msg.Point = Point(x=randint(1, 10), y=randint(1, 10), z=randint(1, 10))
  pub.publish(msg)
  print ("print : x =", msg.Point.x, "y =", msg.Point.y, "z =", msg.Point.z)
  rate.sleep()
