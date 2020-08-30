#!/usr/bin/env python
import rospy
from learner1.msg import comple
from random import random

def talker():
    rospy.init_node('secondpub')
    tub = rospy.Publisher('Chatterbot', comple,queue_size=10)
    rate=rospy.Rate(1)

    while not rospy.is_shutdown():
        msg=comple()
        msg.real = random()
        msg.imaginery=random()
        tub.publish(msg)
        rate.sleep()


if __name__=='__main__':
    talker()