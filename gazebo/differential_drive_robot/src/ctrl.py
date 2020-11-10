#!/usr/bin/env python
# license removed for brevity
import rospy
from gazebo_msgs.msg import ModelStates

def talker():
    pub = rospy.Publisher('/gazebo/model_states', ModelStates, queue_size=10)
    rospy.init_node('dd_ctrl', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        buff = ModelStates()
        buff.name ="dd_robot::chassis"
        buff.twist = 10
        rospy.loginfo(buff)
        pub.publish(buff)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass