import java.util.*;

public class Solution {
    public ArrayList<Integer> solution(int []arr) {
        int[] answer = {};
        ArrayList<Integer> al = new ArrayList<>();
        Queue<Integer> queue = new LinkedList<>();
        for(int i=0; i<arr.length; i++){
            queue.add(arr[i]);
        }
        int temp = -1;
        int dequeued = 0;
        while(!queue.isEmpty()){
            dequeued = queue.remove();
            if(temp==dequeued){
                
            }
            else{
                al.add(dequeued);
                temp = dequeued;
            }
        }
        

        return al;
    }
}