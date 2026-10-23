def longest_palindromic_substring(s):
  """
  Given a string s, return the longest palindromic substring.
  """
  
  curr_longest = "" # Set current longest palindrome to empty string
  
  for start in range(len(s)): # Loop through the length of the variable
    for end in range(start + 1, len(s) + 1): # Ensures loop starts at index 0 and goes to the end since Python slicing excludes endng index
      substring = s[start:end] # Includes start but excludes end. Outer loop controls starting point, inner loops controls where substring ends, together they check every nonempty substring
      
      if substring == substring[::-1]: # Checks the string is equal forward and in reverse
        if len(substring) > len(curr_longest): # Checks if newly found palindrome is longer than what has been found so far
          curr_longest = substring # If so, replace current palindrome with newly found palindrome
  
  return curr_longest
  