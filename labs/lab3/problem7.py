# 7. Fie un dictionar global definit asemanator cu cel de mai sus,
#  cu deosebirea ca functiile date ca valori ale dictionarului pot primi orice combinatie de parametri.
#  Sa se scrie o functie apply_function care primeste ca parametru numele unei operatii
# 	si aplica functia corespunzatoare peste argumentele primite.
# 	Sa se implementeze astfel incat, in cazul adaugarii unei functii noi,
#   sa nu fie necesara modificarea functiei apply_function.
#
# 	Un exemplu de dictionar global ar putea fi urmatorul:
# 			{
#
# 				"print_all": lambda *a, **k: print(a, k),
#
# 				"print_args_commas": lambda *a, **k: print(a, k, sep=", "),
#
# 				"print_only_args": lambda *a, **k: print(a),
#
# 				"print_only_kwargs": lambda *a, **k: print(k)
#
# 			}


global_dictionary = {"print_all": lambda *a, **k: print(a, k),
                     "print_args_commas": lambda *a, **k: print(a, k, sep=", "),
                     "print_only_args": lambda *a, **k: print(a),
                     "print_only_kwargs": lambda *a, **k: print(k)
                     }


def apply_function(operation_name, *a, **k):
    operation = global_dictionary[operation_name]
    return operation(a, k)


apply_function("print_all", "a", 1, 5, ["1", "2", "3"], 4)
apply_function("print_args_commas", "a", 1, 5, ["1", "2", "3"], 4)
