class Solution {
    public long solution(int price, int money, int count) {
        long cost = 0;
        for(int i=1; i<=count; i++){
            cost += (long)price*i;
        }
        if(money-cost<0){
            return cost-money;
        }
        else{
            return 0;
        }
    }
}