'''
format for renaming
old files name as old_name.srt
and to_be_named only without extension
'''

arr = []
while True:
    try:
        s = input()
        arr.append(s)
    except:
        break
offset = len(arr)//2
for i in range(len(arr)//2):
    print(f"{arr[i]} | {arr[i+offset]}.srt")
