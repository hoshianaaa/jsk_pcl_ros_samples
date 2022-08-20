#!/usr/bin/python

import tkinter as tk
import rospy
from jsk_recognition_msgs.msg import BoundingBox
import tf
from geometry_msgs.msg import Quaternion
from geometry_msgs.msg import Vector3
import math


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

class Application(tk.Frame):

    def __init__(self, master = None):
        super().__init__(master)

        self.x = self.create_scale("x: ", -1, 1, 0.01)
        self.y = self.create_scale("y: ", -1, 1, 0.01)
        self.z = self.create_scale("z: ", -1, 1, 0.01)

        self.dx = self.create_scale("dim x: ", 0.01, 1, 0.01)
        self.dx.set(0.2)
        self.dy = self.create_scale("dim y: ", 0.01, 1, 0.01)
        self.dy.set(0.2)
        self.dz = self.create_scale("dim z: ", 0.01, 1, 0.01)
        self.dz.set(0.2)

        self.ex = self.create_scale("euler x: ", - math.pi, math.pi, 0.01)
        self.ey = self.create_scale("euler y: ", - math.pi, math.pi, 0.01)
        self.ez = self.create_scale("euler z: ", - math.pi, math.pi, 0.01)
        

        self.pub = rospy.Publisher("/attention_clipper/input/box", BoundingBox, queue_size=10)

        wait_init_pos = True
        self.init_pos_read = False
        self.init_pos_msg = None
        if wait_init_pos:
          rospy.Subscriber("/bbox_init_pos", BoundingBox, self.init_pos_callback)
          while alive():
            if self.init_pos_read:
              break

        self.set_pos(self.init_pos_msg)
        self.after(1, self.loop)

    def set_pos(self,msg):
 
        self.x.set(msg.pose.position.x)
        self.y.set(msg.pose.position.y)
        self.z.set(msg.pose.position.z)

        quat = msg.pose.orientation
        euler = quaternion_to_euler(quat)

        self.ex.set(euler.x)
        self.ey.set(euler.y)
        self.ez.set(euler.z)

        
        dx = msg.dimensions.x
        dy = msg.dimensions.y
        dz = msg.dimensions.z

        if (dx != 0) and (dy != 0) and (dz != 0):
          self.dx.set(dx)
          self.dy.set(dy)
          self.dz.set(dz)

    def init_pos_callback(self,msg):
        
        self.init_pos_msg = msg
        self.init_pos_read = True

    def create_scale(self,name="", from_val=-1, to_val=1, resolution = 0.1,length=300,width=20, relese_func=None):

        label = tk.Label(self.master, text=name)
        label.pack()

        scale_var = tk.DoubleVar()

        scaleH = tk.Scale( self.master, 
                    orient=tk.HORIZONTAL,
                    variable = scale_var,
                    length = length,
                    width = width,             
                    sliderlength = 20,      
                    from_ = from_val,       
                    to = to_val,          
                    resolution = resolution,         
                    tickinterval = 50         
                    )

        scaleH.pack()


        return scale_var


    def loop(self):

        x = self.x.get()
        y = self.y.get()
        z = self.z.get()

        dx = self.dx.get()
        dy = self.dy.get()
        dz = self.dz.get()

        ex = self.ex.get()
        ey = self.ey.get()
        ez = self.ez.get()

        #print(x,y,z)
        quat = euler_to_quaternion(Vector3(ex, ey, ez))

        msg = BoundingBox()
        msg.header.frame_id = "base_link"
        msg.pose.position.x = x
        msg.pose.position.y = y
        msg.pose.position.z = z
        msg.pose.orientation.x = quat.x
        msg.pose.orientation.y = quat.y
        msg.pose.orientation.z = quat.z
        msg.pose.orientation.w = quat.w
        msg.dimensions.x = dx
        msg.dimensions.y = dy
        msg.dimensions.z = dz
        self.pub.publish(msg)

        self.after(1, self.loop)

        if rospy.is_shutdown():
          app.master.destroy()


root = tk.Tk()
rospy.init_node("bounding_box_controller")
app = Application(master = root)
app.mainloop()
