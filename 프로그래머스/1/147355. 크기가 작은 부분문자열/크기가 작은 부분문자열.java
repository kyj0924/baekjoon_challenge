class Solution {
    public int solution(String t, String p) {
        
        int t_len = t.length();
        int p_len = p.length();
        long temp_t = 0;
        int count=0;
        long int_p = Long.parseLong(p);
        for(int i=0; i<=t_len-p_len; i++){
            temp_t = Long.parseLong(t.substring(i, i+p_len));
            if(temp_t<=int_p){
                count++;
                
            }
        }
        return count;
    }
}