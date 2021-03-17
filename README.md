# jsk_pcl_ros_samples
jsk_pcl_rosパッケージのサンプル集  
  
# Install/インストール
```
sudo apt-get install -y ros-melodic-jsk-pcl-ros
sudo apt-get install -y ros-melodic-jsk-visualization
git clon https://github.com/hoshianaaa/jsk_pcl_ros_samples.git
cd ~/catkin_ws/src

catkin build 
または...
catkin make

source ~/catkin_ws/devel/setup.bash

```
# Try/試す
## attention_clipper(領域の切り抜き)
```
roslaunch jsk_pcl_ros_samples attention_clipper.launch
```

![attention_clipper1](https://user-images.githubusercontent.com/40942409/111522713-e49c5d00-879d-11eb-88de-588b5b1f4d68.png)



