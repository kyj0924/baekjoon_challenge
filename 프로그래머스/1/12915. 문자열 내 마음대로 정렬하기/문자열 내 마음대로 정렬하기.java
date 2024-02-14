import java.util.*;
class Solution {
    public ArrayList<String> solution(String[] strings, int n) {
        
        String temp = "";
        ArrayList<String> al = new ArrayList<>();
        ArrayList<String> answer = new ArrayList<>();
        for(int i=0; i<strings.length; i++){
            temp = strings[i].charAt(n) + strings[i];
            al.add(temp);
        }
        Collections.sort(al);
        for(int i=0; i<al.size(); i++){
            temp = al.get(i).substring(1);
            answer.add(temp);
        }
        return answer;
    }
}