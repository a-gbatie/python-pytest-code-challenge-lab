from lib.palindrome import longest_palindromic_substring

def test_single_character(): # Defines the test
  result = longest_palindromic_substring("a") # Calls the function, passing 'a' variable
  assert result == "a" # Checks whether the result matches what we expect
  
def test_even_length_palindrome():
  result = longest_palindromic_substring("cbbd")
  assert result == "bb"
  
def test_odd_length_palindrome():
  assert longest_palindromic_substring("racecar") == "racecar" # shorthand for what the previous tests are doing - result and assert in one line
  
def test_multiple_longest_palindrome():
  result = longest_palindromic_substring("babad")
  assert result in ("bab", "aba")

def test_entire_string_is_palindrome():
  assert longest_palindromic_substring("madam") == "madam"
  
def test_no_repeated_characters():
  result = longest_palindromic_substring("abc")
  assert result in ("a", "b", "c")

def test_empty_string():
  assert longest_palindromic_substring("") == ""
  
def test_two_identical_characters():
  assert longest_palindromic_substring("aa") == "aa"
  
def test_two_different_characters():
  result = longest_palindromic_substring("ab")
  assert result in ("a", "b")
  
def test_palindrome_in_a_string():
  assert longest_palindromic_substring("xyzracecarcba") == "racecar"
  
def test_case_sensitivity():
  result = longest_palindromic_substring("Aa")
  assert result in ("A", "a")
  
def test_repeated_characters():
  assert longest_palindromic_substring("aaaa") == "aaaa"