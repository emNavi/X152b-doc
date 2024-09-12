常用算法部署
============

.. toctree::
   :maxdepth: 2
   :caption: 目录
   :hidden:

   calibration
   combinatorial_algorithms
   vins_fusion
   openvins
   ego_planner
   ipc


本项目提供了丰富的前沿无人机自主飞行算法，首先进行以下准备工作

.. code-block:: bash

   # 下载 X152b 开源项目
   git clone --recursive https://github.com/emNavi/X152b.git

   # 环境配置与模块编译
   bash scripts/build.sh

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
   * - `OpenVINS 视觉里程计 <./openvins.html>`_
   * - `Ego-Planner 规划算法 <./ego_planner.html>`_
   * - `IPC 规划控制算法 <./ipc.html>`_
