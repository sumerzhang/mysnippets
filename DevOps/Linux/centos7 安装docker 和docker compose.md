1. 卸载旧版本docker(如果之前没有装过docker可以忽略)

```shell
yum remove docker docker-common docker-selinux
```
2. 安装 yum-utils 包
sql复制代码更新 yum 包
生产环境中此步操作需慎重，看自己情况，学习的话随便搞
这个命令不是必须执行的，看个人情况，后面出现不兼容的情况的话就必须update了

```shell
yum -y update
sudo yum install -y yum-utils device-mapper-persistent-data lvm2
```

3. 配置稳定仓库（二选一，有其他稳定仓库可以自行配置）

配置国内稳定仓库
```shell
yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
```

配置阿里源仓库
```shell
sudo yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
```

4. 更新一下yum缓存
```shell

sudo yum makecache fast

```

5. 安装docker

```shell
yum install docker-ce

```

6. 验证是否安装成功

```shell
docker version
```

7. 设置开机启动

```shell

systemctl start docker		## 启动

systemctl status docker		## 查看状态

systemctl enable docker		## 开机自启动
```


8. 设置docker国内镜像源（也可不设置，但是官方镜像源国内有时候可能拉不到）
8.1 国内的镜像地址
8.1.1 docker中国区官方镜像
https://registry.docker-cn.com

8.1.2 网易
http://hub-mirror.c.163.com

8.1.3 中国科学技术大学
https://docker.mirrors.ustc.edu

8.2 修改daemon.json文件
8.2.1 创建或者修改 /ect/docker/daemon.json文件
vim /etc/docker/daemon.json
8.2.2 添加或者修改如下内容
```json
{
    "registry-mirrors": ["<https://registry.docker-cn.com>"]
}

```


8.3 重启docker服务

```shell
systemctl restart docker

```

8.4 查看源配置是否成功

执行docker info
查看字段：Registry Mirrors
9. 安装docker-compose编排器
9.1 安装docker-compose

官方地址（速度emmm，可能会很慢）

执行
```shell
sudo curl -L "https://github.com/docker/compose/releases/download/1.24.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

```

9.2 赋予执行权限

```shell
sudo chmod +x /usr/local/bin/docker-compose

```


9.3 创建软链接

```shell
ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
```

9.4 验证docker-compose是否安装成功
执行docker-compose -version
