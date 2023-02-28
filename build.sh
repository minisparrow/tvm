#!/bin/bash
mkdir -p build_gpu
cp config.cmake build_gpu/
cmake -S . -B build_gpu
cd build_gpu && make -j 10
