import java.util.*;
class Solution {
    public ArrayList<Integer> solution(int[] numbers) {
        int[] answer = {};
        HashSet<Integer> s = new HashSet<Integer>();
        int first_num = 0;
        int sum = 0;
        for(int i=0; i<numbers.length; i++){
            if(i!=0){
                numbers[i-1] = first_num;
            }
            first_num = numbers[i];
            numbers[i] = -1;
            for(int j=0; j<numbers.length; j++){
                sum = 0;
                if(numbers[j]==-1){
                    continue;
                }
                else{
                    sum = first_num + numbers[j];
                    s.add(sum);
                }
            }
        }
        ArrayList<Integer> al = new ArrayList<>(s);
        Collections.sort(al);
        System.out.println(al);
        
        return al;
    }
}