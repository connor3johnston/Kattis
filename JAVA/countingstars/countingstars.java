/*
Rating: ~ 3.0 / 10
Link: https://open.kattis.com/problems/countingstars
*/

import java.io.*;
import java.util.*;

public class countingstars {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    int num  = 1;
    while (scan.hasNextLine()) {
      String[] line2 = scan.nextLine().split(" ");
      int row = Integer.parseInt(line2[0]);
      int col = Integer.parseInt(line2[1]);
      char[] sky = new char[row*col];
      int[] ids = new int[row*col];
      for (int r = 0; r < row; r++) {
        String line = scan.nextLine();
        for (int c = 0; c < col; c++) {
          sky[r*col+c] = line.charAt(c);
          ids[r*col+c] = r*col+c;
        }
      }
      for (int r = 0; r < row; r++) {
        for (int c = 0; c < col; c++) {
          if (sky[r*col+c] == '-') {
            neighbors(sky,ids, r, c, row, col);
          }
        }
      }
      HashSet<Integer> count = new HashSet<Integer>();
      for (int r = 0; r < sky.length; r++) {
        if (sky[r] == '-') {
          count.add(find(ids, ids[r]));
        }
      }
      System.out.println("Case " + num + ": " + count.size());
      num++;
    }
  }
  public static void neighbors(char[] sky, int[] ids, int r, int c, int row, int col) {
    int cur = r*col+c;
    if (r-1 > -1 && sky[(r-1)*col+c] == '-') {
      union(ids, cur, (r-1)*col+c);
    }
    if (r+1 < row && sky[(r+1)*col+c] == '-') {
      union(ids, cur, (r+1)*col+c);
    }
    if (c+1 < col && sky[r*col+(c+1)] == '-') {
      union(ids, cur, r*col+(c+1));
    }
    if (c-1 > -1 && sky[r*col+(c-1)] == '-') {
      union(ids, cur, r*col+(c-1));
    }
  }

  public static void union(int[] ids, int cur, int next) {
    int par1 = find(ids, cur);
    int par2 = find(ids, next);
    ids[par2] = par1;
  }

  public static int find(int[] ids, int here) {
    if (ids[here] == here) {
      return here;
    }
    ids[here] = find(ids, ids[here]);
    return ids[here];
  }
}

