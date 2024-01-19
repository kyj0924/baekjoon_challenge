class Solution {
    public long solution(long n) {
        long answer = 0;
        long x = 1;
        int flag = 0;
        while((long)Math.pow(x, 2) <= n){
            if(n == (long)Math.pow(x, 2)){
                answer = (long)Math.pow(x+1, 2);
                flag = 1;
                break;
            }
            x++;
        }
        if(flag == 0){
            answer = -1;
        }

        return answer;
    }
}