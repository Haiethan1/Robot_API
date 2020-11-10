#!/usr/bin/env python
# license removed for brevity
import rospy
from gazebo_msgs.msg import LinkState

def talker():
    pub = rospy.Publisher('/gazebo/set_link_state', LinkState, queue_size=10)
    rospy.init_node('dd_ctrl', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        buff = LinkState()
        buff.link_name = "dd_robot::left_wheel"
        buff.reference_frame ="dd_robot::chassis"
        buff.twist.linear.z = 10.0
        buff.reference_frame = "dd_robot::left_wheel"
        buff.link_name ="dd_robot::chassis"
        rospy.loginfo(buff)
        pub.publish(buff)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass