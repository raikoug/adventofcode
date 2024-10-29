

get_last_day() {
    # `find ./ -type d | grep day | awk -F "_" '{print $2}' | sort -n | tail -n 1` find current last day
    # add 1 and create new day directory
    # day_{last_day+1} 
    last_day=`find ./ -type d | grep day | awk -F "_" '{print $2}' | sort -n | tail -n 1`
    echo $last_day
}

create_dir() {
    last_day=`get_last_day`
    new_day=$((last_day+1))
    mkdir day_$new_day
    echo day_$new_day
}

create_files() {
    dirname=$(create_dir)
    touch $dirname/input_1.txt
    touch $dirname/indstructions.md
}

create_files