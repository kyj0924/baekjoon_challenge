class Solution {
    public int solution(int n) {
        int answer = 0;
        String n_str = "";
        int n_temp = n;
        int n_namuzy = 0;
        while(n_temp!=0){
            n_namuzy = n_temp%3;
            n_str+=n_namuzy;
            n_temp /= 3;
        }
        String[] n_arr = n_str.split("");
        
        int tenJin = 0;
        int temp = 0;
        for(int i=n_arr.length-1; i>=0; i--){
            temp = Integer.parseInt(n_arr[n_arr.length-1-i]);
            tenJin+=(Math.pow(3, i)*temp);
        }
        
        return tenJin;
    }
}