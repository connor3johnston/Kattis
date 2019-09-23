/*
Rating: ~ 1.7 / 10
Link: https://open.kattis.com/problems/kitten
*/

import java.util.*;

public class kitten {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);

    int curr = Integer.parseInt(scan.nextLine());
    int[] branches = new int[101];

    String line = scan.nextLine();
    while (!line.equals("-1")) {
      String[] connections = line.split(" ");
      int lower = Integer.parseInt(connections[0]);

      for (int x = 1; x < connections.length; x++) {
        branches[Integer.parseInt(connections[x])] = lower;
      }

      line = scan.nextLine();
    }

    String path = String.format("%s ", curr);
    while (branches[curr] != 0) {
      curr = branches[curr];
      path += String.format("%s ", curr);
    }

    System.out.println(path.trim());
  }
}
