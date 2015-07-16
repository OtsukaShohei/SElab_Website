#!/usr/bin/perl

use strict;

while (<STDIN>) {
    chomp;
    my ($registry, $cc, $type, $start, $value, undef, $status) = split(/\|/);

    next unless ($type eq 'ipv4' && ($status eq 'allocated' || $status eq 'assigned'));

    my $num;
    $num = ($num << 8) + $_ foreach (split(/\./, $start));

    print $num . "\t" . ($num + $value) . "\t" . $cc . "\n";
}