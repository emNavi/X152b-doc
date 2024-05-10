版本修改记录
==============================================
镜像地址 http://10.42.0.180/webdav/X-152b_image_zip/

V1.0
------------

- 基本的编译环境
- ROS-noetic
- 工作代码
	- ego_env_sh
	- swarm_ws
	- param_files
- khadas 专用分支
- nomachine
- 清华源 （apt,ros）

V1.1
------------

- 新的开机logo
- nomachine 自动开启
- 增加 myclashshell


emnavi-x152b-V0.1
------------

基于 V1.1，相较于 fenix 原始固件有以下特征

- X152b开机logo
- 修改了hostname
- 安装 nautilus-extension-gnome-terminal
- 基本的编译环境
    - Eigen3
- 安装ROS-noetic，以及常用包
    - ros-noetic-foxglove-bridge
- 清华源 （apt,ros）
- 安装nomachine，并开机自启
- ubs-gadget，ip 为 192.168.108.1
- 预先编译了ego_planner_v1_all_in_one