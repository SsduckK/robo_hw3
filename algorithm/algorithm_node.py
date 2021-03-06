#!/usr/bin/env python

import rospy
import math
from common_msg.msg import TimePose
from common_msg.srv import OverDistance, OverDistanceResponse

def callback(msg):
  a = msg.Point.x
  b = msg.Point.y
  c = msg.Point.z
  r = math.sqrt(a**2+b**2+c**2)
  reverse_Hdegree = math.cos(math.sqrt(a**2+b**2)/r)
  Hdegree = 90-math.acos(reverse_Hdegree)*180/math.pi
  reverse_Wdegree = math.cos(a/math.sqrt(a**2+b**2))
  Wdegree = 90-math.acos(reverse_Wdegree)*180/math.pi
  print "----subscribe----\n x = %.2f, y = %.2f, z = %.2f\n r = %.2f\n Hdegree = %.2f, Wdegree = %.2f" % (a, b, c, r, Hdegree, Wdegree)

def service_callback(request):
  response = OverDistanceResponse(d = math.sqrt(request.a**2+request.b**2+request.c**2))
  print "---Distance:---", response.d
  return response

rospy.init_node('algorithm_subscriber')
sub = rospy.Subscriber('custom_msg', TimePose, callback)
service = rospy.Service('overdistance', OverDistance, service_callback)
rospy.spin()
