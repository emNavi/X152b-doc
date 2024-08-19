USB Gadget 使用
===============

.. code-block:: bash

    # 启用 gadget
    sudo systemctl enable usb-gadget-khadas.service
    sync
    sudo reboot

    sudo vim /etc/network/interfaces
    #############在其中加入
    auto usb0
        iface usb0 inet static
            address 192.168.108.1
            netmask 255.255.255.0


参考资料
-------------------

https://docs.khadas.com/products/sbc/edge2/configurations/usb-gadget