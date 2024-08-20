# X152b 文档构建用法

文档地址: [https://x152b.readthedocs.io/](https://x152b.readthedocs.io/)

##

1、下载项目
``` bash
git clone https://github.com/emNavi/X152b-doc.git
```

2、构建 Sphinx Docker 容器
```bash
sudo docker build -t sphinxdoc/sphinx:awesome . 
```

3、进行文档内容的修改

4、使用 Sphinx Docker 容器进行编译
```bash
# 在 X152b-doc 目录下执行
sudo docker run --rm -v $(pwd):/docs sphinxdoc/sphinx:awesome make html
```
5、查看更新后的文档结果

运行后生成的静态文档存在 `build/html`中， 可以安装 vscode 中的 Live Server 插件以展示效果(直接打开index.html是一样的，只不过重新编译后需要手动选择刷新)。

Live Server 的使用方法为，将 X152b-doc 作为一个工作空间打开，现在打开 `build/html/index.html`,右键该文件选择 `Open with Live Server`。