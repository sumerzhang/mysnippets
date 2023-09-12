### 1. 创建安装目录
```shell
sudo -i 

mkdir -p /data/docker_data/lsky-pro

cd /data/docker_data/lsky-pro

nano docker-compose.yml
```

```yaml 
version: '3'
services:
    lsky-pro:
        container_name: lsky-pro
        image: dko0/lsky-pro
        restart: always
        volumes:
            - /data/docker_data/lsky-pro/lsky-pro-data:/var/www/html  #映射到本地
        ports:
            - 7791:80
        environment:
            - MYSQL_HOST=mysql
            - MYSQL_DATABASE=lsky-pro
            - MYSQL_USER=lsky-pro
            - MYSQL_PASSWORD=123zshzsk-lsky-pro

    mysql:
        image: mysql:8.0
        container_name: lsky-pro-db
        restart: always
        environment:
          - MYSQL_DATABASE=lsky-pro
          - MYSQL_USER=lsky-pro
          - MYSQL_PASSWORD=lsky-pro
          - MYSQL_ROOT_PASSWORD=123zshzsk-lsky-pro
        volumes:
          - /data/docker_data/lsky-pro/db:/var/lib/mysql

```