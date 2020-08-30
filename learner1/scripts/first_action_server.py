#!/usr/bin/env python
import rospy
import time
import actionlib
from learner1.msg import timerAction, timerGoal, timerResult

def timeso(goal):
    start_time=time.time()
    time.sleep(goal.time_to_wait.to_sec())
    result = timerResult()
    result.time_elapsed = rospy.Duration.from_sec(time.time()-start_time)
    rospy.updates_sent=0
    server.set_succeeded(result)


rospy.init_node('First_Action_Server')
server= actionlib.SimpleActionServer('timer',timerAction,timeso,False)
server.start()
rospy.spin()
