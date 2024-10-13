开篇介绍
=============

.. raw:: html

    <style> .red {color:#; font-weight:bold; font-size:16px} </style>

.. role:: red

.. :red:`test - this text should be red`

项目简介
---------

*Embodied Navigation* (**emNavi**) 是一项基于感知的无人机具身智能导航与控制的研究项目。旨在将最前沿的人工智能与优化方法部署于嵌入式层级的移动机器人之上。
该项目开发了无人机科研平台 **X152b**、 **X660** 等，精简并集成了多种基于无人机平台的前沿研究算法。本文介绍了 **emNavi** 项目基于 **X152b** 型无人机的二次开发平台，以及几种典型智能算法的一键部署。

X152b平台
-------

X152b 是一款集成了双目深度相机 D430、轻量级机载算力平台 Edge2、Mini PX4 飞控、以及穿越机动力套件的自主飞行无人机。
X152b 预装载了 Ubuntu20.04.6-LTS 操作系统，并提供基于此环境的无人机感知、规划、控制、以及学习的二次开发平台。

.. |image1| image:: ./assets/X152b-main.png
   :target: ../index.html
   :alt: Image 1
   :width: 300px
   :height: 180px

.. |image2| image:: ./assets/X152b-front.png
   :target: ../index.html
   :alt: Image 2
   :width: 300px
   :height: 170px

.. |image3| image:: ./assets/X152b-top.png
   :target: ../index.html
   :alt: Image 3
   :width: 300px
   :height: 170px

.. list-table::
   :widths: auto
   :header-rows: 0

   * - |image1|
     - |image2|
     - |image3|

.. TODO(): 可以使用 Three.js 生成用户可点击的3D模型，并且还有爆炸图

.. .. raw:: html

..    <iframe title="3D Model" 
..            width="100%" 
..            height="400px"
..            frameborder="0" 
..            allowfullscreen 
..            mozallowfullscreen="true" 
..            webkitallowfullscreen="true" 
..            allow="autoplay; fullscreen; vr" 
..            src="https://sketchfab.com/models/b0e69a53c4944882b3a4a4e4ed4df80a/embed">
..    </iframe>

.. TODO(Derkai): 这里可以做一个三分页面块，用于一目了然的知道网站的文档组织由三大块构成

文档组织
------------------
本网站分为三个部分，主要内容概括如下：

- 快速配置：快速上手X152b。

- 算法部署：介绍基于X152b的前沿开源算法部署方法。该部分将会随着我们对更多算法的优化与适配而不断扩充。

- 问题答疑：针对无人机软硬件各种常见问题的解答。

