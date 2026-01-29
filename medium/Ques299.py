# 299. Bulls and Cows
# in python
class Solution:
    def getHint(self, secret: str, guess: str) -> str:

        # This loop will take care of "bull" cases
        bull = 0
        for i in range(len(secret)):
            bull += int(secret[i] == guess[i])

        # This loop will take care of "cow" cases
        cows = 0
        for c in set(secret):
            cows += min(secret.count(c), guess.count(c))

        return f"{bull}A{cows-bull}B"

# in java
class Solution {
    public String getHint(String secret, String guess) {
        int cows = 0;
        int bulls = 0;
        int[] count = new int[10];
        for (int i = 0; i < secret.length(); i++) {
            int s = secret.charAt(i) - '0';
            int g = guess.charAt(i) - '0';
            if (s == g) {
                bulls++;
            } else {
                if (count[s] < 0)
                    cows++;
                if (count[g] > 0)
                    cows++;
                count[s]++;
                count[g]--;
            }
        }
        return bulls + "A" + cows + "B";
    }
}
