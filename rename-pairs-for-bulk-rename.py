'''
format for renaming
old files name as old_name.srt
and to_be_named only without extension
'''


def takeInput():
    arr = []
    while True:
        try:
            s = input()
            arr.append(s)
        except:
            break
    return arr

def makeOutputFormat(arr):
    offset = len(arr)//2
    for i in range(len(arr)//2):
        mkv_name,subtitle_name = arr[i].strip(), arr[i+offset].strip()
        subtitle_ext = subtitle_name[-3:]
        new_subtitle_name = mkv_name + '.' + subtitle_ext
        print(f"{subtitle_name} | {new_subtitle_name}")

def takeInputFile():
    file_name = 'in.txt'
    with open(file_name,'r') as f:
        arr = f.readlines()
    return arr

arr = takeInputFile()
makeOutputFormat(arr)