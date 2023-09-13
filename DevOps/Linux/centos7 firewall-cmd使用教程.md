firewalld-cmd常用命令，以443端口举例，永久操作需要添加 --permanent 参数，其他端口放行替换443即可。

添加规则
临时添加：
```shell
firewall-cmd --zone=public --add-port=443/tcp
```

持久添加：
```shell
firewall-cmd --permanent --zone=public --add-port=443/tcp

```

添加完规则要生效需要让防火墙重新加载规则

重新加载规则
```shell
firewall-cmd --reload
```

删除规则
临时删除：

firewall-cmd --zone=public --remove-port=443/tcp
持久删除：

firewall-cmd --permanent --zone=public --remove-port=443/tcp
删除完规则要生效需要让防火墙重新加载规则

查看所有已放行的端口
firewall-cmd --zone=public --list-ports