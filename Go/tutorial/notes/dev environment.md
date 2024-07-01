# Go dev environment in Centos 8

## 安装 Centos8

切换root用户，创建going用户
```shell
useradd going 
passwd goging 

sed -i '/^root.*ALL=(ALL).*ALL/a\going\tALL=(ALL) \tALL' /etc/sudoers  # 添加sudoers

```

配置$HOME/.bashrc
```shell
# Basic envs
export LANG="en_US.UTF-8" # 设置系统语言为 en_US.UTF-8，避免终端出现中文乱码
export PS1='[\u@dev \W]\$ ' # 默认的 PS1 设置会展示全部的路径，为了防止过长，这里只展示
export WORKSPACE="$HOME/workspace" # 设置工作目录
export PATH=$HOME/bin:$PATH # 将 $HOME/bin 目录加入到 PATH 变量中
# Default entry folder
cd $WORKSPACE # 登录系统，默认进入 workspace 目录
```


## 安装依赖和配置

## Go编译环境安装和配置

## Go 开发IDE安装和配置