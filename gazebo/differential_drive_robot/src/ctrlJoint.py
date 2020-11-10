#!/usr/bin/env python3
# license removed for brevity
import rospy
from gazebo_msgs.srv import ApplyJointEffort
from std_msgs.msg import Header

def talker():
#    pub = rospy.Publisher('/gazebo/apply_joint_effort', ApplyJointEffort, queue_size=10)
    rospy.init_node('dd_ctrl', anonymous=True)
    pub = rospy.ServiceProxy('/gazebo/apply_joint_effort',ApplyJointEffort)
    rate = rospy.Rate(10) # 10hz
    i = 0
    buff = ApplyJointEffort()
    buff.joint_name = "dd_robot::left_wheel_hinge"
    buff.effort = 1.0
    buff.start_time = 0.0
    buff.duration = 0.0
    start_time = rospy.Time(0,0)
    end_time = rospy.Time(0.01,0)
    while not rospy.is_shutdown():
        if i > 30:
            buff.effort = -buff.effort
            i = 0
        i = i + 1


        # ['joint_name', 'effort', 'start_time', 'duration']
        #pub( buff.joint_name, buff.effort, buff.start_time, buff.duration )
        #pub( buff.joint_name, buff.effort, 0.0, 0.1 )
        buff.joint_name = "dd_robot::left_wheel_hinge"
        pub(buff.joint_name, buff.effort, start_time, end_time)
        buff.joint_name = "dd_robot::right_wheel_hinge"
        pub(buff.joint_name, buff.effort, start_time, end_time)
        rospy.loginfo(buff)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
