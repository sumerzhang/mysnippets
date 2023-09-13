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
![1694601167975.png](https://imgs.noper.top/im/2023/09/13/65018fd13a653.png)

# 国内直接运行modular install mojo比较慢，主要看网速

modular install mojo
```
![1694601234872.png](https://imgs.noper.top/im/2023/09/13/650190149d020.png)

配置一下环境变量
![1694601280060.png](https://imgs.noper.top/im/2023/09/13/650190420857d.png)

5. Open the Ubuntu workspace in VS Code with this:

code .
Command copied to clipboard

6. Get started with Hello World!
![1694601116639.png](https://imgs.noper.top/im/2023/09/13/65018f9deba18.png)