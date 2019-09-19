/*
Rating: ~ 3.1 / 10
Link: https://open.kattis.com/problems/grid
*/

import java.util.*;

public class grid {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    int moves = -1;

    String[] line = scan.nextLine().split(" ");
    int r = Integer.parseInt(line[0]);
    int c = Integer.parseInt(line[1]);
    int[][] grid = new int[r][c];

    for (int x = 0; x < r; x++) {
      String nums = scan.nextLine();
      for (int y = 0; y < c; y++) {
        grid[x][y] = nums.charAt(y) - '0';
      }
    }

    boolean[][] visited = new boolean[r][c];
    visited[0][0] = true;
    Queue<int[]> queue = new LinkedList<int[]>();
    queue.add(new int[]{0, 0, 0});

    while (!queue.isEmpty()) {
      int[] curr = queue.poll();
      int row = curr[0];
      int col = curr[1];

      if (row == r - 1 && col == c - 1) {
        moves = curr[2];
        break;
      }

      int jump = grid[row][col];

      if (row - jump >= 0 && !visited[row - jump][col]) {
        queue.add(new int[]{row - jump, col, curr[2] + 1});
        visited[row - jump][col] = true;
      }
      if (row + jump < r && !visited[row + jump][col]) {
        queue.add(new int[]{row + jump, col, curr[2] + 1});
        visited[row + jump][col] = true;
      }
      if (col - jump >= 0 && !visited[row][col - jump]) {
        queue.add(new int[]{row, col - jump, curr[2] + 1});
        visited[row][col - jump] = true;
      }
      if (col + jump < c && !visited[row][col + jump]) {
        queue.add(new int[]{row, col + jump, curr[2] + 1});
        visited[row][col + jump] = true;
      }
    }

    System.out.println(moves);
  }
}
