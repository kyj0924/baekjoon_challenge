class Solution {
    public int[] solution(String s) {
        
        int distance =10001;
        int index=0;
        int[] answer = new int[s.length()];
        String[] s_arr = s.split("");
        for(int i=0; i<s_arr.length; i++){
            if(answer[s.indexOf(s_arr[i])]!=-1){
                index = s.indexOf(s_arr[i]);
                answer[index] = -1;
            }
            else if(answer[i]==0){
                for(int j=i-1; j>=s.indexOf(s_arr[i]); j--){
                    if(s_arr[i].equals(s_arr[j])){
                        distance = i-j;
                        answer[i]=distance;
                        break;
                    }
                }
            }
        }
        
        return answer;
    }
}