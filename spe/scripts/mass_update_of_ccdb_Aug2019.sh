#!/usr/bin/env bash

# Valerio
# 2019, Aug 29
# This script just PRINTs the commands used on Aug 28th for uploading again

CCDB_CONNECTION=mysql://clas12writer:geom3try@clasdb/clas12

# re-upload to ccdb in run order
for f in ../201{8,9}/*.txt ; do
    run=$(basename $f .txt)
    echo ccdb add calibration/ltcc/spe -r $run- $f
done
