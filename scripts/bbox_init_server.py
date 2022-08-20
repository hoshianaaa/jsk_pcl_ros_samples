#!/usr/bin/python

import sys
import rospy
from jsk_recognition_msgs.msg import BoundingBox

import tf
from geometry_msgs.msg import Quaternion
from geometry_msgs.msg import Vector3
import math

import json
import os

def read_json_file(file_name):
  if os.path.exists(file_name):
    with open(file_name, 'r') as f:
      json_load = json.load(f)
      return json_load, True
  return None, False

def write_json_file(file_name, dict_data):
  with open(file_name, 'w') as f:
    json.dump(dict_data, f, indent=2)

def alive():
    return not rospy.is_shutdown()

def euler_to_quaternion(euler):
    """Convert Euler Angles to Quaternion

    euler: geometry_msgs/Vector3
    quaternion: geometry_msgs/Quaternion
    """
    q = tf.transformations.quaternion_from_euler(euler.x, euler.y, euler.z)
    return Quaternion(x=q[0], y=q[1], z=q[2], w=q[3])


def quaternion_to_euler(quaternion):
    """Convert Quaternion to Euler Angles

    quarternion: geometry_msgs/Quaternion
    euler: geometry_msgs/Vector3
    """
    e = tf.transformations.euler_from_quaternion((quaternion.x, quaternion.y, quaternion.z, quaternion.w))
    return Vector3(x=e[0], y=e[1], z=e[2])

def callback(msg):

  x = msg.pose.position.x 
  y = msg.pose.position.y 
  z = msg.pose.position.z
  qx = msg.pose.orientation.x
  qy = msg.pose.orientation.y
  qz = msg.pose.orientation.z
  qw = msg.pose.orientation.w
  dx = msg.dimensions.x
  dy = msg.dimensions.y
  dz = msg.dimensions.z

  data["x"] = x
  data["y"] = y
  data["z"] = z
  data["qx"] = qx
  data["qy"] = qy
  data["qz"] = qz
  data["qw"] = qw
  data["dx"] = dx
  data["dy"] = dy
  data["dz"] = dz
  
  write_json_file(f_name, data)

f_name = os.environ['HOME'] + "/.ros/init_pos.json"

if len(sys.argv) > 1:
  f_name = sys.argv[1]

data, read_sucess = read_json_file(f_name)

if read_sucess == False:
  print("cannot find file")
  data = {'x': 0, 'y': 0, 'z': 0, 'qx': 0, 'qy': 0, 'qz': 0, 'qw': 1, 'dx': 0.2, 'dy': 0.2, 'dz': 0.2}
  write_json_file(f_name, data)

else:
  print(data)

first_pub = False

rospy.init_node("bbox_init_server")
pub = rospy.Publisher("/bbox_init_pos", BoundingBox, queue_size=10)
cripper_pub = rospy.Publisher("/attention_clipper/input/box", BoundingBox, queue_size=10)
rospy.Subscriber("/attention_clipper/input/box", BoundingBox, callback)


r = rospy.Rate(10)

x = data["x"]
y = data["y"]
z = data["z"]
qx = data["qx"]
qy = data["qy"]
qz = data["qz"]
qw = data["qw"]
dx = data["dx"]
dy = data["dy"]
dz = data["dz"]


while alive():
 
  print(data)

  x = data["x"]
  y = data["y"]
  z = data["z"]
  qx = data["qx"]
  qy = data["qy"]
  qz = data["qz"]
  qw = data["qw"]
  dx = data["dx"]
  dy = data["dy"]
  dz = data["dz"]

  msg = BoundingBox()
  msg.header.seq = 1
  msg.header.frame_id = "base_link"
  msg.pose.position.x = x
  msg.pose.position.y = y
  msg.pose.position.z = z
  msg.pose.orientation.x = qx
  msg.pose.orientation.y = qy
  msg.pose.orientation.z = qz
  msg.pose.orientation.w = qw
  msg.dimensions.x = dx
  msg.dimensions.y = dy
  msg.dimensions.z = dz

  pub.publish(msg)
  cripper_pub.publish(msg)

  r.sleep()
