# 8. Sa se scrie un script care primeste urmatoarele argumente:
# path, tree_depth, filesize , filecount, dircount
# si care creeaza o structura de directoare de adancime depth astfel:
#       incepand din radacina path vor fi create dircount directoare
#       si filecount fisiere cu continut de filesize octeti (doar caracterul "a" de exemplu")
#       iar acest proces va fi repetat recursiv pentru fiecare director creat pana cand se obtine
#       adancimea dorita (in directoarele aflate la adacimea maxima nu se vor crea alte directoare)
#
# De exemplu, daca rulam scriptul astfel:
#   python3 create_dummy_tree.py test 2 1024 3 3 va fi creat in directorul curent urmatoarea structura:
#     test
#     test/dir0
#     test/dir0/file1 (size 1024)
#     test/dir0/file2 (size 1024)
#     test/dir0/file3 (size 1024)
#     test/dir1
#     test/dir1/file1 (size 1024)
#     test/dir1/file2 (size 1024)
#     test/dir1/file3 (size 1024)
#     test/dir2
#     test/dir2/file1 (size 1024)
#     test/dir2/file2 (size 1024)
#     test/dir2/file3 (size 1024)
#     test/file0 (size 1024)
#     test/file1 (size 1024)
#     test/file2 (size 1024)

