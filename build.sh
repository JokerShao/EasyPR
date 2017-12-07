#!/usr/bin/env bash

rm -rf build
python autoconfig.py
mkdir build
cd build
cmake ..
make -j8
