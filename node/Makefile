
LIB_NODE = node-$(NODE_VERSION)/out/Release/lib.target/libnode.so

libnode-$(NODE_VERSION).so: $(LIB_NODE)
	cp $^ $@

$(LIB_NODE):
	cd node-$(NODE_VERSION); ./configure
	$(MAKE) -C node-$(NODE_VERSION) -j4

# Support for OSv's combined kernel+module build system ('make modules=node'
# and 'make clean')
#VERSION=4.1.1
VERSION=4.6.1
#VERSION=6.9.1
module:
	if test ! -d node-$(VERSION); then ./GET $(VERSION); $(MAKE) NODE_VERSION=$(VERSION); fi
	echo '/libnode.so: $${MODULE_DIR}/libnode-$(VERSION).so' > usr.manifest
	: > bootfs.manifest
clean:
	rm -rf node-$(VERSION) usr.manifest bootfs.manifest libnode-$(VERSION).so
