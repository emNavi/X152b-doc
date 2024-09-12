使用 foxglove 进行可视化
=======================

手动编译 foxglove_brigdge
------------------------

.. code:: bash

    mkdir -p ~/dependencies_ws/src
    cd ~/dependencies_ws
    git clone https://github.com/foxglove/ros-foxglove-bridge.git src/ros-foxglove-bridge
    catkin_make
    source install/local_setup.bash

测试

```bash
roslaunch --screen foxglove_bridge foxglove_bridge.launch
```
