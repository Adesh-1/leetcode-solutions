# 2469. Convert the Temperature
# in python
class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [(celsius + 273.15), (celsius * 1.80 + 32.00)]

# in java
class Solution {
    public double[] convertTemperature(double celsius) {
        return new double[] { (celsius + 273.15), (celsius * 1.80 + 32.00) };
    }
}
