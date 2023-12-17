use strict;
use warnings;
use Path::Tiny;

my $BASE = Path::Tiny::path("C:/Users/raikoug/SyncThing/shared_code_tests/adventOfCode/2023/");

sub get_day_input {
    my ($day, $test) = @_;
    $test //= 0;
    my $file_name = ($test ? "test_" : "") . "input.txt";
    my $file_path = $BASE->child(sprintf("day_%02d", $day), $file_name);
    return split "\n", $file_path->slurp;
}

sub get_file_path {
    my ($day, $test) = @_;
    $test //= 0;
    my $file_name = ($test ? "test_" : "") . "input.txt";
    my $file_path = $BASE->child(sprintf("day_%02d", $day), $file_name);
    return $file_path;
}