#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
def callfast(msg):
    print(msg.msg)
def listener():
    rospy.init_node('firstlistener')
    rospy.Subscriber('Chatter',Int32,callfast)
    rospy.spin()

if __name__ =='__main__':
    listener()
