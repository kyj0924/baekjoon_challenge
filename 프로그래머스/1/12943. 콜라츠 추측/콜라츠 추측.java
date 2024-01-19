class Solution {
    public int solution(int num) {
        long temp = num;
        int count = 0;
        int answer = 0;
        if(num == 1){
            return 0;
        }
        while(temp!=1){
            if(temp%2==0){
                temp = temp/2;
                count++;
            }
            else{
                temp = temp*3+1;
                count++;
            }
            if(count==500 && temp!=1){
                answer = -1;
                break;
            }
        }
        
        if(answer != -1){
            answer = count;
        }
        return answer;
    }
}