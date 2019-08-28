# Valerio
# 2019, Aug 29
# check the 2nd column of all the calibration files
for f in ../201{8,9}/*.* ; do awk -v ff=$f 'BEGIN{print ff}{c[$2]++}END{for(v in c)print v,c[v]}' $f;done
