public class RomanToInteger {
    public int romanToInt(String s) {
        int[] value = new int[128];
        value['I'] = 1;
        value['V'] = 5;
        value['X'] = 10;
        value['L'] = 50;
        value['C'] = 100;
        value['D'] = 500;
        value['M'] = 1000;

        int total = 0;
        for (int i = 0; i < s.length(); i++) {
            int curr = value[s.charAt(i)];
            int next = (i + 1 < s.length()) ? value[s.charAt(i + 1)] : 0;

            if (curr < next) {
                total -= curr;
            } else {
                total += curr;
            }
        }
        return total;
    }
}
