# jsk_pcl_ros_samples
jsk_pcl_rosパッケージのサンプル集  
  
# Install/インストール
```
sudo apt-get install -y ros-melodic-jsk-pcl-ros
sudo apt-get install -y ros-melodic-jsk-visualization
git clon https://github.com/hoshianaaa/jsk_pcl_ros_samples.git
cd ~/catkin_ws/src

catkin build 
または/or
catkin make

source ~/catkin_ws/devel/setup.bash

```
# Try/試す
## attention_clipper(領域の切り抜き)

サンプルの起動
```
roslaunch jsk_pcl_ros_samples attention_clipper.launch
```

![attention_clipper1](https://user-images.githubusercontent.com/40942409/111522713-e49c5d00-879d-11eb-88de-588b5b1f4d68.png)

BoundingBoxの移動
```
rostopic pub /attention_clipper/input/pose geometry_msgs/PoseStamped "header:
  seq: 0
  stamp:
    secs: 0
    nsecs: 0
  frame_id: 'base_link'
pose:
  position:
    x: 0.0
    y: 0.1
    z: 0.0
  orientation:
    x: 0.0
    y: 0.0
    z: 0.0
    w: 0.0"
```

![attention_clipper2](https://user-images.githubusercontent.com/40942409/111523346-858b1800-879e-11eb-8375-3107b5459416.png)

BoundingBoxの拡大
```
rostopic pub /attention_clipper/input/box jsk_recognition_msgs/BoundingBox "header:
  seq: 0
  stamp: {secs: 0, nsecs: 0}
  frame_id: 'base_link'
pose:
  position: {x: 0.0, y: 0.1, z: 0.0}
  orientation: {x: 0.0, y: 0.0, z: 0.0, w: 0.0}
dimensions: {x: 0.2, y: 0.2, z: 0.2}
value: 0.0
label: 0"
```

![attention_clipper3](https://user-images.githubusercontent.com/40942409/111523770-021df680-879f-11eb-91f4-72ab7dc0fe33.png)


