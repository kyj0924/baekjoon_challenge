import java.util.*;
class Solution {
    public long solution(long n) {
        String n_str = Long.toString(n);
        String[] arr = n_str.split("");
        Arrays.sort(arr, Collections.reverseOrder());
        String sorted_str = "";
        for(int i=0; i<arr.length; i++){
            sorted_str += arr[i];
        }
        long answer = Long.parseLong(sorted_str);
        return answer;
    }
}