import os

files = ['./zip/'+file for file in list(os.listdir('zip'))]
splits = 8
chunklen = int(len(files)/splits)
print("all: " + ' '.join(f"output/{num}" for num in range(splits)))

outputnum = 0
def requirements(filelist: str) -> str:
    global outputnum
    print(f"output/{outputnum}: {filelist}")
    print(f"\tpython3 corpus.py $@ $?")
    outputnum += 1

for y in range(splits-1):
    filelist = ' '.join(files[y*chunklen:(y+1)*chunklen])
    requirements(filelist)
requirements(' '.join(files[(y+1)*chunklen:]))
