One thing that I found was weird was that pop from stack worked and the original stack was modified. But the push to stack function sent back None like I thought it would. In test_is_twelve_digit it said that 12 was a digit because it is just checking if the string is in the list of digits, so 123456789 would return true also. In comparePrecedence it does not fail when you pass it something random like ** or anything because it is assuming that you are just sending it an operator. 
