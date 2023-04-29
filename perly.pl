sub escape_single_quotes
{
	my $string = $_[0];
	$string =~ s/'/''/g;
	return $string;
}
