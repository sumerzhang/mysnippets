1. Install VS Code, the WSL extension, and the Mojo extension.
2. Install Ubuntu 22.04 for WSL and open it.
3. In the Ubuntu terminal, install the Modular CLI:
```shell
curl https://get.modular.com | \
  MODULAR_AUTH=mut_2dc30aa7773942b99f027f173b6a8610 \
  sh -
```
Command copied to clipboard
4. Install the Mojo SDK:
```shell

# 配置一下全局的国内pip镜像
# pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

# 国内直接运行modular install mojo比较慢，主要看网速

modular install mojo
```


5. Open the Ubuntu workspace in VS Code with this:

code .
Command copied to clipboard

6. Get started with Hello World!