from lib.palindrome import longest_palindromic_substring

def test_single_character(): # Defines the test
  result = longest_palindromic_substring("a") # Calls the function, passing 'a' variable
  assert result == "a" # Checks whether the result matches what we expect
  
def test_even_length_palindrome():
  result = longest_palindromic_substring("cbbd")
  assert result == "bb"