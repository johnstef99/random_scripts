#!/bin/bash

inputaudio=$1
list="$2"

timestamps=( $(cut -d' ' -f1 $list) )
length=${#timestamps[@]}

titles=( $(cut -d' ' -f2 $list | cut -d'-' -f1) )
artists=( $(cut -d' ' -f2 $list | cut -d'-' -f2) )

last_song_timestamp=${timestamps[$length-1]}

echo "There are $length timestamps"

folder="$(echo "$inputaudio" | iconv -c -f UTF-8 -t ASCII//TRANSLIT | tr -d '[:punct:]' | tr '[:upper:]' '[:lower:]' | tr ' ' '-' | sed "s/-\+/-/g;s/\(^-\|-\$\)//g")"
! mkdir -p "$folder" && echo "Do you have write access in this directory?" && exit 1

for (( i=0; i<$length-1; i++))
  do
    file="${artists[$i]}-${titles[$i]}.mp3"
    begin=${timestamps[$i]}
    end=${timestamps[$i+1]}
    echo -e "$begin => $end \t TITLE: ${titles[$i]}"
   	ffmpeg -nostdin -y -loglevel -8 -i "$inputaudio" -ss "$begin" -to "$end" -vn -c copy -metadata title="${titles[$i]}" -metadata artist="${artists[$i]}" "$folder/$file"
  done

##exporting last song
file="${artists[$length-1]} - ${titles[$length-1]}"
begin=${timestamps[$length-1]}
end="END"
echo -e "$begin => $end \t TITLE: ${titles[$i]}"
ffmpeg -nostdin -y -loglevel -8 -i "$inputaudio" -ss "$begin" -vn -c copy -metadata title="${titles[$length-1]}" -metadata artist="${artists[$length-1]}" "$folder/$file"
