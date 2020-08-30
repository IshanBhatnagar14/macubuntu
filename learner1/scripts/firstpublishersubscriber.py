#!/usr/bin/env python
import rospy
from random import random
from learner1.msg import comple

rospy.init_node('talk', anonymous = True)
val = comple()
final = comple()

def fact(data):
    val.real = random ()
    val.imaginery= random()
    final.real = data.real * val.real
    final.imaginery = data.imaginery * val.imaginery
    tub.publish(final)
    print(final)


    rospy.Subscriber('Chatterbot', comple ,fact)
    tub = rospy.Publisher('calval', comple, queue_size=10)

    rospy.spin()






