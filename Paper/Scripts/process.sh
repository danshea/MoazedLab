#!/bin/bash
for i in *.sra; do
sra2sam.sh $(echo $i | cut -d. -f1)
done
