传感器标定
==============================================

**本篇目标：使用 Kalibr 工具，完成 X152b 无人机 IMU 和 D430 相机联合标定，确保数据源准确**

对无人机上的相机和IMU（惯性测量单元）进行 **联合标定** 的目的是为了获取多传感器精确的内、外参，从而能将两者的数据进行精确融合，以此提高无人机在定位、导航、姿态估计以及环境感知等任务中的精度和可靠性。

确保无人机飞控和相机都安装好并通电能正常使用后，按下列步骤进行：

.. code-block:: bash

    # 进入 X152b 项目目录，下载 Kalibr 工具包并编译
    bash scripts/kalibr_setup.sh

.. TODO(Derkai): 这里缺少一张流程图，相机标定--> IMU 标定 --> 联合标定

相机标定
----------------------------------------------

**1、准备标定板**

通过这个网站生成标定板图案,打印出来或投放在屏幕上显示：

.. raw:: html

   <a href="https://calib.io/pages/camera-calibration-pattern-generator" target="_blank">https://calib.io/pages/camera-calibration-pattern-generator</a>

填写以下参数并点击生成：

.. image:: ./assets/calibr_broad.png
  :width: 700
  :alt: calibr_broad

**生成的标定板图案所示：**

.. image:: ./assets/apirltag_example.png
  :width: 700
  :alt: calibr_broad

进入 `src/tasks/kalibr` 目录下，新建一个 yaml 文件，命名为 `april_6x6_24x24mm.yaml` ，内容如下所示。（ **以标定板图案实际测量为准** ）

.. code-block:: bash

    target_type: 'aprilgrid' # 标识码类型
    tagCols: 6               # 标识码列数
    tagRows: 6               # 标识码行数
    tagSize: 0.015           # 标识码边长 [m]
    tagSpacing: 0.3          # 标识码边长与标识码间隔边长的比例
    # 计算方式：标签的物理边长 tagSize 为 1.5cm，而两个相邻标签中心之间的距离 spacing 为 1.95cm 
    # tagSpacing = (1.95 / 1.5) -1 = 0.3

**2.录制相机图像包**

可以 `自定义 RealSense 相机 launch 启动文件 <./diy_camera_config.html>`_ 给 D430 相机专用。

.. code-block:: bash

    # 启动相机
    roslaunch realsense2_camera rs_camera_d430.launch

    # 注意打开两个 rqt_image_view 同时查看两个摄像头的图像，保证标定板在两个摄像头图像里面。
    rqt_image_view

    # 更改图片发布的频率并发布到指定话题，打开两个终端，分别执行：
    # 通常设备采集的频率为 20-60 hz, 这会使得标定的图像过多, 而导致计算量太大. 将topic的频率降低到 4hz 左右进行采集.
    rosrun topic_tools throttle messages /camera/infra1/image_rect_raw 4.0 /infra_left
    rosrun topic_tools throttle messages /camera/infra2/image_rect_raw 4.0 /infra_right

录制包操作细节：D435i静止，标定板移动。四个维度移动，前后左右上下及倾斜。

.. code-block:: bash

    # 回到 kalibr 所在的目录，录制相机bag包，执行
    rosbag record /infra_left /infra_right -O images.bag

    # 标定相机内参和相机间外参
    rosrun kalibr kalibr_calibrate_cameras --target april_6x6_24x24mm.yaml --bag images.bag --bag-from-to 5 30 --models pinhole-radtan pinhole-radtan --topics /infra_left /infra_right --approx-sync 0.14 

**3.相机标定评估**

标定完后会在当前执行命令的目录下生成三个文件，一个 pdf,一个 yaml，一个 txt。
等待片刻后结果将自动可视化显示，保证所有相机重投影误差在 0.1~0.2 以内，标定结果较好，如下所示。

.. image:: ./assets/camera_calibration.png
  :width: 700
  :alt: camera_calibration

其中相机标定结果文件 images-camchain.yaml 示例：

