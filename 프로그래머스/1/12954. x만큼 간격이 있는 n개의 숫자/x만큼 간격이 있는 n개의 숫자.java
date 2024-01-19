class Solution {
    public long[] solution(int x, int n) {
        long[] answer = new long[n];
        long num = x;
        for(int i=1; i<=n; i++){
            long temp = i*num;
            answer[i-1] = temp;
        }
        
        return answer;
    }
}