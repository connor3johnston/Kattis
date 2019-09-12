/*
Rating: ~ 1.4 / 10
Link: https://open.kattis.com/problems/nodup
*/

import java.io.*;
import java.util.*;

public class nodup {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);

    String[] phrase = scan.nextLine().split(" ");
    HashSet<String> filter = new HashSet<String>(Arrays.asList(phrase));

    if (filter.size() < phrase.length) {
      System.out.println("no");
    } else {
      System.out.println("yes");
    }
  }
}
