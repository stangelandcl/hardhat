.PHONY: install sdist bootstrap stats nix
OLD_VERSION=
VERSION=20180823

sdist:
	python3 setup.py sdist --formats=gztar

bootstrap:
	./bootstrap.sh

install: sdist
	cp dist/hardhat-0.1.tar.gz ~/Downloads
	rm -rf ~/Downloads/hardhat-0.1
	cd ~/Downloads && tar xvf hardhat-0.1.tar.gz
	rm -rf ~/hardhat/${VERSION}
	if [ -z "$OLD_VERSION" ]; then rm -rf ~/hardhat/${OLD_VERSION} ; fi
	cd ~/Downloads/hardhat-0.1 && ./bootstrap.sh --march=native --prefix=~/hardhat/${VERSION} --cpus=.25 --pkgfile=~/vcs/hardhat/config/example.config


install_root: sdist
	mkdir -p ~/Downloads
	cp dist/hardhat-0.1.tar.gz ~/Downloads
	rm -rf ~/Downloads/hardhat-0.1
	cd ~/Downloads && tar xvf hardhat-0.1.tar.gz
	rm -rf ~/hardhat/${VERSION}
	if [ -z "$OLD_VERSION" ]; then rm -rf ~/hardhat/${OLD_VERSION} ; fi
	cd ~/Downloads/hardhat-0.1 && ./bootstrap.sh --use-root --march=native --prefix=~/hardhat/${VERSION} --cpus=.5



stat:
	@echo "Estimated package counts as of $$(date +%Y-%m-%d)  "
	@echo "doc       = $$(($$(find hardhat/recipes/doc -name '*.py' | wc -l) - 1))  "
	@echo "java      = $$(($$(find hardhat/recipes/java -name '*.py' | wc -l) - 2))  "
	@echo "ocaml     = $$(($$(find hardhat/recipes/ocaml -name '*.py' | wc -l) - 2))  "
	@echo "other     = $$(($$(find hardhat/recipes -maxdepth 1 -name '*.py' | wc -l) - 2))  "
	@echo "perl      = $$(($$(find hardhat/recipes/perl -name '*.py' | wc -l) - 1))  "
	@echo "python    = $$(($$(find hardhat/recipes/python -name '*.py' | wc -l) - 2))  "
	@echo "toolchain = 3  "
	@echo "x11       = $$(($$(find hardhat/recipes/x11 -name '*.py' | wc -l) - 2))  "
	@echo "  "
	@echo "----------------  "
	@echo "total     = $$(($$(find hardhat/recipes -name '*.py' -o -path toolchain -prune -o -path cross -prune | wc -l) - 12))  "



