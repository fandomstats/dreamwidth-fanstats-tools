#!/bin/bash
#http://daredevilkink.dreamwidth.org/725.html?view=top-only&page=2#comments
#wget 

function fatal {
  echo -e "\e[1;31;40mFATAL ERROR: \e[0m$1" >&2
  exit 1
}

function countdown
{
        local OLD_IFS="${IFS}"
        IFS=":"
        local ARR=( $1 )
        local SECONDS=$((  (ARR[0] * 60 * 60) + (ARR[1] * 60) + ARR[2]  ))
        local START=$(date +%s)
        local END=$((START + SECONDS))
        local CUR=$START

        while [[ $CUR -lt $END ]]
        do
                CUR=$(date +%s)
                LEFT=$((END-CUR))

                printf "\r%02d:%02d:%02d" \
                        $((LEFT/3600)) $(( (LEFT/60)%60)) $((LEFT%60))

                sleep 1
        done
        IFS="${OLD_IFS}"
        echo "        "
}

if [[ $1 =~ ^-|^$ ]]; then
  fatal "usage: [url] [number of pages to scrape] (optional parameters: -f [basename for output] -o [output folder])"
fi

if [[ $2 =~ ^-|^$ ]]
then
  fatal "not enough parameters"
else 
  main_url=$1
  pages=$2
  shift 2
fi

filebase="dreamwidth"
folder="dreamwidth"

while getopts ":f:o:" opt
do
  case $opt in
    f) filebase="$OPTARG" ;;
    o) folder="$OPTARG" ;;
    *) fatal "Unrecognized parameter -$OPTARG." ;;
  esac
done

if [ ! -d "$folder" ]; then
  mkdir $folder
fi

echo "$filebase-001.html: "
curl -# -o "$folder/$filebase-001.html" "$main_url?view=top-only&page=1#comments"

for ((c=2;c<=$pages;c++))
do
  countdown "00:00:10"
  filename=$(printf "%s/%s-%03d.html" $folder $filebase $c)
  url=$(printf "%s?view=top-only&page=%d#comments" $main_url $c)
  printf "%s-%03d.html: \n" $filebase $c
  curl -# -o $filename $url  
done

echo "done."