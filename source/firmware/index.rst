系统及固件设置
============

.. toctree::
    :titlesonly:
    :glob:

    *


Tips
-------


.. code-block:: bash

    # 添加 在文件管理器中添加 open in terminal
    sudo apt install nautilus-extension-gnome-terminal

    # 安装 ros 以及常用包



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



