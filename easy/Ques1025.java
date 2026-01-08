// 1025. Divisor Game
 
      /*
            alice wins if n is even and loses if n is odd.
            if n %2 == 0:
                return True 
            else:
                return False
        */

// in java
class Solution {
    public boolean divisorGame(int n) {
        return n % 2 == 0;
    }
}

// in python
class Solution:
    def divisorGame(self, n: int) -> bool:
        return n % 2 == 0

      
