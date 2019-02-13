/*
Rating: ~ 1.7 / 10
Link: https://open.kattis.com/problems/karte
*/

import java.io.*;
import java.util.*;

public class karte {
   public static void main(String[] args) {
      Scanner scan = new Scanner(System.in);
      int nope = 0;
      HashSet p = new HashSet();
      HashSet k = new HashSet();
      HashSet h = new HashSet();
      HashSet t = new HashSet();

      String[] line = scan.nextLine().split("");
      for (int x = 0; x < line.length; x+=3) {
         String card = line[x] + line[x+1] + line[x+2];
         if (card.charAt(0) == 'P') {
            if (p.contains(card)) {
               nope = 1;
               break;
            }
            else {
               p.add(card);
            }
         }
         if (card.charAt(0) == 'K') {
            if (k.contains(card)) {
               nope = 1;
               break;
            }
            else {
               k.add(card);
            }
         }
         if (card.charAt(0) == 'H') {
            if (h.contains(card)) {
               nope = 1;
               break;
            }
            else {
               h.add(card);
            }
         }
         if (card.charAt(0) == 'T') {
            if (t.contains(card)) {
               nope = 1;
               break;
            }
            else {
               t.add(card);
            }
         }
      }
      if (nope == 1) {
         System.out.println("GRESKA");
      }
      else {
         System.out.print(13 - p.size() + " ");
         System.out.print(13 - k.size() + " ");
         System.out.print(13 - h.size() + " ");
         System.out.print(13 - t.size() + " ");
      }
   }
}
