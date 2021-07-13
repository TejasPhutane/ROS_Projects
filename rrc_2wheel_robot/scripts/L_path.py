#!/usr/bin/env python

import rospy
from geometry_msgs.msg  import Twist
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Range
from tf.transformations import euler_from_quaternion
import math

'''
    Class to move in L pattern with obstacle avoidance
    topics: /rrc_2wheel_robot/cmd_vel -> velocity input (v_x,v_y,w_theta) to differential drive robot
            /rrc_2wheel_robot/odom    -> odometry from robot (x,y,quaterion)
            /sonar_l_sensor           -> left sensor range
            /sonar_f_sensor           -> front sensor range
            /sonar_r_sensor           -> right sensor range
'''
class CleaningRobot():

    def __init__(self):
        #Initializing ROS node
        rospy.init_node('cleanbot_auto_mode', anonymous=True)

        #Publish/Subscribe ROS topics
        self.velocity_publisher = rospy.Publisher('/rrc_2wheel_robot/cmd_vel', Twist, queue_size=10)
        self.pose_subscriber = rospy.Subscriber('/rrc_2wheel_robot/odom', Odometry,self.PoseCallback)       
        self.left_sensor = rospy.Subscriber("/sonar_l_sensor",Range,self.left_sensor_callback)
        self.front_sensor = rospy.Subscriber("/sonar_f_sensor",Range,self.front_sensor_callback)
        self.right_sensor = rospy.Subscriber("/sonar_r_sensor",Range,self.right_sensor_callback)

        self.rate = rospy.Rate(10)
        self.distance_threshold = 0.3 # in meter
        
        self.l_dist = 0
        self.f_dist = 0
        self.r_dist = 0
        self.previous = "R"
        #wait for Initialization
        rospy.sleep(4)

    ### Getting robot position and distance sensor values

    '''
        Function Callback to get robot position			
    '''
    def PoseCallback(self,pose_message):
    
        self.odom_x = pose_message.pose.pose.position.x
        self.odom_y = pose_message.pose.pose.position.y
        rot_q = pose_message.pose.pose.orientation
        (roll, pitch, self.odom_theta) = euler_from_quaternion ([rot_q.x, rot_q.y, rot_q.z, rot_q.w])
        #self.position = [self.odom_x,self.odom_y,self.odom_theta]

    '''
        Function Callback to get left sensor distance and converting it into binary using distance_threshold
    '''
    def left_sensor_callback(self,msg):
        
        if msg.range < self.distance_threshold:
            self.l_dist = 1
        else:
            self.l_dist = 0
            
    '''
        Function Callback to get front sensor distance and converting it into binary using distance_threshold
    '''
    def front_sensor_callback(self,msg):
        #print("distance received: "+ str(msg.range))
        if msg.range < self.distance_threshold:
            self.f_dist = 1
        else:
            self.f_dist = 0

        #print(self.f_dist)

    '''
        Function Callback to get right sensor distance and converting it into binary using distance_threshold
    '''
    def right_sensor_callback(self,msg):

        if msg.range < self.distance_threshold:
            self.r_dist = 1
        else:
            self.r_dist = 0

    '''
        Function to rotate the robot
        
        Input - 
            1. param_degree - angle to rotate (radians)
            2. param_speed - rotation speed (deg/sec)
            3. param_dir - 'a' ->anticlockwise
                           'c' ->clockwise
	'''
    def func_rotate(self, param_degree, param_speed, param_dir):

        obj_velocity_mssg = Twist()

        # Store start Theta of the Robot
        start_degree = self.odom_theta
        current_degree = self.odom_theta

        
        var_loop_rate = rospy.Rate(10)
        # Set the speed of rotation according to param_dir
        if(param_dir == 'a'):
            # Anticlockwise
            obj_velocity_mssg.angular.z = math.radians(
                abs(int(param_speed)))  
        else:
            # Clockwise
            obj_velocity_mssg.angular.z = (-1) * \
                math.radians(abs(int(param_speed)))

        # Rotate till desired angle is reached
        degree_rotated = 0.0

        while not rospy.is_shutdown():
            if((round(degree_rotated) < param_degree)):
                self.velocity_publisher.publish(obj_velocity_mssg)

                var_loop_rate.sleep()

                current_degree = self.odom_theta
                degree_rotated = abs(current_degree - start_degree)
                print('Degree Rotated: {}'.format(degree_rotated))
            else:
                break

        # Stop the Robot after the desired angle is reached
        obj_velocity_mssg.angular.z = 0
        self.velocity_publisher.publish(obj_velocity_mssg)
        print('Angle Reached')

    '''
        Function to move the Robot straight for specific distance
        
        Input - 
            1. param_dis - distance to travel (m)
            2. param_speed - speed (m/s)
            3. param_dir - 'f' ->forward
                           'b' ->backward
	'''
    def func_move_straight(self, param_dis, param_speed, param_dir):

        obj_velocity_mssg = Twist()

        # Store the start position of the Robot
        start_x = self.odom_x
        start_y = self.odom_y  

        
        var_loop_rate = rospy.Rate(10)

        # Set the Speed of the Robot according to the direction
        if param_dir == 'f':
            obj_velocity_mssg.linear.x = abs(param_speed)
        else:
            obj_velocity_mssg.linear.x = (-1) * abs(param_speed)

        # Move till desired distance is covered
        dis_moved = 0.0

        while not rospy.is_shutdown():

            if (dis_moved < param_dis):
                self.velocity_publisher.publish(obj_velocity_mssg)

                var_loop_rate.sleep()
                #dis_moved = abs(self.odom_x - start_x)
                dis_moved = abs(
                    math.sqrt(((self.odom_x - start_x) ** 2) + ((self.odom_y - start_y) ** 2)))
                print('Distance Moved: {}'.format(dis_moved))
            else:
                break

        # Stop the Robot after desired distance is covered
        obj_velocity_mssg.linear.x = 0
        self.velocity_publisher.publish(obj_velocity_mssg)
        print('Destination Reached')

    '''
        Function for L pattern Obstacle Avoidance 

    '''
    def L_path_cleaning(self):
        #case 1 : 000 => move forward
        #case 2 : 010 => left or right alternating and move unit distance and repeat last action
        velocity_message = Twist()
        if self.f_dist==0 :
            velocity_message.linear.x =0.3
            self.velocity_publisher.publish(velocity_message)
            self.rate.sleep()
        else:
            if self.previous=="R":
                self.func_rotate(1.5708, 60, "a")
                self.func_move_straight(0.2,0.3,'f')
                self.func_rotate(1.5708, 60, "a")
                self.previous ="L"
            elif self.previous=="L":
                self.func_rotate(1.5708, 60, "c")
                self.func_move_straight(0.2,0.3,'f')
                self.func_rotate(1.5708, 60, "c")
                self.previous ="R"

if __name__ == '__main__':
    robot = CleaningRobot()
    while not rospy.is_shutdown():
        robot.L_path_cleaning()

        #print sensor distance 
        distance = [robot.l_dist,robot.f_dist,robot.r_dist]
        print distance

