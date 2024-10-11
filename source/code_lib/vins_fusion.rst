Vins-Fusion 视觉里程计
==============================================

环境配置与模块编译
----------------------------------------------

.. code-block:: bash

    # 进入 X152b 项目根目录执行
    bash src/vins_fusion/vins_fusion_setup.sh

使用
----------------------------------------------

.. code-block:: bash

    # 进入 X152b 项目根目录执行
    # 初始化无人机
    bash scripts/one_shot_single.sh
    # 启动 Vins-Fusion 视觉里程计
    bash src/vins_fusion/vins_fusion_run.sh

VINS 里程计算法支持运行时自动优化 相机-IMU 的内外参，可根据标定情况选择是否优化

.. code-block:: yaml

    # 修改 realsense_stereo_imu_config.yaml
    estimate_extrinsic: # 0 当标定的内外参误差较小，使用手动填入的预设值，不开启优化
                        # 1 当标定的内外参误差较大，只能给出粗略的值时，开启内外参自动优化

调参建议
----------------------------------------------

1、确保初始化时，即IMU预积分阶段时，无人机处于水平静止状态.

.. TODO(Derkai): 这里缺几张动图或者短视频用于展示不同参数的影响

常见问题
----------------------------------------------