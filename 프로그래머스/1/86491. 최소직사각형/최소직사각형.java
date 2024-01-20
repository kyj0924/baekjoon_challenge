import java.util.*;
class Solution {
    public int solution(int[][] sizes) {
        // 가로 길이 최대 > 세로길이 최대 ==> 가로 세로 중 작은 값들 중에서 가장 큰 값이 세로 길이
        // 가로 길이 최대 < 세로길이 최대 ==> 가로 세로 중 작은 값들 중에서 가장 큰 값이 가로 길이
        // 가로 길이 최대 = 세로길이 최대 ==> 둘다 최대여야됨
        int width_max = 0;
        int height_max = 0;
        int temp = 0;
        int result = 0;
        
        for(int i=0; i<sizes.length; i++){
            
            if(width_max<=sizes[i][0]){
                width_max = sizes[i][0];
            }
            if(height_max<=sizes[i][1]){
                height_max = sizes[i][1];
            }
            if(Math.min(sizes[i][0], sizes[i][1])>=temp){
                temp = Math.min(sizes[i][0], sizes[i][1]);
            }
        }
        result = Math.max(width_max, height_max) * temp;
        
        return result;
    }
}