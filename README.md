go_zamiatanie
=============

Zadanie na projekt z przedmiotu Geometria Obliczeniowa. 
Program pozwala na zdefiniowanie dowolnej liczby odcinków w przestrzeni 2D, a następnie wyszukiwanie ich przecięć.

Whole app is written in python. It's using numpy and matplotlib libraries.
To use this app, siply run _main.py_ file.

####Program usage:
- save_stretches - save to file
- load_stretches - load from file
- set_generator_area <x1> <x2> <y1> <y2> - set area for stretches generator
- generate_stretches <n> - generate n stretches
- add_stretch <x1> <y1> <x2> <y2> - add stretch between 2 points
- clean - cleans list of stretches
- print_stretches - prints stretches
- is_crossing - check if at least one crossing occurs
- find_crossings - find all crossing in given stretches set
