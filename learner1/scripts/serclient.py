#!/usr/bin/env python
import rospy
from learner1.srv import wordcount
import sys

rospy.init_node('ser_client')
rospy.wait_for_service('word_count')
word_count=rospy.ServiceProxy('word_count',wordcount)
words = ' '.join(sys.argv[1:])
count = word_count(words)
print (words, '->', count)