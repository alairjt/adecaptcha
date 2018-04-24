#!/usr/bin/env bash

cd app

apt-get install libmad0-dev
git clone --depth 1 https://github.com/jaqx0r/pymad
cd pymad/
python config_unix.py
python setup.py install

cd ..

wget -O - http://ekyo.nerim.net/software/pyogg/pyao-0.82.tar.gz | tar xzv
apt-get install libao-dev
wget -O - https://launchpad.net/ubuntu/+archive/primary/+files/pyao_0.82-5build1.debian.tar.gz| tar xzv
patch -p0 -i debian/patches/driver_id.patch
patch -p0 -i debian/patches/int_format_strings.patch
patch -p0 -i debian/patches/python25.patch
cd pyao-0.82/
python config_unix.py
python setup.py install

cd ..

rm -r pyao-0.82 debian/ pymad

rm adecaptcha/pwrspec.so
rm adecaptcha/pwrspec.c
python setup.py build_ext --inplace

cd adecaptcha
cd libsvm-3.17
make clean
make lib
cd ..
rm svm;ln -s libsvm-3.17/python/ svm
cd ..
#pip install -r requirements.txt
#cd adecaptcha
#python adecaptcha.py ulozto.cfg ./test1.wav

