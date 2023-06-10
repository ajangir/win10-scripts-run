for i in *.mp3; do ffmpeg-normalize "$i" -c:a mp3 -v -ext mp3;done
for i in *.mp3; do ffmpeg -i "$i" -filter:a "volume=4" out/"$i";done
