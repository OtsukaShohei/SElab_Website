#!/usr/bin/perl

my $file = "ipv4.txt";
my $log = "log.txt";
my $count;
my $jp;
my $us;
my $ru;

print qq(Content-type: text/html\n\n); 
print qq(<html>\n);
print qq(<body>\n);
print qq(<center>\n);


open(my $fh, '<', $log) or die ("Error: $!\n");

if(-e "./JP.txt"){
	open(DELFILE,">JP.txt");
    unlink("JP.txt");
}
if(-e "./US.txt"){
	open(DELFILE,">US.txt");
    unlink("US.txt");
}
if(-e "./RU.txt"){
	open(DELFILE,">RU.txt");
    unlink("RU.txt");
}
if(-e "./DK.txt"){
	open(DELFILE,">DK.txt");
    unlink("DK.txt");
}
if(-e "./IN.txt"){
	open(DELFILE,">IN.txt");
    unlink("IN.txt");
}


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
				++$count;
				seek(COUNT,0,0);
				print COUNT "$count\n";
				close(COUNT);
	    	}
	    	else{
				open(NEW, ">>$cc.txt");
				print NEW "1\n";
				close(NEW);
	 		}
	    
	    	last;
		}
    }
    close(FH);
}

open(JP, "+< JP.txt");
open(US, "+< US.txt");
open(RU, "+< RU.txt");
open(DK, "+< DK.txt");
open(IN, "+< IN.txt");

$jp = <JP>;
$us = <US>;
$ru = <RU>;
$dk = <DK>;
$in = <IN>;

print qq(<figure>\n);
print qq(<img src="img/JP.png" height="52" width="80" alt="" border="2">\n);
print "$jp &nbsp;";
print qq(<img src="img/US.png" height="52" width="80" alt="" border="2">\n);
print "$us &nbsp;";
print qq(<img src="img/RU.png" height="52" width="80" alt="" border="2">\n);
print "$ru";
print qq(<img src="img/DK.png" height="52" width="80" alt="" border="2">\n);
print "$dk &nbsp;";
print qq(<img src="img/IN.png" height="52" width="80" alt="" border="2">\n);
print "$in &nbsp;";
print qq(<figcaption>\n);



print qq(</figcaption>\n);
print qq(</figure>\n);

print qq(</center>\n);
print qq(</body>\n);
print qq(</html>\n);

close(JP);
close(US);
close(RU);
close(DK);
close(IN);
