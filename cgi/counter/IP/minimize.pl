#!/usr/bin/perl

use strict;

my ($flag, $START, $END, $CC);

$flag = 0;
while (<STDIN>) {
    chomp;
    my ($start, $end, $cc) = split(/\t/);

    if ($cc ne $CC || $start != $END) {
        if ($flag != 0) { print $START . "\t" . $END . "\t" . $CC . "\n"; }
        else { $flag = 1; }
        $START = $start;
    }

    $END = $end;
    $CC = $cc;
}
print $START . "\t" . $END . "\t" . $CC . "\n";
