# X152b Documentation

> 此文档为使用指南

https://x152b-doc.readthedocs.io/

## Quick Start

Clone code 

构建docker image
```bash
sudo docker build -t sphinxdoc/sphinx:awesome . 
```

编译，可以直接使用docker完成编译，在X152b目录下使用
```bash
sudo docker run --rm -v $(pwd):/docs sphinxdoc/sphinx:awesome make html
```
运行后生成的静态文档存在 `build/html`中， 可以安装vscode 中的 Live Server 插件以展示效果(直接打开index.html是一样的，只不过重新编译后需要手动选择刷新)。

Live Server 的使用方法为，将 X152b-doc 作为一个工作空间打开，现在打开 `build/html/index.html`,在文件中右键选择`Open with Live Server`。



# 参考

Build HTML document::
```bash
sudo docker run --rm -v $(pwd):/docs sphinxdoc/sphinx make html
```