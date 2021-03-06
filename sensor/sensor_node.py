#!/usr/bin/env python
import rospy
from random import *
from geometry_msgs.msg import Point
from common_msg.msg import TimePose
from common_msg.srv import OverDistance, OverDistanceRequest

rospy.init_node('sensor_publisher.py')
rospy.wait_for_service('overdistance')
requester = rospy.ServiceProxy('overdistance', OverDistance)
pub = rospy.Publisher('custom_msg', TimePose, queue_size=1)
msg = TimePose()
rate = rospy.Rate(1)
while not rospy.is_shutdown():
  msg.timestamp = rospy.get_rostime()
  msg.Point = Point(x=randint(1, 10), y=randint(1, 10), z=randint(1, 10))
  pub.publish(msg)
  print "print : x =", msg.Point.x, "y =", msg.Point.y, "z =", msg.Point.z
  if msg.Point.x > 5 and msg.Point.y > 5 and msg.Point.z > 5:
    req = OverDistanceRequest(a = msg.Point.x, b = msg.Point.y, c = msg.Point.z)
    res = requester(req)
    print "Too FAR", res.d
  rate.sleep()
