# V. Mascagna - vmascagn@jlab.org - 2019, Dec 23
# 
# If the numbering of the layers is already 1,2, do not change
# if is 0,1, move to 1,2
#
# Print to stdout

#!/usr/bin/env bash
if [ $# -ne 1 ];then
    echo "Error: provide the file name as 1st argument";
    exit 1
fi
awk 'BEGIN{add1=0}{if(NR==1)if($2==0) add1=1;$2+=add1;print }' $1
