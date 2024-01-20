class Solution {
    public String solution(String s, int n) {
        String answer = "";
        char[] c_arr = s.toCharArray();
        char temp_c = 0;
        for(char c : c_arr){
            if(c==32){
                answer += " ";
            }
            else{
                if(c<=90){
                    c+=n;
                    if(c>90){
                        c-=26;
                    }
                }
                else{
                    c+=n;
                    if(c>122){
                        c-=26;
                    }
                }
                answer+=c;
            }
        }
        return answer;
    }
}