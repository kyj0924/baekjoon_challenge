class Solution {
    public int[] solution(int start_num, int end_num) {
        String temp = "";
        for(int i=start_num; i<=end_num; i++){
            temp += i+" ";
        }
        String[] temp_arr = temp.split(" ");
        int[] answer = new int[temp_arr.length];
        for(int i=0; i<temp_arr.length; i++){
            answer[i] = Integer.parseInt(temp_arr[i]);
        }
        
        return answer;
    }
}