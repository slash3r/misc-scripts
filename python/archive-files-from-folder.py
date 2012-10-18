'''
    The code is pretty much self explanatory.
    This script walks a given folder, or the 'pics' folder in the current
    working directory, and archives all it's file in zip files of at most the
    given size, or 0.5 GB.
'''

import os
import zipfile

def archive(name, flist):
    print "Creating the zip file: " + name
    zf = zipfile.ZipFile(name, mode='w')

    for (fname, fsize) in flist:
        print "\tadding: " + fname + "[" + fsize + "]"
        zf.write(fname)

    print "Closing the archive.\n"
    zf.close()

def start_processing(target_dir='pics', max_arch_size=524288000):
    curr_dir = os.getcwd()
    os.chdir(target_dir)

    for (root, _, filenames) in os.walk(os.getcwd()):
        curr_size = 0
        prev_size = 0
        total_size = 0

        flist = []

        index = 0

        for filename in filenames:
            # generate the file information
            filepath = root + '\\' + filename
            filesize = os.path.getsize(filepath)

            # add the file to the current list
            flist.append((filename, filesize))

            # calculate the current size indicators
            total_size = total_size + filesize
            curr_size = curr_size + filesize

            # test to see if the quota has been exceeded
            if prev_size < max_arch_size and curr_size >= max_arch_size:
                # create archive
                arch_name = curr_dir + '\\' + 'arch_{0:03d}.zip'.format(index)
                archive(arch_name, flist)

                # reset the values
                flist = []
                curr_size = 0

                # advance the index
                index = index + 1

        # all done, pack the remaining files
        if curr_size != 0:
            arch_name = curr_dir + '\\' + 'arch_{0:03d}.zip'.format(index)
            archive(arch_name, flist)

if __name__ == "__main__":
    start_processing()
