import java.util.*;

class GfG {

   
    static ArrayList<Integer> bfs(
        ArrayList<ArrayList<Integer>> adj) {
        int V = adj.size();
        
        int s = 0; 

        ArrayList<Integer> res = new ArrayList<>();
        
       
        Queue<Integer> q = new LinkedList<>();

        boolean[] visited = new boolean[V];
        
        
        visited[s] = true;
        q.add(s);
        
  
        while (!q.isEmpty()) {
            
            res.add(curr);
           
            for (int x : adj.get(curr)) {
                if (!visited[x]) {
                    visited[x] = true;
                    q.add(x);
                }
            }
        }
        return res;
    }
    
    public static void main(String[] args) {
        
     
       
        ArrayList<ArrayList<Integer>> adj = new ArrayList<>();
        adj.add(new ArrayList<>(Arrays.asList(1, 2)));
        adj.add(new ArrayList<>(Arrays.asList(0, 2, 3)));       
        adj.add(new ArrayList<>(Arrays.asList(0, 4)));       
        adj.add(new ArrayList<>(Arrays.asList(1,4)));          
        adj.add(new ArrayList<>(Arrays.asList(2,3)));          
        
        
        ArrayList<Integer> ans = bfs(adj);
        for (int i : ans) {
            System.out.print(i + " ");
        }
    }
}