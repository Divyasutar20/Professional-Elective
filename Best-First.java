// Function to perform Best First Search
import java.util.*;

class GfG {

    static ArrayList<Integer> bestFirstSearch(int[][] edges, 
    int src, int target, int n) {
     
        ArrayList<ArrayList<int[]>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adj.add(new ArrayList<>());
        }
        for (int i = 0; i < edges.length; i++) {
            adj.get(edges[i][0]).add(new int[]{edges[i][1], edges[i][2]});
            adj.get(edges[i][1]).add(new int[]{edges[i][0], edges[i][2]});
        }

        boolean[] visited = new boolean[n];
        Arrays.fill(visited, false);
        
      
        PriorityQueue<int[]> pq = new PriorityQueue<>
        (new Comparator<int[]>() {
            public int compare(int[] a, int[] b) {
                return Integer.compare(a[0], b[0]);
            }
        });

        pq.add(new int[]{0, src});
        
      
        visited[src] = true;
  
        ArrayList<Integer> path = new ArrayList<>();
    
        while (!pq.isEmpty()) {
            
            int x = pq.peek()[1];
     
            path.add(x);
           
            pq.poll();
          
            if (x == target)
                break;
    
            for (int i = 0; i < adj.get(x).size(); i++) {
                if (!visited[adj.get(x).get(i)[0]]) {
          
                    visited[adj.get(x).get(i)[0]] = true;
            
                    pq.add(new int[]{adj.get(x).get(i)[1], 
                    adj.get(x).get(i)[0]});
                }
            }
        }
        
        return path;
    }
    
    public static void main(String[] args) {
        int n = 14;
        int[][] edgeList = {
            {0, 1, 3}, {0, 2, 6}, {0, 3, 5},
            {1, 4, 9}, {1, 5, 8}, {2, 6, 12},
            {2, 7, 14}, {3, 8, 7}, {8, 9, 5},
            {8, 10, 6}, {9, 11, 1}, {9, 12, 10},
            {9, 13, 2}
        };
        
        int source = 0;
        int target = 9;
        
        ArrayList<Integer> path = 
        bestFirstSearch(edgeList, source, target, n);
        
        for (int i = 0; i < path.size(); i++) {
            System.out.print(path.get(i) + " ");
        }
    }
}