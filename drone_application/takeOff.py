#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import Empty

def takeOff():
    bol = True
    while (bol):
        var = input("0 to Land, 1 to Take Off \n2 to Exit:\t")
        if var == 1:
            pub = rospy.Publisher("ardrone/takeoff", Empty, queue_size=10)
            rospy.init_node('takeoff', anonymous=True)
        elif var == 0:
            pub = rospy.Publisher("ardrone/land", Empty, queue_size=10)
            rospy.init_node('land', anonymous=True)
            bol = False
        rate = rospy.Rate(10) # 10hz
        while not rospy.is_shutdown():
            pub.publish(Empty())
            rate.sleep()

if __name__ == '__main__':
    try:
        takeOff()
    except rospy.ROSInterruptException:
        pass
