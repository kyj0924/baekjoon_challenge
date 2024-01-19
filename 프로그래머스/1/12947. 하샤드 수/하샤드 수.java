class Solution {
    public boolean solution(int x) {
        boolean answer = true;
        int sum = 0;
        String x_str = Integer.toString(x);
        String[] x_arr = x_str.split("");
        for(int i=0; i<x_arr.length; i++){
            sum += Integer.parseInt(x_arr[i]);
        }
        if(x%sum==0){
            answer = true;
        }
        else{
            answer = false;
        }
        return answer;
    }
}