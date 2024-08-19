常见问题 Q&A
========================



如何修改开机启动 Logo
------------------------

在 `/etc/update-motd.d/00-header` 中

.. code-block:: bash

  #!/bin/bash

  KERNEL_VER=$(uname -r)

  . /etc/os-release
  . /etc/fenix-release

  printf "\nWelcome to \e[0;91mFenix\x1B[0m %s %s %s\n" "$VERSION $PRETTY_NAME Linux $KERNEL_VER"

  # TERM=linux toilet -f standard -F metal "Khadas $BOARD"
  # X-152b 的位置就是会显示大logo的地方
  TERM=linux toilet -f standard -F metal "X-152b"

  if cat /proc/cmdline | grep -q reboot_test; then
          TERM=linux toilet -f standard -F metal "REBOOT TEST"
  fi

.. 效果如下
.. TODO(Derkai):这里缺一张开机修改后的Logo图


常见网络问题
------------------------

clash 的GitHub配置

.. code:: bash
    
    Host github.com
        User git
        Port 443
        HostName ssh.github.com
        IdentityFile ~/.ssh/id_rsa
        ProxyCommand nc -v -x 127.0.0.1:7891 %h %p