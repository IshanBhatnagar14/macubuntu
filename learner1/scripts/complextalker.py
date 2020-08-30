import rospy
from learner1.msg import comple
from random import random 

rospy.init_node('message_pub')
pub = rospy.Publisher('compleX', comple)

rate = rospy.Rate(1)

while not rospy.is_shutdown():
      msg = comple()
      msg.real = random()
      msg.imaginery= random()
      pub.publish(msg)
      rate.sleep()
