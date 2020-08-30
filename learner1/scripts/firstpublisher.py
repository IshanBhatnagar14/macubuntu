#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

def talker ():
    rospy.init_node('firsttalker')     # no spaces allowed in node name
    pub = rospy.Publisher('Chatter',Int32,queue_size=10)
    rate = rospy.Rate(1)
    count=0
    while not rospy.is_shutdown():

        pub.publish(count)
        count = count + 1
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except:
        pass
