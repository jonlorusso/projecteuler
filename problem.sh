#!/bin/sh

padded=$(seq -f "%05g" $1 $1)
file="problem${padded}.$2"

open https://projecteuler.net/problem=$1

touch $file
git add $file
vim $file
