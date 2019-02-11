/*
Rating: ~ 1.2 / 10
Link: https://open.kattis.com/problems/lastfactorialdigit
*/

import java.io.*;
import java.util.*;

public class lastfactorialdigit {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    int cases = Integer.parseInt(scan.nextLine());
    for (int x = 0; x < cases; x++) {
      int num = Integer.parseInt(scan.nextLine());
      int factorial = 1;
      while (num > 1) {
        factorial *= num;
        num--;
      }
      String stringform = Integer.toString(factorial);
      System.out.println(stringform.charAt(stringform.length()-1));
    }
  }
}
