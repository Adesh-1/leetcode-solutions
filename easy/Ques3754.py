# 3754. Concatenate Non-Zero Digits and Multiply by Sum I
# in python

# 1st method -> simple and easy to read
class Solution:
    def sumAndMultiply(self, n: int) -> int:
        # Convert the integer to a list of its digit characters
        s = list(str(n))
        
        # Remove all '0' characters from the list
        ln = list(filter(lambda x: x != "0", s))
        
        # Convert remaining characters to integers
        m = list(map(int, ln))
        
        # If list is empty (means n had only zeros), return 0
        if not m:
            return 0
        
        # Join the digits to form a new integer
        a = int("".join(str(i) for i in m))
        
        # Return (sum of digits) * (number formed by digits)
        return sum(m) * a

# 2nd method -> tricky
class Solution:
    def sumAndMultiply(self, n: int) -> int:
        # Convert number to digits and remove all '0' digits
        list_no = [int(i) for i in str(n) if i != "0"]

        # If all digits were zero, return 0 (to avoid int("") error)
        if not list_no:
            return 0

        # Form a new integer by joining the remaining digits
        digit = int("".join(str(i) for i in list_no))

        # Return: (sum of digits) * (the formed integer)
        return sum(list_no) * digit
