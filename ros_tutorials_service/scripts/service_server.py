#!/usr/bin/env python

from ros_tutorials_service.srv import *
import rospy

def handle_add_two_ints(req):

    print ("Returning [%s + %s = %s]"%(req.a, req.b, (req.a + req.b)))

    return SrvTutorialResponse(req.a + req.b)

def add_two_ints_server():

    rospy.init_node('service_server_py')

    s = rospy.Service('ros_tutorial_srv', SrvTutorial, handle_add_two_ints)

    print( "Ready to add two ints.")

    rospy.spin()

if __name__ == "__main__":

    add_two_ints_server()