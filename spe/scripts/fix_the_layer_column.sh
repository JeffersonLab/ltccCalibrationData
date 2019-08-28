# Valerio
# 2019, Aug 29
# For each calibration file,
# if the numbering of the layers is already 1,2, do not change
# if is 0,1, move to 1,2

# to detect the coordinate system, use the first layer occurence (0 if it's the 0,1 system, 1 if 1,2) 

for f in ../201{8,9}/*.txt ; do
    newtempname=$(echo $f.new)
    awk -v ff=$f 'BEGIN{add1=0}{if(NR==1)if($2==0) add1=1;$2+=add1;print }' $f > $newtempname ;
    #clean (you are deleting old files! USE WITH CAUTION)
    mv -v $newtempname $f
done
