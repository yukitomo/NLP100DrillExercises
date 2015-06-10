#!/bin/sh
echo "$ bash test2.sh"
expand -t 1 address.txt
echo "other command : tr '\t' " " < address.txt"
