#!/bin/sh

DIR=$(cd $(dirname $0); pwd)
cd $DIR

rm -f ./delegated-*

wget ftp://ftp.arin.net/pub/stats/arin/delegated-arin-extended-latest
wget ftp://ftp.ripe.net/pub/stats/ripencc/delegated-ripencc-latest
wget ftp://ftp.apnic.net/pub/stats/apnic/delegated-apnic-latest
wget ftp://ftp.lacnic.net/pub/stats/lacnic/delegated-lacnic-latest
wget ftp://ftp.afrinic.net/pub/stats/afrinic/delegated-afrinic-latest

cat delegated-* | perl ./conv.pl | sort -n | perl ./minimize.pl > ipv4.txt