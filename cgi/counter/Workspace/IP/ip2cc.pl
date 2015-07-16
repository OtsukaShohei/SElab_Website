#!/usr/bin/perl

use strict;


my $file = 'ipv4.txt';
my $log = "../log.txt";
my $count;
open(my $fh, '<', $log) or die ("Error: $!\n");
while (my $l = <$fh>) {   
    chomp($l);
    my $num;
    $num = ($num << 8) + $_ foreach (split(/\./, $l));
    open(FH, $file);
    while (<FH>) {
	chomp;
	my ($start, $end, $cc) = split(/\t/);
	
	if ($start <= $num && $num < $end) {
	    my($country, $visitor) = split(/\s/);
	    if(-e "$cc.txt"){
		open(COUNT, "+< $cc.txt") or die ("NOT FOUND\n");
		eval{flock(COUNT,2)};
		$count = <COUNT>;
		print $count;
		++$count;
		seek(COUNT,0,0);
		print COUNT "$count\n";
	    }
	    else{
		print "NO!!\n";
		open(CH, ">$cc.txt");
		print CH "1\n";
	    }
	    
	    
	    last;
	}
    }
    close(FH);
}

