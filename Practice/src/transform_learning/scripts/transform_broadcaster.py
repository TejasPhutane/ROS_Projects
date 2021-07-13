#!usr/bin/env python
import roslib
import rospy
roslib.load_manifest('first_bringup')
import tf
import turtlesim.msg

def handle_turtle_pose(msg,turtlename):
    br  = tf.TransformBroadcaster(queue_size=100)
    br.sendTransform((msg.x,msg.y,0),
                      tf.transformations.quaternion_from_euler(0,0,msg.theta),
                      rospy.Time.now(),
                      turtlename,
                      "world")

def broadcaster():
    rospy.init_node("tf_broadcaster",anonymous=True)
    turtlename = rospy.get_param('~turtle')
    rospy.Subscriber('/{}/pose'.format(turtlename),
                     turtlesim.msg.Pose,
                     handle_turtle_pose,
                     turtlename)
    rospy.spin()
if __name__ == "__main__":
    broadcaster()
  