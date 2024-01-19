class Solution {
    public String solution(String s) {
        String answer = "";
        if(s.length()%2==0){
            if(s.length()/2+2 <= s.length()){
                answer = s.substring(s.length()/2-1, s.length()/2+1);    
            }
            else{
                answer = s.substring(s.length()/2-1);
            }   
        }
        else{
            answer = s.substring(s.length()/2, s.length()/2+1);
        }
        return answer;
    }
}