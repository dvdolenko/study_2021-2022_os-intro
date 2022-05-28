#!/bin/bash

gcc l11.c -o l11
./l11
code=$?
case $code in
	0) echo "<0";;
	1) echo ">0";;
	2) echo "=0";;
esac
