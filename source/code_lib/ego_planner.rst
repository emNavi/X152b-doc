Ego-Planner 规划算法
==============================================

.. TODO(Derkai): 需要解决视频无法播放的问题
.. raw:: html

    <video width="600" controls>
      <source src="https://emnavi-doc-img.oss-cn-beijing.aliyuncs.com/oss_prj_test/video/2024-09-18 22-55-05.mp4" type="video/mp4">
      Your browser does not support the video tag.
    </video>

环境配置与模块编译
----------------------------------------------

.. code-block:: bash

    # 进入 X152b 项目根目录执行
    bash src/ego_planner_swarm_v1/ego_planner_swarm_v1_setup.sh

当终端提示 `Ego-Planner-Swarm-V1 setup completed successfully!` 时，表明 Ego-Planner-Swarm-V1 安装配置完成。

算法使用
----------------------------------------------

.. code-block:: bash

    # 进入 X152b 项目根目录执行
    # 初始化无人机
    bash scripts/one_shot_single.sh
    # 启动 Ego-Planner 规划算法
    bash src/ego_planner_swarm_v1/ego_planner_run.sh

使用建议
----------------------------------------------

1、调整油门估计：可以先关闭油门估计，使用手动估计的油门值，并且对油门速度做一下限制，避免飞机起飞后直接炸机

.. TODO(Derkai): 这里缺几张动图或者短视频用于展示不同参数的影响

常见问题
----------------------------------------------