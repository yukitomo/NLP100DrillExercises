#!/bin/sh
#bash test10.sh
cut -f 2 address.txt|sort | uniq -c | sort -k 1 -r > test10_2.result
