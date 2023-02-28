#!/bin/bash
/***********************************************
# Copyright (c) 2019, Shanghai
# All rights reserved.
#
# @Filename: source.sh
# @Version：V1.0
export TVM_HOME=$PWD
export PYTHONPATH=$TVM_HOME/python:${PYTHONPATH}
export PYTHONPATH=$TVM_HOME/utils:${PYTHONPATH}
export LD_LIBRARY_PATH=$TVM_HOME/build_gpu/:$LD_LIBRARY_PATH
