class Solution {
    public int[] solution(int n, int k) {
        String temp = "";
        int count = 0;
        for(int i=1; i<=n; i++){
            if(i%k==0){
                temp += i+" ";
                count++;
            }
        }
        int[] answer = new int[count];
        System.out.println(temp);
        for(int i=0; i<answer.length; i++){
            String[] arr = temp.split(" ");
            answer[i] = Integer.parseInt(arr[i]);
        }
        
        return answer;
    }
}