#!/bin/bash

x=$(ls dsa/lab1/ | grep '.c*' | wc -l)
shopt -s nullglob
array=(dsa/lab1/*)
rm success failure

for (( i = 0; i < x; i++ )); do
	gcc -w ${array[i]} -o a
	./a < my_in > out1
	flag=$(diff out1 my_out)
	flag=$?
	if [[ $flag -eq 0 ]]; then
		echo ${array[i]} >> success
	else
		printf "output is different for ${array[i]}\n\n"
		echo ${array[i]} >> failure
	fi
done