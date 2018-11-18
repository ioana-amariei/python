# 1. Create a module that contains a function named "sort_uuids".
#   This function reads the file sample.txt ( download ),
# 	and sorts the lines base on the string that is between the first and second dash ("-").
# 	Ex: 00e43761-e18a-40c6-b252-3407aa1d8e45 => is sorted by "e18a".
# 	There might be situations where the code might raise Exception. Catch them all !
# 	Create a new file, named "results.txt".
# 	Write in this file the sorted uuids.
#
# 	A universally unique identifier (UUID) is a 128-bit number used to identify information in computer systems.
# 	In its canonical textual representation, the sixteen octets of a UUID are represented as 32 hexadecimal (base 16)
#   digits, displayed in five groups separated by hyphens, in the form 8-4-4-4-12 for a total of 36 characters
# 	(32 alphanumeric characters and four hyphens). (wiki)
import traceback


def sort_uuids():
    read_fd = open('sample.txt', 'r')
    try:
        uuids = read_fd.readlines()
        uuids.sort(key=lambda uuid: uuid.split('-')[1])

        write_fd = open('results.txt', 'w+')
        write_fd.writelines(uuids)
        write_fd.close()

    except Exception as e:
        print(e)
        traceback.print_exc()
    finally:
        read_fd.close()


sort_uuids()
