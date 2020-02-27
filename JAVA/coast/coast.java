// Inputs: n, m, n rows of signals
// Outputs: count

import java.util.LinkedList;
import java.util.Scanner;

public class coast {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);

    String[] n_m = in.nextLine().split(" ");
    int n = Integer.parseInt(n_m[0]);
    int m = Integer.parseInt(n_m[1]);

    int[][] map = new int[n + 2][m + 2];
    boolean[][] visited = new boolean[n + 2][m + 2];

    for (int r = 1; r < n + 1; r++) {
      String[] row = in.nextLine().split("");
      for (int c = 1; c < m + 1; c++) {
        map[r][c] = Integer.parseInt(row[c - 1]);
      }
    }

    int count = bfs(map, visited, n, m);
    System.out.println(count);
  }

  public static int bfs(int[][] map, boolean[][] visited, int n, int m) {
    LinkedList<Point> q = new LinkedList<Point>();
    q.add(new Point(0, 0));
    visited[0][0] = true;
    int count = 0;

    while (!q.isEmpty()) {
      Point curr = q.poll();

      if (curr.r - 1 > -1 && !visited[curr.r - 1][curr.c]) {
        if (map[curr.r - 1][curr.c] == 1) {
          count += 1;
        } else {
          q.add(new Point(curr.r - 1, curr.c));
          visited[curr.r - 1][curr.c] = true;
        }
      }
      if (curr.r + 1 < n + 2 && !visited[curr.r + 1][curr.c]) {
        if (map[curr.r + 1][curr.c] == 1) {
          count += 1;
        } else {
          q.add(new Point(curr.r + 1, curr.c));
          visited[curr.r + 1][curr.c] = true;
        }
      }
      if (curr.c - 1 > -1 && !visited[curr.r][curr.c - 1]) {
        if (map[curr.r][curr.c - 1] == 1) {
          count += 1;
        } else {
          q.add(new Point(curr.r, curr.c - 1));
          visited[curr.r][curr.c - 1] = true;
        }
      }
      if (curr.c + 1 < m + 2 && !visited[curr.r][curr.c + 1]) {
        if (map[curr.r][curr.c + 1] == 1) {
          count += 1;
        } else {
          q.add(new Point(curr.r, curr.c + 1));
          visited[curr.r][curr.c + 1] = true;
        }
      }
    }

    return count;
  }

  static class Point {
    int r = 0;
    int c = 0;

    Point(int r, int c) {
      this.r = r;
      this.c = c;
    }
  }
}
