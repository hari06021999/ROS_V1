#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int16
import time
import sys
    
    
          
class node():       
	def __init__(self):

	    # In ROS, nodes are uniquely named. If two nodes with the same
	    # name are launched, the previous one is kicked off. The
	    # anonymous=True flag means that rospy will choose a unique
	    # name for our 'listener' node so that multiple listeners can
	    # run simultaneously.
	    print("subscribe node")
	    
	    self.data_sub=rospy.Subscriber("test", Int16, self.callback)
	    
	    #rospy.init_node('listener', anonymous=True)
	    # spin() simply keeps python from exiting until this node is stopped
	    
	
	
	def callback(self,data):
	    print("---------------")
	    rospy.loginfo(data.data) 
	    #self.pub_1.publish(data)	    

def main(args):
    rospy.init_node('subscriber_to_publisher', anonymous=True)
    try:
        O=node()
        rospy.spin()
    except rospy.ROSInterruptException:
	    pass    
if __name__ == '__main__':
     main(sys.argv)   
    