.. code-block:: yaml

    cam0:                   # cam0相机编号
    cam_overlaps: [1]
    camera_model: pinhole   # cam0相机模型
    # cam0 畸变系数：针孔模型一般默认 k3 为0，因此这里只显示出了四个值
    distortion_coeffs: [-0.01378805419196066, 0.002278788473702715, 0.0007173277022338453, -0.006341399229805932]
    distortion_model: radtan
    # cam0 相机内参
    intrinsics: [391.0320770550118, 387.9456433375324, 314.83224317528516, 243.05566306809567]
    resolution: [640, 480]  # cam0 图像分辨率
    rostopic: /infra_left   # cam0 图像话题
    cam1:                   # cam1 相机编号
    T_cn_cnm1:              # 将 cam0 相机坐标系转换为 cam1 相机坐标系的外参矩阵
    - [0.9999982915331912, -0.00031303784731164517, -0.0018217952711038997, -0.04972812293434749]
    - [0.0003167560316089834, 0.9999978669601184, 0.002041014658102277, -3.6665360162458345e-05]
    - [0.0018211524703070222, -0.002041588235736951, 0.9999962576535776, 0.0014231911875602474]
    - [0.0, 0.0, 0.0, 1.0]
    cam_overlaps: [0]
    camera_model: pinhole   # cam1相机模型
    # cam1 畸变系数：针孔模型一般默认 k3 为0，因此这里只显示出了四个值
    distortion_coeffs: [-0.004326382830568126, -0.008360676153607263, 0.00019896224536200172, -0.006517330768703903]
    distortion_model: radtan
    # cam1 相机内参
    intrinsics: [390.92818900850614, 388.52174683212223, 316.74730795452746, 242.1032869823098]
    resolution: [640, 480]  # cam1 图像分辨率
    rostopic: /infra_right  # cam1 图像话题

IMU标定
----------------------------------------------

.. code-block:: bash

    # 1.启动飞控IMU，可使用 rqt_topic 检查飞控IMU数据是否正常发送
    # 运行后静置飞机在水平面两小时以上以保证充足的IMU数据
    roslaunch mavros px4.launch fcu_url:=/dev/ttyACM0:921600
    # 2.录制IMU数据包
    rosbag record -O x152b_imu /mavros/imu/data_raw
    # 3.标定IMU
    roslaunch imu_utils fcu_imu.launch
    # 新建一个终端以400倍速播放IMU数据
    rosbag play -r 400 x152b_imu.bag

最终会生成一堆文件，只用关注 `yaml` 文件即可，关注角速度和加速度的里面 avg 部分的值即可，就是用红框框出来的这四个：

.. image:: ./assets/imu_calibration_result.png
  :width: 500
  :alt: imu_calibration_result

新建一个 `imu.yaml` 文件，填入红框内的数据，用于接下来的联合标定

.. code-block:: bash

    rostopic: /imu
    update_rate: 200.0 # 以实际IMU采集频率填写(Hz)

    gyroscope_noise_density: 1.5331156827140093e-03
    gyroscope_random_walk: 1.6734607279923772e-05

    accelerometer_noise_density: 1.8278801197156819e-02
    accelerometer_random_walk: 5.154477377534344e-04


联合标定
----------------------------------------------

.. code-block:: bash
        
    # 1.启动相机
    roslaunch realsense2_camera rs_camera_d430.launch
    # 2.打开三个终端分别执行：
    rosrun topic_tools throttle messages /camera/infra1/image_rect_raw 20.0 /infra_left
    rosrun topic_tools throttle messages /camera/infra2/image_rect_raw 20.0 /infra_right
    rosrun topic_tools throttle messages /mavros/imu/data_raw 200.0 /imu
    # 3.注意打开两个 rqt_image_view 同时查看两个摄像头的图像，保证标定板在两个摄像头图像里面。
    rqt_image_view
    # 4.录制 Cam-IMU 包
    # 录制包操作细节：D435i静止，标定板移动。四个维度移动，前后左右上下及倾斜。
    rosbag record -O imu_stereo_20240709.bag /infra_left /infra_right /imu
    # 5.联合标定
    rosrun kalibr kalibr_calibrate_imu_camera --target april_6x6_24x24mm.yaml --cam double_cam_20240709-camchain.yaml --imu imu.yaml --bag imu_stereo_20240709.bag

等待片刻，在生成的 pdf 报告里面，两个相机的重投影误差都小于 0.2 才算可以。如下面两幅图所示。

.. |image1| image:: ./assets/cam2imu_calibration_1.png
   :alt: Image 1
   :width: 500px
   :height: 280px

.. |image2| image:: ./assets/cam2imu_calibration_2.png
   :alt: Image 2
   :width: 500px
   :height: 270px

.. list-table::
   :widths: auto
   :header-rows: 0

   * - |image1|
     - |image2|

.. TODO(Derkai):需要将配置文件保存到专用的配置文件夹里面
保存结果
----------------------------------------------
现在你可以手动将标定的结果存放到项目下了



至此，通过传感器标定确保了数据源准确，接下来你可以开始 `部署算法并进行测试 <./combinatorial_algorithms.html>`_ 了
