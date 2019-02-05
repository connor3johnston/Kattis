/*
Rating: ~ 1.8 / 10
Link: https://open.kattis.com/problems/anewalphabet
*/

import java.io.*;
import java.util.*;
import java.lang.*;

public class anewalphabet {
   public static void main(String[] args) {
      HashMap<Character, String> dic = new HashMap<Character, String>(26);
      dic.put('a', "@");
      dic.put('b', "8");
      dic.put('c', "(");
      dic.put('d', "|)");
      dic.put('e', "3");
      dic.put('f', "#");
      dic.put('g', "6");
      dic.put('h', "[-]");
      dic.put('i', "|");
      dic.put('j', "_|");
      dic.put('k', "|<");
      dic.put('l', "1");
      dic.put('m', "[]\\/[]");
      dic.put('n', "[]\\[]");
      dic.put('o', "0");
      dic.put('p', "|D");
      dic.put('q', "(,)");
      dic.put('r', "|Z");
      dic.put('s', "$");
      dic.put('t', "']['");
      dic.put('u', "|_|");
      dic.put('v', "\\/");
      dic.put('w', "\\/\\/");
      dic.put('x', "}{");
      dic.put('y', "`/");
      dic.put('z', "2");

      Scanner scan = new Scanner(System.in);
      String line = scan.nextLine();
      for (int x = 0; x < line.length(); x++) {
         if (dic.containsKey(Character.toLowerCase(line.charAt(x)))) {
		 System.out.print(dic.get(Character.toLowerCase(line.charAt(x))));
         }
         else {
		 System.out.print(line.charAt(x));
         }
      }
      System.out.println();
   }
}
