/*
Rating: ~ 1.6 / 10
Link: https://open.kattis.com/problems/sodasurpler
*/

import java.util.*;

public class sodasurpler {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    String[] line = scan.nextLine().split(" ");
    int total = Integer.parseInt(line[0]) + Integer.parseInt(line[1]);
    int count = 0;
    int needed = Integer.parseInt(line[2]);
    while (total >= needed) {
      total = total - needed + 1;
      count++;
    }
    System.out.println(count);
  }
}
