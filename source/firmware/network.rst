常见网络问题
=============

clash 的GitHub配置

.. code:: bash
    
    Host github.com
        User git
        Port 443
        HostName ssh.github.com
        IdentityFile ~/.ssh/id_rsa
        ProxyCommand nc -v -x 127.0.0.1:7891 %h %p