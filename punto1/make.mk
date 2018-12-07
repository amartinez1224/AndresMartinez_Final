archivo0.pdf : archivo0.dat 
	python3 leer.py
    
archivo0.dat : gen  
	./gen
    
gen : gencadenas.c 
	gcc -fopenmp gencadenas.c -o gen -lm