# in your Dockerfile
FROM sphinxdoc/sphinx

WORKDIR /docs
# ADD requirements.txt /docs
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple  pydata-sphinx-theme
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple  sphinxawesome-theme