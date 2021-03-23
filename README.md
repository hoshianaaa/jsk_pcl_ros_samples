# jsk_pcl_ros_samples
jsk_pcl_rosパッケージのサンプル集  
  
# インストール
```
sudo apt-get install -y ros-melodic-jsk-pcl-ros
sudo apt-get install -y ros-melodic-jsk-visualization
git clon https://github.com/hoshianaaa/jsk_pcl_ros_samples.git
cd ~/catkin_ws/src

catkin build 
または
catkin make

source ~/catkin_ws/devel/setup.bash

```
# 試す
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

サンプル2(複数のBoundingBox)の起動
```
roslaunch jsk_pcl_ros_samples attention_clipper_multi.launch 
```

![Screenshot from 2021-03-18 04-53-53](https://user-images.githubusercontent.com/40942409/111529920-0e598200-87a6-11eb-9cb8-f6e991a1a1e1.png)


## detect_graspable_poses_pcabase(把持推定)

```
roslaunch jsk_pcl_ros_samples detect_graspable_poses_pcabase.launch
```

![Screenshot from 2021-03-21 14-44-07](https://user-images.githubusercontent.com/40942409/111895762-0b85b800-8a58-11eb-9fb8-8461c23ee58d.png)

## Octree_voxel_grid(点群のボクセル化)
```
roslaunch jsk_pcl_ros_samples octree_voxel_grid.launch
```

rqt_reconfigureからresolution(ボクセル間の間隔)の変更ができます。

```
rosrun rqt_reconfigure rqt_reconfigure
```
![Screenshot from 2021-03-24 04-41-32](https://user-images.githubusercontent.com/40942409/112209309-a8b13e00-8c5c-11eb-951e-209bef975879.png)

![Screenshot from 2021-03-24 04-41-41](https://user-images.githubusercontent.com/40942409/112209333-ad75f200-8c5c-11eb-9486-4963d9e34fd3.png)

![Screenshot from 2021-03-24 04-41-51](https://user-images.githubusercontent.com/40942409/112209345-b1097900-8c5c-11eb-9210-82a949f15f28.png)



