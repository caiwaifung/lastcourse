for i in {9,4,8,12,16,20,24,30}; do 
    cur="PCA$i"
    if [ $i == 9 ]; then
        cur="ColorMomentHSV9"
    fi
    echo "${cur}:"
    python run.py vio $cur data5k $i | grep '#cor'
done
