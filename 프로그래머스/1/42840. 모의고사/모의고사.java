import java.util.*;
class Solution {
    public ArrayList<Integer> solution(int[] answers) {
        ArrayList<Integer> result = new ArrayList<>();
        int[] num1 = {1, 2, 3, 4, 5};
        int[] num2 = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] num3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        int num1_count = 0;
        int num2_count = 0;
        int num3_count = 0;
        for(int i=0; i<answers.length; i++){
            if(answers[i] == num1[i%5]){
                num1_count++;
            }
            if(answers[i] == num2[i%8]){
                num2_count++;
            }
            if(answers[i] == num3[i%10]){
                num3_count++;
            }
        }
        
        int max = 0;
        max = (num1_count >= num2_count) ? num1_count : num2_count;
        max = (max >= num3_count) ? max : num3_count;
        if(max == num1_count){
            result.add(1);
        }
        if(max == num2_count){
            result.add(2);
        }
        if(max == num3_count){
            result.add(3);
        }
        
        return result;
    }
}