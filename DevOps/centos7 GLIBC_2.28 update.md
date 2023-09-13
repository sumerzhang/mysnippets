centos /lib64/libc.so.6: version `GLIBC_2.28' not found (required by

解决方案：升级glibc到2.28版本


```shell
	wget https://mirror.bjtu.edu.cn/gnu/libc/glibc-2.28.tar.xz 
	sudo tar -xf glibc-2.28.tar.xz -C /usr/local/
	cd /usr/local/glibc-2.28/ 
	sudo mkdir build 
	cd build/ 
	sudo ../configure --prefix=/usr/local/glibc-2.28
	```
	运行到…/configure --prefix=/usr/local/glibc-2.28时报错
	报错1：
	configure: error: in `/root/test/glibc-2.28/build’:  
	configure: error: no acceptable C compiler found in $PATH
	```bash
	yum install gcc -y
	```
	报错2：
	These critical programs are missing or too old: make bison compiler  
	Check the INSTALL file for required versions.
	解决方案： make bison compiler太过老旧。按下文方法解决。
	### centos 升级GCC编译器
	```bash
	yum -y install centos-release-scl 
	yum -y install devtoolset-8-gcc devtoolset-8-gcc-c++ devtoolset-8-binutils 
	scl enable devtoolset-8 bash 
	echo "source /opt/rh/devtoolset-8/enable" >>/etc/profile
	```
	### 升级make
	```bash
	wget http://ftp.gnu.org/gnu/make/make-4.2.tar.gz
	tar -xzvf make-4.2.tar.gz
	cd make-4.2
	sudo ./configure
	sudo make
	sudo make install
	sudo rm -rf /usr/bin/make
	sudo cp ./make /usr/bin/
	make -v
```

	### 升级glibc-2.28
	```bash
	wget  https://mirror.bjtu.edu.cn/gnu/libc/glibc-2.28.tar.xz
	sudo tar -xf glibc-2.28.tar.xz -C /usr/local
	cd /usr/local/glibc-2.28/
	sudo mkdir build
	cd build/
	sudo yum install -y bison
	sudo ../configure --prefix=/usr --disable-profile --enable-add-ons --with-headers=/usr/include --with-binutils=/usr/bin
	sudo make  //make 运行时间较长，可能会有半小时
	sudo make install
```

	nvim: /lib64/libm.so.6: version `GLIBC_2.29' not found (required by nvim)
	```bash
	wget https://mirror.bjtu.edu.cn/gnu/libc/glibc-2.29.tar.xz
	sudo tar -xf glibc-2.29.tar.xz -C /usr/local/
	cd /usr/local/glibc-2.29/ 
	sudo mkdir build 
	cd build/ 
	sudo yum install -y bison
	sudo ../configure --prefix=/usr --disable-profile --enable-add-ons --with-headers=/usr/include --with-binutils=/usr/bin
	sudo make  //make 运行时间较长，可能会有半小时
	sudo make install
```

