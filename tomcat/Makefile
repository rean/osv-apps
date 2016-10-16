.PHONY: module
module: upstream

upstream:
	./GET
	cp tomcat-cmd-line.sh ROOTFS/usr/tomcat/bin

clean:
	rm -rf upstream ROOTFS *.pyc
