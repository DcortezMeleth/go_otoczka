go_otoczka
==========

Zadanie na projekt z przedmiotu Geometria Obliczeniowa. 
Program pozwala na zdefiniowanie punków w przestrzeni 2D na jeden z wybranych sposobów, a następnie wyszukiwanie punktów tworzących otoczkę naszego zboru. Do wyszukiwania punktów otoczki mamy do wyboru dwa algorytmy: **Grahama** i **Jarvisa**.

Cała aplikacja została napisana w języku python. Wykorzystuje ona biblioteki numpy oraz graphics.
Aby uruchomić aplikację należy odpalić plik _main.py_.

####Program usage:
- save_points - save to file
- load_points - load from file
- save_result - save to file
- set_n <n> <square_n=25> <diagonal_n=20> - set number of points to generate
- set_range <min> <max> - set params for range generation
- set_circle <center.x> <center.y> <r> - set params for circle generation
- set_quadrilateral <x1.x> <x1.y> <x2.x> <x2.y> <x3.x> <x3.y> <x4.x> <x4.y>  - set params for quadrilateral generation
- set_square <x1.x> <x1.y> <x3.x> <x3.y> - set params for square generation
- generate <figure> - generate points (0 - range, 1 - circle, 2 - quadrilateral, 3 - square)
- solve <algorithm> - solve problem using chosen algorithm(0 - Graham, 1 - Jarvis)
- draw_points - draw generated points set
- draw_result - draws result sequentially, drawing stretches one by one
- print_points - print generated points
- print_result - prints points in result list
- print_help - print program usage
