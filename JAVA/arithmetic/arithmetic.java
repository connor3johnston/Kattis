/*
Rating: ~ 3.8 / 10
Link: https://open.kattis.com/problems/arithmetic
*/

import java.io.*;
import java.util.*;

public class arithmetic {
  public static void main(String[] args) {
      Scanner scan = new Scanner(System.in);
      String octal = scan.nextLine();
      while (octal.length() % 4 != 0) {
         octal = "0" + octal;
      }
      String output = "";
      String octSub = octal.substring(0, 4);
      long binary = Long.parseLong(octSub, 8);
      String hex = Long.toHexString(binary);
  	System.out.print(hex.toUpperCase());
      for (int x = 4; x < octal.length(); x += 4) {
         octSub = octal.substring(x, x + 4);
         binary = Long.parseLong(octSub, 8);
         hex = Long.toHexString(binary);
         while (hex.length() != 3) {
            hex = "0" + hex;
         }
  	System.out.print(hex.toUpperCase());
      }
	System.out.println();
  }
}
