/*
Rating: ~ 3.9 / 10
Link: https://open.kattis.com/problems/kastenlauf
*/

import java.io.*;
import java.util.*;

public class kastenlauf {
   public static void main(String[] args) {
      Scanner scan = new Scanner(System.in);
      int cases = Integer.parseInt(scan.nextLine());
      for (int x = 0; x < cases; x++) {
         int stops = Integer.parseInt(scan.nextLine());
         Coordinates[] bars = new Coordinates[stops];
         Coordinates start = new Coordinates(scan.nextInt(), scan.nextInt());
         scan.nextLine();
         for (int y = 0; y < stops; y++) {
            bars[y] = new Coordinates(scan.nextInt(), scan.nextInt());
            scan.nextLine();
         }
         Coordinates end = new Coordinates(scan.nextInt(), scan.nextInt());
         scan.nextLine();
         Stack<Coordinates> track = new Stack<Coordinates>();
         boolean[] visited = new boolean[bars.length];
         track.push(start);
         boolean found = DFS(track, end, bars, visited);
         if (found) {
            System.out.println("happy");
         }
         else {
            System.out.println("sad");
         }
      }
   }

   public static boolean DFS(Stack<Coordinates> track, Coordinates end, Coordinates[] bars, boolean[] visited) {
      Coordinates current = track.pop();
      int distance = Math.abs(current.x-end.x)+Math.abs(current.y-end.y);
      if (distance <= 1000) {
         return true;
      }
      boolean found = false;
      for (int x = 0; x < bars.length; x++) {
         if (visited[x]) {
            continue;
         }
         if (found) {
            break;
         }
         int checkd = Math.abs(current.x-bars[x].x)+Math.abs(current.y-bars[x].y);
         if (checkd <= 1000) {
            track.push(current);
            track.push(bars[x]);
            visited[x] = true;
            found = DFS(track, end, bars, visited);
         }
      }
      return found;
   }
}

class Coordinates {
   int x = -5;
   int y = -5;

   Coordinates(int x, int y) {
      this.x = x;
      this.y = y;
   }
}

