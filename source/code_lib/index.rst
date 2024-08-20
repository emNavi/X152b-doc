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


本项目提供了丰富的前沿无人机人工智能算法，仅需3步即可进行实机飞行

1、首先进行 `无人机传感器标定 <./calibration.html>`_，确保数据源准确

2、 `你可以参考这个示例 <./combinatorial_algorithms.html>`_ ,按需组建自己的 `感知-规划-控制` 工作流并部署到无人机。

3、 `算法评估与可视化 <./foxglove.html>`_


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
