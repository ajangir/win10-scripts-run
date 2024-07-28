ls -directory | forEach-Object {echo $_.FullName; cp "$_\2_English.srt" "$_.srt" -verbose}
adb shell ls -A sdcard/Download/0fdm/*.zip | ForEach-Object{adb pull "$_"; adb shell rm "$_"}
ls -directory | forEach-Object {echo $_.FullName; $sub=ls $_|sort length -desc|select -first 1;cp $sub "$_.srt" -verbose}; mv *.srt ..
ls *.zip | ForEach-Object{7z x $_}
