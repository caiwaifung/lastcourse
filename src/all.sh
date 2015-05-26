for i in {9,4,8,12,16,20,24,30}; do 
    cur="PCA$i"
    flag=""
    if [ $i == 9 ]; then
        cur="ColorMomentHSV9"
    fi
    echo "${cur}:"
    #python run.py a $cur data5k $i $flag | grep '#access\|#split'
    python run.py a $cur data5k $i $flag | grep '#correct'
done
