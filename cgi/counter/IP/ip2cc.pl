#!/usr/bin/perl

use strict;

my ($file, $addr);

$file = 'ipv4.txt';
$addr = $ARGV[0];

if ($addr !~ /^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$/) {
    print "Usage: perl $0 <addr>\n";
    exit;
}

my $num;
$num = ($num << 8) + $_ foreach (split(/\./, $addr));

open(FH, $file);
while (<FH>) {
    chomp;
    my ($start, $end, $cc) = split(/\t/);

    if ($start <= $num && $num < $end) {
        print $cc . "\n";
        last;
    }
}
close(FH);