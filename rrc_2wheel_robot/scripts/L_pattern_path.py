#!/usr/bin/env python

import rospy
from geometry_msgs.msg  import Twist
from nav_msgs.msg import Odometry
from math import pow,atan2,sqrt
from sensor_msgs.msg import Range
from tf.transformations import euler_from_quaternion
import math
PI = 3.14
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

        self.rate = rospy.Rate(5)
        self.distance_threshold = 0.3 # in meter
        
        self.l_dist = 0
        self.f_dist = 0
        self.r_dist = 0
        self.previous = "R"
        
    ### Getting robot position and distance sensor values
    def PoseCallback(self,pose_message):
    
        odom_x = pose_message.pose.pose.position.x
        odom_y = pose_message.pose.pose.position.y
        rot_q = pose_message.pose.pose.orientation
        (roll, pitch, self.odom_theta) = euler_from_quaternion ([rot_q.x, rot_q.y, rot_q.z, rot_q.w])
        self.position = [odom_x,odom_y,self.odom_theta]
        #print self.position
    def left_sensor_callback(self,msg):
        
        if msg.range < self.distance_threshold:
            self.l_dist = 1
        else:
            self.l_dist = 0

    def front_sensor_callback(self,msg):
        #print("distance received: "+ str(msg.range))
        if msg.range < self.distance_threshold:
            self.f_dist = 1
        else:
            self.f_dist = 0

        #print(self.f_dist)

    def right_sensor_callback(self,msg):

        if msg.range < self.distance_threshold:
            self.r_dist = 1
        else:
            self.r_dist = 0

    # def rotate(self,speed,angle,clockwise):

    #     #Converting from angles to radians
    #     angular_speed = speed*2*PI/360
    #     relative_angle = angle*2*PI/360
    #     vel_msg = Twist()
    #     #We wont use linear components
    #     vel_msg.linear.x=0
    #     vel_msg.linear.y=0
    #     vel_msg.linear.z=0
    #     vel_msg.angular.x = 0
    #     vel_msg.angular.y = 0

    #     # Checking if our movement is CW or CCW
    #     if clockwise:
    #         vel_msg.angular.z = -abs(angular_speed)
    #     else:
    #         vel_msg.angular.z = abs(angular_speed)
    #     # Setting the current time for distance calculus
    #     t0 = rospy.Time.now().to_sec()
    #     current_angle = 0

    #     while(current_angle < relative_angle):
    #         self.velocity_publisher.publish(vel_msg)
    #         t1 = rospy.Time.now().to_sec()
    #         current_angle = angular_speed*(t1-t0)

        
    #     self.velocity_publisher.publish(vel_msg)

    # Function to rotate the turtle in turtlesim_node
    def func_rotate(self, param_degree, param_speed, param_dir):

        obj_velocity_mssg = Twist()

        # Store start Theta of the turtle
        start_degree = self.odom_theta
        current_degree = self.odom_theta

        
        var_loop_rate = rospy.Rate(10)
        # Set the speed of rotation according to param_dir
        if(param_dir == 'a'):
            obj_velocity_mssg.angular.z = math.radians(
                abs(int(param_speed)))  # Anticlockwise
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

        # Stop the Turtle after the desired angle is reached
        obj_velocity_mssg.angular.z = 0
        self.velocity_publisher.publish(obj_velocity_mssg)
        print('Angle Reached')


    def move(self,speed, distance, is_forward):
        #declare a Twist message to send velocity commands
        velocity_message = Twist()
        #get current location 


        if (speed > 0.4):
            print 'speed must be lower than 0.4'
            return

        if (is_forward):
            velocity_message.linear.x =abs(speed)
        else:
        	velocity_message.linear.x =-abs(speed)

        distance_moved = 0.0
        loop_rate = rospy.Rate(10) # we publish the velocity at 10 Hz (10 times a second)    
    

        t0 = rospy.Time.now().to_sec()

        while True :
                rospy.loginfo("Turtlesim moves forwards")
                self.velocity_publisher.publish(velocity_message)

                loop_rate.sleep()
                t1 =  rospy.Time.now().to_sec()
                #rospy.Duration(1.0)
                
                distance_moved = (t1-t0) * speed
                print  distance_moved               
                if  not (distance_moved<distance):
                    rospy.loginfo("reached")
                    break
        
        #finally, stop the robot when the distance is moved
        velocity_message.linear.x =0
        self.velocity_publisher.publish(velocity_message)




    def L_path_cleaning(self):
        #print(self.l_dist, self.f_dist, self.r_dist)
        #case 1 : 000 => move forward
        #case 2 : 010 => left or right alternating and move unit distance and repeat last action
        velocity_message = Twist()
        if self.f_dist==0 :
            velocity_message.linear.x =0.3
            self.velocity_publisher.publish(velocity_message)

        else:
            if self.previous=="R":
                self.func_rotate(1.5708, 30, "a")
                self.move(0.2,0.4,True)
                self.func_rotate(1.5708, 30, "a")
                self.previous ="L"
            elif self.previous=="L":
                self.func_rotate(1.5708, 30, "c")
                self.move(0.2,0.4,True)
                self.func_rotate(1.5708, 30, "c")
                self.previous ="R"



if __name__ == '__main__':
    robot = CleaningRobot()
    while not rospy.is_shutdown():
        robot.L_path_cleaning()
        distance = [robot.l_dist,robot.f_dist,robot.r_dist]
        print distance

