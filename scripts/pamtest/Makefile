.PHONY: all

all:
	gcc -o pamtest pamtest.c -lpam
	cp pamtest.pamd $(HARDHAT_PREFIX)/etc/pam.d/pamtest
	./pamtest $(USER) || /bin/true
	rm $(HARDHAT_PREFIX)/etc/pam.d/pamtest
