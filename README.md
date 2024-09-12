# X152b 文档构建用法

[![Documentation Status](https://readthedocs.org/projects/x152b/badge/?version=latest)](https://x152b.readthedocs.io/en/latest/?badge=latest)

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

## 通过配置 css 文件丰富网页显示效果

例如：想要添加一个按钮样式的图块实现超链接跳转

1、新建一个 css 文件，名为 `button.css` 位于 `source/_static/` 目录下
```css
a.button {
    display: inline-block;
    padding: 10px 15px;
    font-size: 14px;
    color: white;
    background-color: #74ab76;
    border-radius: 5px;
    text-decoration: none;
    border: 1px solid #4CAF50;
}

a.button:hover {
    background-color: #45a049;
    border: 1px solid #45a049;
}
```
2、在 `source/conf.py` 中添加该 css 文件

```python
def setup(app):
    app.add_css_file('button.css')
```

3、在需要修改的网页中添加该按钮效果

```rst
.. raw:: html

   <a href="https://example.com" class="button">Click Here</a>
```

4、使用 Sphinx Docker 容器重新编译，查看修改后的网页效果