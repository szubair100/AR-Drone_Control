# AR-Drone_Control

## Programs Installation:
  - ROS

## Required ROS Packet Installation:
  - [apriltags2_ros](http://wiki.ros.org/apriltags2_ros)
    - [GitHub Repo](https://github.com/dmalyuta/apriltags2_ros) 
  - [ardrone_autonomy](http://wiki.ros.org/ardrone_autonomy)
    - [GitHub Repo](https://github.com/AutonomyLab/ardrone_autonomy.git)

## Direction:
  1. Install all required packet

## To Run:
- Terminal 1: `roslaunch drone_application launch_drone.launch`
- Terminal 2: `roslaunch apriltags2_ros continuous_detection.launch`
- Terminal 3: `rqt` (make sure to have image  view open : Plugins/Visualization/Image view)
- Terminal 4: `rostopic list (to get rostopic publish option)`
  - `rostopic pub -1 …` to imput commands
       
# Procedure
### AR Drone Control
  1. Installed `ardrone_autonomy`
  2. Created New Packet `drone_application`
    ```catkin_create_pkg drone_application std_msgs rospy roscpp```
  3. Created Launch file `launch_drone.launch` in `drone_application` with the following code:
  ```
    <launch>
      <arg name="droneip" default="192.168.1.1" />
      <node name="ardrone_driver" pkg="ardrone_autonomy" type="ardrone_driver" output="screen" args="-ip $(arg droneip)">
              <param name="navdata_demo" value="False" />
              <param name="realtime_navdata" value="True" />
              <param name="realtime_video" value="True" />
              <param name="looprate" value="30" />
      </node>
    </launch>
  ```
  4. Connect to Drone through WiFi
  5. Lauch Drone, in terminal:
  ```roslaunch drone_application launch_drone.launch```
     Message appeared as follow:
      ```
      [ INFO] [1456020168.671768680]: Successfully connected to 'My ARDrone' (AR-Drone 2.0 - Firmware: 2.4.8) - Battery(%): 85
      ```
Based on [GaiTech EDU](https://edu.gaitech.hk/drones/ar_parrot_2/ar-parrot-2-ros.html)

### AprilTag2
  1. Installed Package into `~/catkin_ws/src` with `git clone https://github.com/dmalyuta/apriltags2_ros.git`
  2. Calibrations For AR Drone:
    - in apriltags2_ros `catkin_ws/src/apriltags2_ros/apriltags2_ros/launch/continuous_detection.launch`
      - change line 14 to `<remap from="image_rect" to="/ardrone/image_raw" />`
      - change line 15 to `<remap from="camera_info" to="/ardrone/camera_info" />`
      
      
**Copyright**

The source code in apriltags2/ is wholly the work of the APRIL Robotics Lab at The University of Michigan. This package simply rearranges the source code to be able to compile it with catkin.

The source code in apriltags2_ros/ is original code that is the ROS wrapper itself, see the LICENSE. It is inspired by apriltags_ros and provides a superset of its functionalities.

If you use this code, please kindly cite:
- D. Malyuta, “Navigation, Control and Mission Logic for Quadrotor Full-cycle Autonomy,” Master thesis, Jet Propulsion Laboratory, 4800 Oak Grove Drive, Pasadena, CA 91109, USA, December 2017.
- J. Wang and E. Olson, "AprilTag 2: Efficient and robust fiducial detection," in ''Proceedings of the IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)'', October 2016.


## System Spec:
  - OS: Ubuntu 16.04 LTS
  - Memory: 7.8 Gb
  - Processor: Intel® Core™ i5-3570 CPU @ 3.40GHz × 4
  - Graphic: AMD CAICOS (DRM 2.50.0 / 4.13.0-43-generic, LLVM 5.0.0)
  - OS Type: 64-bit

## Air Drone Spec:
  - Drone: [Parrot AR Drone 2.0](https://www.parrot.com/global/drones/parrot-ardrone-20-elite-edition#parrot-ardrone-20-elite-edition)
  - HD video recording:
    - 720p 30fps HD camera
    - Wide-angle lens: 92° diagonal
    - Basic encoding profile: H264
    - Photo format: JPEG
    - Connection: Wi-Fi
  - Electronic assistance
    - Processor: ARM Cortex A8 1 GHz 32-bit processor with DSP video 800 MHz TMS320DMC64x
    - OS: Linux 2.6.32
    - RAM: DDR2 1 GB at 200 MHz
    - USB: High-speed USB 2.0 for extensions
    - Wi-Fi b g n
    - Gyroscope: 3 axles, accuracy of 2,000°/second
    - Accelerometer: 3 axles, accuracy of +/- 50 mg
    - Magnetometer: 3 axles, accuracy of 6°
    - Pressure sensor: Accuracy of +/- 10 Pa
    - Altitude ultrasound sensor: Measures altitude
    - Vertical camera: QVGA 60 FPS to measure the ground speed
  - Motors & Weight
    - 4 "inrunner" type brush-free motors: 14.5 watts and 28,500 rev/min
    - Micro ball bearing: Yes
    - Nylatron Gears: Yes
    - Bronze self-lubricating ball bearings: Yes
    - Weight:
      > With internal frame 380 g & 
      > With external frame 420 g
