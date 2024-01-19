import java.util.*;
class Solution {
    public int[] solution(int[] arr, int divisor) {
        ArrayList array = new ArrayList();
        int count = 0;
        for(int i=0; i<arr.length; i++){
            if(arr[i]%divisor==0){
                array.add(arr[i]);
                count++;
            }
        }
        if(count==0){
            count++;
        }
        int[] answer = new int[count];
        if(array.size()==0){
            answer[0]=-1;            
        }
        else{
            for(int i=0; i<array.size(); i++){
                answer[i] = (int)array.get(i);
            }
        }
        Arrays.sort(answer);
        return answer;
    }
}