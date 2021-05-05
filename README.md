# jsk_pcl_ros_samples
jsk_pcl_rosパッケージのサンプル集  
  
# インストール
```
sudo apt-get install -y ros-melodic-jsk-pcl-ros
sudo apt-get install -y ros-melodic-jsk-visualization
git clone https://github.com/hoshianaaa/jsk_pcl_ros_samples.git
cd ~/catkin_ws

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


## HSI_color_filter(RGB点群のHSI色空間フィルター)

```
roslaunch jsk_pcl_ros_samples hsi_color_filter.launch
```

rqt_reconfigureでHSIのしきい値を変更できます。
```
rosrun rqt_reconfigure rqt_reconfigure
```

![Screenshot from 2021-03-30 22-29-35](https://user-images.githubusercontent.com/40942409/112997014-af353d80-91a7-11eb-8b02-83f0ea5db343.png)


## supervoxel segmentation

```
roslaunch jsk_pcl_ros_samples supervoxel_segmentation.launch
```

![Screenshot from 2021-04-18 17-47-29](https://user-images.githubusercontent.com/40942409/115139733-7b468d00-a06e-11eb-87b2-07b864ef6806.png)

- change parameter

```
rosrun rqt_reconfigure rqt_reconfigure
```

## normal_estimation_omp(法線推定)

```
roslaunch jsk_pcl_ros_samples normal_estimation_omp.launch
```

![Screenshot from 2021-05-02 02-37-04](https://user-images.githubusercontent.com/40942409/116790481-541ca080-aaef-11eb-91dc-f6a5c3e9eb92.png)

## multi_plane_sac_segmentation(平面検出)

```
roslaunch jsk_pcl_ros_samples multi_plane_sac_segmentation.launch
```

![Screenshot from 2021-05-05 13-54-35](https://user-images.githubusercontent.com/40942409/117098641-097a7d00-adaa-11eb-9fc0-8d06de02d2ae.png)

## region_growing_segmentation

```
roslaunch jsk_pcl_ros_samples region_growing_segmentation.launch
```

![Screenshot from 2021-05-05 17-32-45](https://user-images.githubusercontent.com/40942409/117115553-38075080-adc8-11eb-9ed8-4002a921bf8f.png)

