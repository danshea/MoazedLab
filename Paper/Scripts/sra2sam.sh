#!/bin/bash
export PATH=/usr/local/sratoolkit.2.3.5-2-centos_linux64/bin:$PATH
if [[ $# != 1 ]]; then
    echo "usage $0 sra_accession"
else
    if [[ ! -a ${1}.sra ]]; then
        echo "$1 does not exist."
        exit 1
    fi
    inputfile="$1"
    outputfile="${1}.sam.bz2"
    outputdir="/usr/local/galaxy-dist/MoazedLabData/Processed"
    sam-dump -r --bzip2 --output-file ${outputdir}/${outputfile} ${inputfile}
fi
exit 0
