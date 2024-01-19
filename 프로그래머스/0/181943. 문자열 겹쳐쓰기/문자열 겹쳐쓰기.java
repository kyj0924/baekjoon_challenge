class Solution {
    public String solution(String my_string, String overwrite_string, int s) {
        String answer = "";
        String front_str = my_string.substring(0, s);
        String rear_str = my_string.substring(s+overwrite_string.length());
        answer = front_str + overwrite_string + rear_str;
        
        return answer;
    }
}