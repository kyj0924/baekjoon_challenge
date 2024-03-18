import java.util.*;

class Solution {
    public String[] solution(String[] players, String[] callings) {
        
        HashMap<String, Integer> rankingMap = new HashMap<String, Integer>();
        HashMap<Integer, String> playerMap = new HashMap<Integer, String>();
        
        for(int i=0; i<players.length; i++){
            rankingMap.put(players[i], i);
            playerMap.put(i, players[i]);
        }
        
        for(int i=0; i<callings.length; i++){
            int player_idx = rankingMap.get(callings[i]);
            String player = playerMap.get(player_idx);
            String front_player = playerMap.get(player_idx-1);
            rankingMap.put(front_player, player_idx);
            rankingMap.put(player, player_idx-1);
            playerMap.put(player_idx-1, player);
            playerMap.put(player_idx, front_player);
        }
        
        String[] answer = new String[players.length];
        
        for(int i=0; i<players.length; i++){
            answer[i] = playerMap.get(i);
        }
        
        return answer;
    }
}