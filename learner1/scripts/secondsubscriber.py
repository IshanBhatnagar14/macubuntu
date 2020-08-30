#!/usr/bin/env python
import rospy
from learner1.msg import comple

def wakiki(msg):
    print(msg.real,msg.imaginery)

def listener():
    rospy.init_node('Listener2')
    rospy.Subscriber('Chatterbot',comple,wakiki)
    rospy.spin()

if __name__ =='__main__':
    listener()