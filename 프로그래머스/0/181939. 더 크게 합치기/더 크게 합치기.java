class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        String ab = Integer.toString(a) + Integer.toString(b);
        String ba = Integer.toString(b) + Integer.toString(a);
        int ab_num = Integer.parseInt(ab);
        int ba_num = Integer.parseInt(ba);
        if(ab_num>=ba_num){
            answer = ab_num;
        }
        else{
            answer = ba_num;
        }
        return answer;
    }
}