算法部署
============

.. toctree::
   :maxdepth: 2
   :caption: 目录
   :hidden:

   calibration
   vins_fusion
   ego_planner
   combinatorial_algorithms
   algorithm_evaluation_and_visualization

本项目提供了丰富的前沿无人机自主飞行算法，首先进行以下准备工作：

.. TODO(Derkai):通用环境后期可更新至系统装机驱动，这样就可以不用在这一步进行通用环境配置了,而是仅进行子算法模块的配置与编译

.. code-block:: bash

   # 下载 X152b 开源项目
   git clone --recursive https://github.com/emNavi/X152b.git

   # 环境配置与模块编译
   bash scripts/build.sh

项目主要结构介绍
------------------

.. code-block:: bash

    x152b
      ├── scripts # 存放各类工具脚本
      │   ├── build.sh # 通用环境配置
      │   ├── one_shot_single.sh # 无人机初始化
      │   ├── takeoff.sh # 起飞
      │   ├── land.sh # 降落
      │   └── kill_one_shot.sh  # 关闭所有程序
      └── src
          ├── autonomous_drone_sdk # 各类基础功能实现
          │   ├── global_interface # 接口层（存放参数文件、通讯接口等）
          │   └── modules # 飞控驱动、相机驱动、通讯驱动等实现
          │
          │   # 这里存放所有已适配算法，以及一键配置、运行的脚本
          ├── 算法1
          ├── 算法2
          └── ... # 更多适配算法持续更新中

**在无人机准备就绪后，仅需3步即可部署算法进行实机飞行：**

..  添加这行 <br> 是因为下面的按钮和上面的文字需要一行空行

.. raw:: html

   <br>

.. TODO(Derkai): 可以考虑换成图片

.. raw:: html

   <a href="./calibration.html" class="firmware_prepare_index_button-blue">1.无人机传感器标定</a>
   <a href="./combinatorial_algorithms.html" class="firmware_prepare_index_button-green">2.组合算法并部署</a>
   <a href="./algorithm_evaluation_and_visualization.html" class="firmware_prepare_index_button-red">3.算法评估与可视化</a>

.. .. raw:: html

..    <div class="combinatorial_algorithms_process_image-block">
..        <a href="./calibration.html">
..            <img src="./assets/block_calibration.png" alt="Block 1">
..        </a>
..        <img src="./assets/arrow.png" alt="Arrow 1" class="combinatorial_algorithms_process_arrow">
..        <a href="./combinatorial_algorithms.html">
..            <img src="./assets/block_combinatorial_algorithms.png" alt="Block 2">
..        </a>
..        <img src="./assets/arrow.png" alt="Arrow 2" class="combinatorial_algorithms_process_arrow">
..        <a href="./algorithm_evaluation_and_visualization.html">
..            <img src="./assets/block_algorithm_evaluation_and_visualization.png" alt="Block 3">
..        </a>
..    </div>


.. 1、首先进行 `无人机传感器标定 <./calibration.html>`_，确保数据源准确

.. 2、 `你可以参考这个示例 <./combinatorial_algorithms.html>`_ ,按需组建自己的 `感知-规划-控制` 工作流并部署到无人机。

.. 3、 `算法评估与可视化 <./algorithm_evaluation_and_visualization.html>`_


目前已适配的算法
-----------------------------------------------
.. list-table::
   :widths: 10
   :align: left
   :header-rows: 1

   * - `VINS-Fusion 视觉里程计 <./vins_fusion.html>`_
   * - `Ego-Planner 规划算法 <./ego_planner.html>`_
   * - 更多算法持续更新中...
