连接至飞行器机载电脑
===============

X152b 提供了四种连接至机载电脑的方式
- USB 直连
- 使X152b作为wifi接入点(AP Mode)
- 使X152b的连接至局域网(STA Mode)

USB 直连
--------------

在机载PC上电前，拔掉如下端口上插入的任何设备，此时当PC上电后会启用usb-gadget功能，现在可通过USB将PC连接至任意电脑，电脑中会新增一个网卡，手动配置其IP为


AP Mode
--------------

.. warning::
    使用 function键在2秒内短按3次会进入 MaskROM 模式

短按一次，退出热点模式
长按2s,进入热点模式（AP mode），热点名称默认为 hostname

现在你可以登录到机载pc上了
.. code-block:: bash

    (base) hao@hao-5900x-lltech:~$ ssh emnavi@192.168.2.1
    emnavi@192.168.2.1's password: 

    Welcome to Fenix 1.5.1 Ubuntu 20.04.6 LTS Linux 5.10.66  
    __  __     _ ____ ____  _     
    \ \/ /    / | ___|___ \| |__  
    \  /_____| |___ \ __) | '_ \ 
    /  \_____| |___) / __/| |_) |
    /_/\_\    |_|____/_____|_.__/ 
                                

    * Website:        https://www.khadas.com
    * Documentation:  https://docs.khadas.com
    * Forum:          https://forum.khadas.com

    Last login: Sat May 11 13:11:40 2024 from 192.168.2.198
    emnavi@emNavi-x152b-ubuntu20:~$

STA Mode
--------------

请使用nmcli配置wifi

.. code-block:: bash

    # 当触发时执行一次，STA -> AP
    # 配置一个热点叫做 Hostpot,2.4Ghz的似乎

    sudo nmcli con add type wifi ifname wlan0 mode ap con-name Hostspot ssid khadas_ap_5G
    sudo nmcli con modify Hostspot 802-11-wireless.band a
    sudo nmcli con modify Hostspot 802-11-wireless.channel 149
    sudo nmcli con modify Hostspot 802-11-wireless-security.key-mgmt wpa-psk
    sudo nmcli con modify Hostspot 802-11-wireless-security.proto rsn
    sudo nmcli con modify Hostspot 802-11-wireless-security.group ccmp
    sudo nmcli con modify Hostspot 802-11-wireless-security.pairwise ccmp
    sudo nmcli con modify Hostspot 802-11-wireless-security.psk 12345678
    sudo nmcli con modify Hostspot ipv4.addresses 192.168.2.1/24
    sudo nmcli con modify Hostspot ipv4.gateway 192.168.2.1
    sudo nmcli con modify Hostspot ipv4.method shared
    sudo nmcli con up Hostspot

    # 连接到新wifi

    # 关闭 Hostpot
    sudo nmcli connection down Hostspot
    
    sudo nmcli device wifi rescan 
    sudo nmcli device wifi connect






.. fenix 默认固件P按键为电源键，现在通过设置将其定义为连接键




.. sudo systemctl stop systemd-logind.service


.. evtest /dev/input/event1 

.. https://forum.khadas.com/t/overwrite-button-behaviour/21111



.. 短按是无效了，长按还是有效
.. 似乎无法禁止开机自启动




ID 号
-----

ID号是用户为X152b定义的用于分辨无人机的编号，当没有定义时，ID=-1。用户自定义的ID号需要在 0~255之间


升级
---

请不要手动升级ubuntu版本


