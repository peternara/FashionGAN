# Copyright (c) 2019, NVIDIA CORPORATION. All rights reserved.
#
# This work is licensed under the Creative Commons Attribution-NonCommercial
# 4.0 International License. To view a copy of this license, visit
# http://creativecommons.org/licenses/by-nc/4.0/ or send a letter to
# Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

"""Global configuration."""

#----------------------------------------------------------------------------
# Paths.

result_dir = 'results'
data_dir = '/dataset'
cache_dir = 'cache'
run_dir_ignore = ['results', '/dataset', 'cache']

#----------------------------------------------------------------------------

# floyd run --gpu2 --env pytorch-1.0 --data wmreynol5/datasets/fashion_middle/5:fashion_middle "python train.py"
# floyd run --gpu2 --env pytorch-1.0 --data wmreynol5/datasets/dataset/1:dataset "python train.py"
