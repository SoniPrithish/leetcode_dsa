class Solution {
    public String getPermutation(int n, int k) {
        int[] fact = new int[n];
    fact[0] = 1;
    for (int i = 1; i < n; i++) {
        fact[i] = fact[i-1] * i;
    }
    
    // Available digits
    List<Integer> digits = new ArrayList<>();
    for (int i = 1; i <= n; i++) {
        digits.add(i);
    }
    
    StringBuilder result = new StringBuilder();
    k--; // Convert to 0-based indexing
    
    for (int i = 0; i < n; i++) {
        int index = k / fact[n-1-i];        // Which digit to pick
        result.append(digits.get(index));   // Add digit
        digits.remove(index);               // Remove used digit
        k = k % fact[n-1-i];               // Update k
    }
    
    return result.toString();
    }}
