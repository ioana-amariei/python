# 2. Using the same file from Problem 1 (sample.txt), modify the line that does not respect the uuid format
#  (if there is any).
# 	This modification means to replace the bad line with this message "|INVALID_UUID|".
# 	You may use the file cursor to make the changes (seek or tell)


def replace_invalid_format_line():
    read_fd = open("sample.txt", "r")
    write_fd = open("updated.txt", "w+")

    content = read_fd.readlines()
    for line in content:
        if len(line) < 37 or len(line) > 37:
            write_fd.write("|INVALID_UUID|\n")
        else:
            write_fd.write(line)

    write_fd.close()
    read_fd.close()


replace_invalid_format_line()
