import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        String answer = "";
        for(int i=0; i<a.length(); i++){
            char temp = a.charAt(i);
            if(Character.isUpperCase(temp)){
                answer += Character.toLowerCase(temp);
            }
            else{
                answer += Character.toUpperCase(temp);
            }
        }
        System.out.println(answer);
    }
}