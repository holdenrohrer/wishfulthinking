import os

outputnum = 0
def build_makefile(inputdir, outputdir='output', splits=8, makefile='Makefile'):
    '''Expecting a directory full of .zip files, each with a .txt inside
    them'''
    files = [f'./{inputdir}/'+file for file in list(os.listdir(inputdir))]
    chunklen = int(len(files)/splits)
    outputfile = open(makefile, 'w')
    outputfile.write("all: " + ' '.join(f"{outputdir}/{num}" for num in range(splits)) + '\n')

    def requirements(filelist: str) -> str:
        global outputnum
        outputfile.write(f"{outputdir}/{outputnum}: {filelist}\n")
        outputfile.write(f"\tpython3 generate_corpus.py $@ {filelist}\n")
        # we might be able to use $? to improve on "interrupted runs" time
        # if we log out the current calculated frequency on interrupt/error.
        outputnum += 1

    for y in range(splits-1):
        filelist = ' '.join(files[y*chunklen:(y+1)*chunklen])
        requirements(filelist)
    requirements(' '.join(files[(y+1)*chunklen:]))

    outputfile.close()
