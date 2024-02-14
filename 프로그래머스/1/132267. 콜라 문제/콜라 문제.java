class Solution {
    public int solution(int a, int b, int n) {
        int answer = 0;
        
        while(n-a>=0){
            n -= a;
            answer += b;
            n += b;
        }
        
        return answer;
    }
}