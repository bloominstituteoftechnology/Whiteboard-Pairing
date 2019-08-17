func count(votes: [String]) -> String? {
	var counts = [String : Int]()
	
	// Iterate over entire array
	for vote in votes {
		// Increment the number of votes for the name
		counts[vote, default: 0] += 1
	}
	
	var maxVotes = 0
	var winner = ""
	for (name, numVotes) in counts {
		// Check to see if current name has more votes then the current max
		if numVotes > maxVotes {
			// Since this name has more votes, its currently the winner
			winner = name
			// Sets the max votes to the current names votes if larger
			maxVotes = numVotes
			
			// Checks to see if current name is tied with the winner
		} else if numVotes == maxVotes {
			// if tied, sets the winner to the name that is greater (last alphabetically)
			if name > winner { winner = name }
		}
	}
	return winner
}

/*
This solution uses doesn't use a for loop or any mutation in place. The closure passed
to sorted() could be reduced to a single line except that the compiler chokes on 
type-checking it.
*/
func count2(votes: [String]) -> String? {
	return Dictionary(votes.map { ($0, 1) }, uniquingKeysWith: +)
	.sorted {
		if $0.value == $1.value { return $0.key > $1.key }
		return $0.value > $1.value
	}.first?.key
}

print(
	count(votes: [
		"veronica",
		"mary",
		"alex",
		"james",
		"mary",
		"michael",
		"alex",
		"michael",
	])!
) // should print "michael"

print(
	count(votes: [
		"john",
		"johnny",
		"jackie",
		"johnny",
		"john",
		"jackie",
		"jamie",
		"jamie",
		"john",
		"johnny",
		"jamie",
		"johnny",
		"john",
	])!
) // should print "johnny"