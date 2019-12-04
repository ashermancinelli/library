#! /usr/bin/env sh

if [ -f data/religion.csv ]
then
    mv data/religion.csv tmp.csv
    sed 's/Robert Leaney,/Robert Leaney;/' tmp.csv > data/religion.csv
    rm tmp.csv
else
    echo Religion csv not found...
fi

if [ ! -f data/cs.csv ]; then
    echo CS csv not found...
fi
