import java.util.*;
class Solution {
    public ArrayList<Integer> solution(String[] name, int[] yearning, String[][] photo) {
        
        int score = 0;
        HashMap<String, Integer> hm = new HashMap<>();
        ArrayList<Integer> answer = new ArrayList<>();
        
        for(int i=0; i<name.length; i++){
            hm.put(name[i], yearning[i]);
        }
        
        for(int i=0; i<photo.length; i++){
            score = 0;
            for(int j=0; j<photo[i].length; j++){
                
                if(hm.get(photo[i][j])==null){
                    continue;
                }
                else{
                    score += hm.get(photo[i][j]);
                }
            }
            answer.add(score);
        }
        return answer;
    }
}