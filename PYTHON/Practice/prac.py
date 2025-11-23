def reverse_string(s: str) -> str:
   """Return the reversed string using slicing.

   Example: reverse_string('abc') -> 'cba'
   """
   return s[::-1]


def reverse_string_manual(s: str) -> str:
   """Return the reversed string using an explicit loop (manual method)."""
   result_chars = []
   for ch in s:
      result_chars.insert(0, ch)
   return "".join(result_chars)


if __name__ == "__main__":
   import sys

   # Accept string from command-line args or prompt the user
   if len(sys.argv) > 1:
      to_reverse = " ".join(sys.argv[1:])
   else:
      try:
         to_reverse = input("Enter string: ")
      except EOFError:
         to_reverse = ""

   # Print the reversed string (slicing method)
   print(reverse_string(to_reverse))