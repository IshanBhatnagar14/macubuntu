#!/usr/bin/env python
import rospy
from learner1.srv import wordcount,wordcountResponse

def counter(request):
    return wordcountResponse(len(request.word.split()))      # Coonstructor takes matching arguments


rospy.init_node('service_server')
rospy.Service('word_count',wordcount,counter)
rospy.spin()
