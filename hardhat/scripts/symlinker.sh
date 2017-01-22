#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "usage: symlinker.sh source_dir target_dir"
fi

SRC=$1
TARGET=$2

SRC=$( readlink -m $SRC )
TARGET=$( readlink -m $TARGET )

echo "symlinking $SRC to $TARGET recursively"


IFS=$'\n'
mkdir -p $SRC
cd $SRC
FILES=( $( find -L . -type f -name "*" ) )

for file in "${FILES[@]}"
do
	src=$( readlink -m $file )
	target=$TARGET/$file
	target=$( readlink -m $target)
	target_dir=$( dirname $target )
	mkdir -p $target_dir
    if [ ! -e $target ]; then
	    ln -s $src $target
    fi
done




