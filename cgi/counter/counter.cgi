#!/usr/bin/perl

$tm = time;
($sec, $min, $hour, $mday, $mon, $year) = localtime($tm);
$year += 1900;
++$mon;


print qq(Content-type: text/html\n\n); 
print qq(<html>\n);
print qq(<body>\n);
print qq(<center>\n);

open(TIME,"+<time.txt");
open(TEST,"+<test.txt");
print TEST "$sec, $min, $hour, $mday, $mon, $year";
$old_time = <TIME>; #最終アクセスの時間
$new_time = $hour * 60 * 60 + $min * 60 + $sec; #最新更新時間
if($new_time <= $old_time){
    seek(TIME,0,0);
    print TIME $hour * 60 * 60 + $min * 60 + $sec;
    open(DELFILE,">ip.txt");
    unlink("ip.txt");
    open(NEWFILE, ">>ip.txt");
    print NEWFILE "1";
    close NEWFILE;
}
else{
    if($new_time - $old_time >= 1200){
        seek(TIME,0,0);
        print TIME $hour * 60 * 60 + $min * 60 + $sec;
        open(DELFILE,">ip.txt");
        unlink("./ip.txt");
        open(NEWFILE, ">>ip.txt");
        print NEWFILE "1";
        close NEWFILE;
    }
}


my $file = "ip.txt";
open(FILE,"+<counter.dat");
eval{flock(FILE,2)};
$count = <FILE>;

open(my $fh, '<', $file) or die ("Error: $!\n");
while (my $l = <$fh>) {
    chomp($l);
    if ($ENV{'REMOTE_ADDR'} eq $l) {
        last;
    }
    if (eof $fh) {
        close($fh);
        open(OUT,">> $file");
        print OUT "\n";
        print OUT $ENV{'REMOTE_ADDR'};
        close(OUT);
        ++$count;
        seek(FILE,0,0);
        print FILE $count;
        close FILE;

    }
}

#log用
my $file = "log.txt";
open(my $fh, '<', $file) or die ("Error: $!\n");
while (my $l = <$fh>) {
    chomp($l);
    if ($ENV{'REMOTE_ADDR'} eq $l) {
        last;
    }
    if (eof $fh) {
        close($fh);
        open(OUT,">> $file");
        print OUT "\n";
        print OUT $ENV{'REMOTE_ADDR'};
        close(OUT);
    }
}

print "You are $count visitor."; 
print qq(</center>\n);
print qq(</body>\n);
print qq(</html>\n);