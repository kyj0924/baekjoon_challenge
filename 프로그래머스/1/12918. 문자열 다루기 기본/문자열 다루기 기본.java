class Solution {
    public boolean solution(String s) {
        int count = 0;
        if(s.length()==4 || s.length()==6){
            for(int i=0; i<s.length(); i++){
                if(Character.isDigit(s.charAt(i))){
                    count++;
                }
            }
        }
        if(count == s.length()){
            return true;
        }
        else{
            return false;
        }
    }
}