class Solution {
    public int solution(int a, int b) {
        String ab = Integer.toString(a) + Integer.toString(b);
        int ab_num = Integer.parseInt(ab);
        int answer = Math.max(ab_num, 2*a*b);
        
        return answer;
    }
}