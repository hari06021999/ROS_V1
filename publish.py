#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import Int16
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
button = 18
GPIO.setup(button,GPIO.IN)
print("Publish node")
def publish_data():
	pub = rospy.Publisher('test', Int16, queue_size=1)
	rospy.init_node('publish_data', anonymous=True)
	rate = rospy.Rate(1000) # 10hz
	while not rospy.is_shutdown():
		
		if GPIO.input(button)==1:
			data=1
			rospy.loginfo(data)
			pub.publish(data)
			print("---------------")
			rospy.sleep(1)
			
if __name__ == '__main__':
	try:
	    publish_data()
	    
	except rospy.ROSInterruptException:
	    pass			
