import java.util.*;
class Solution {
    public ArrayList solution(int n, int m) {
        ArrayList n_al = new ArrayList();
        ArrayList m_al = new ArrayList();
        ArrayList answer_al = new ArrayList();
        if(n<m){
            if(m%n==0){
                answer_al.add(n);
                answer_al.add(m);
            }
            else{
                for(int i=n; i>=1; i--){
                    if(m%i==0 && n%i==0){
                        answer_al.add(i);
                        break;
                    }
                }
                int x = 2;
                while(true){
                    long num = (long)m*x;
                    if((num)%n==0){
                        answer_al.add(num);
                        break;
                    }
                    x++;
                }
                
            }
        }
        else if(n==m){
            answer_al.add(n);
            answer_al.add(m);
        }
        else{
            if(n%m==0){
                answer_al.add(m);
                answer_al.add(n);
            }
            else{
                for(int i=m; i>=1; i--){
                    if(n%i==0 && m%i==0){
                        answer_al.add(i);
                        break;
                    }
                }
                int y = 2;
                
                while(true){
                    long num = (long)n*y;
                    if((num)%m==0){
                        answer_al.add(num);
                        break;
                    }
                    y++;
                }
            }
            
        }
        
    
        return answer_al;
    }
}