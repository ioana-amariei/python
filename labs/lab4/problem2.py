# 2. Using the same file from Problem 1 (sample.txt), modify the line that does not respect the uuid format
#  (if there is any).
# 	This modification means to replace the bad line with this message "|INVALID_UUID|".
# 	You may use the file cursor to make the changes (seek or tell)
import re


def replace_invalid_format_line():
    f = open("updated.txt", "r")
    line_regex = re.compile("[a-zA-Z0-9]{8}-([a-zA-Z0-9]{4}-){3}[a-zA-Z0-9]{12}")

    updated_lines = []

    for line in f:
        if line_regex.match(line):
            updated_lines.append(line)
        else:
            updated_lines.append("|INVALID_UUID|\n")

    f.close()

    f = open("updated.txt", "w")
    for line in updated_lines:
        f.write(line)
    f.close()


replace_invalid_format_line()
