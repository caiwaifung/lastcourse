FLAGS=-DFEATURE_DIM=$(DIM)

all: a

a: RTree.h a.cpp comm.h
	g++ a.cpp -o a $(FLAGS) -Wall -Wconversion -Wextra --std=c++11

clean:
	rm a
