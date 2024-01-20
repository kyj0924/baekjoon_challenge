import java.util.*;
class Solution {
    public int solution(int[] d, int budget) {
        Arrays.sort(d);
        int temp = 0;
        int index = 0;
        int count = 0;
        while(index<d.length){
            if(temp+d[index]<=budget){
                temp+=d[index];
                index++;
                count++;
            }
            else{
                break;
            }
        }
        
        return count;
    }
}