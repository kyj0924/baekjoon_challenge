import java.util.*;
class Solution {
    public int[] solution(int[] arr) {
        ArrayList array = new ArrayList();
        
        int min = arr[0];
        if(arr.length==1){
            int[] answer = new int[1];
            answer[0] = -1;
            return answer;
        }
        else{
            int[] answer = new int[arr.length-1];
            for(int i=0; i<arr.length; i++){
                array.add(arr[i]);
                if(arr[i]<=min){
                    min = arr[i];
                }
            }
            int idx = array.indexOf(min);
            array.remove(idx);
            for(int i=0; i<array.size(); i++){
                answer[i]=(int)array.get(i);
            }
            return answer;
        }
    }
}