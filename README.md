# Hardhat Package Manager
Builds from source including gcc, glibc and binutils
Useful for building new glibc and compiler on older linuxes.
I use it on Fedora 24 and CentOS 6. MIT license.

It builds binutils, glibc and gcc from source and uses the newly
built glibc. In the future I would like to add the option of using
preinstalled compilers instead and a preinstalled glibc and make
it work for mingw64 on windows.

The goal is to be something like homebrew/linuxbrew but in python
instead of ruby.

## To bootstrap

### Python 2.6 bootstrap
1. Run `python setup.py sdist`
2. `cd dist`
3. `scp *.tar.gz YOUR_SERVER:YOUR_LOCATION`
4. `ssh YOUR_SERVER`
5. `cd YOUR_LOCATION`
6. `tar xvf hardhat-VERSION.tar.gz`
7. `cd hardhat-VERSION`
8. `./bootstrap.sh --prefix=YOUR_PREFIX` or `./bootstrap.sh --prefix=YOUR_PREFIX --no-sudo` if you do not have sudo
9. `. YOUR_PREFIX/init.sh`
10. `hardhat install YOUR_PROGRAMS`
11. `hardhat --help` for more information

## To use
`. HARDHAT_PREFIX_DIR/init.sh`

`hardhat install emacs`

or

`hardhat list`

to see what is available

Thanks to Linux from Scratch and Beyond Linux from Scratch for most
of the information and for the patches applied using patch.

Estimated package counts as of 2017-10-14
doc       = 3  
java      = 5  
ocaml     = 9  
other     = 463  
perl      = 4  
python    = 177  
toolchain = 3  
x11       = 54

----------------  
total     = 742  
