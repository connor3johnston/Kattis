import java.util.*;

public class Classy {
   public static void main(String[] args) {
      Scanner scan = new Scanner(System.in);
      int cases = Integer.parseInt(scan.nextLine());
      for (int x = 0; x < cases; x++) {
         int people = Integer.parseInt(scan.nextLine());
         HashMap<String, String[]> upper = new HashMap<String, String[]>();
         HashMap<String, String[]> middle = new HashMap<String, String[]>();
         HashMap<String, String[]> lower = new HashMap<String, String[]>();
         ArrayList<String> order = new ArrayList<String>();
         for (int y = 0; y < people; y++) {
            String[] line = scan.nextLine().split(" ");
            String[] ranks = line[1].split("-");
            String last = ranks[ranks.length-1];
            String name = line[0];
            if (last.equals("upper")) {
               upper.put(name, ranks);
            }
            else if (last.equals("middle")) {
               middle.put(name, ranks);
            }
            else if (last.equals("lower")) {
               lower.put(name, ranks);
            }
         }
      	
         while (!upper.isEmpty()) {
            String[] values = upper.keySet().toArray(new String[upper.size()]);
            String highest = values[0];
            String second = "";
            for (int z = 1; z < values.length; z++) {
               String[] one = upper.get(highest);
               String[] two = upper.get(values[z]);
               int comp = 0;
               int index1 = one.length-1;
               int index2 = two.length-1;
               do {
                  String comp1 = "";
                  String comp2 = "";
                  if (index1 < 0 && index2 > -1) {
                     comp1 = "middle";
                     comp2 = two[index2];
                     comp = compare(comp1, comp2);
                     break;
                  }
                  else if (index2 < 0 && index1 > -1) {
                     comp2 = "middle";
                     comp1 = one[index1];
                     comp = compare(comp1, comp2);
                     break;
                  }
                  else if (index1 < 0 && index2 < 0) {
                     break;
                  }
                  comp1 = one[index1];
                  comp2 = two[index2];
                  comp = compare(comp1, comp2);
                  index1--;
                  index2--;
               } while (comp == 0);
               if (comp == -1) {
                  highest = values[z]; 
               }
               else if (comp == 0) {
                  String temp = "";
                  if (highest.length() < values[z].length()) {
                     temp = highest;
                     highest = values[z];
                     second = temp;
                  }
                  else {
                     second = values[z];
                  }
                  int track = -1;
                  for (int p = 0; p < second.length(); p++) {
                     if (second.charAt(p) < highest.charAt(p)) {
                        track = 1;
                        break;
                     }
                     else if (second.charAt(p) > highest.charAt(p)) {
                        track = 0;
                        break;
                     }
                  }
                  String temp2 = "";
                  if (track == 1) {
                     temp2 = highest;
                     highest = second;
                     second = temp2;
                  }
               }
            }	
            order.add(highest);
            upper.remove(highest);
            if (!second.equals("")) {
               order.add(second);
               upper.remove(second);
            }
         }	
         while (!middle.isEmpty()) {
            String[] values = middle.keySet().toArray(new String[middle.size()]);
            String highest = values[0];
            String second = "";
            for (int z = 1; z < values.length; z++) {
               String[] one = middle.get(highest);
               String[] two = middle.get(values[z]);
               int comp = 0;
               int index1 = one.length-1;
               int index2 = two.length-1;
               do {
                  String comp1 = "";
                  String comp2 = "";
                  if (index1 < 0 && index2 > -1) {
                     comp1 = "middle";
                     comp2 = two[index2];
                     comp = compare(comp1, comp2);
                     break;
                  }
                  else if (index2 < 0 && index1 > -1) {
                     comp2 = "middle";
                     comp1 = one[index1];
                     comp = compare(comp1, comp2);
                     break;
                  }
                  else if (index1 < 0 && index2 < 0) {
                     break;
                  }
                  comp1 = one[index1];
                  comp2 = two[index2];
                  comp = compare(comp1, comp2);
                  index1--;
                  index2--;
               } while (comp == 0);
               if (comp == -1) {
                  highest = values[z]; 
               }
               else if (comp == 0) {
                  String temp = "";
                  if (highest.length() < values[z].length()) {
                     temp = highest;
                     highest = values[z];
                     second = temp;
                  	
                  }
                  else {
                     second = values[z];
                  }
                  int track = -1;
                  for (int p = 0; p < second.length(); p++) {
                     if (second.charAt(p) < highest.charAt(p)) {
                        track = 1;
                     }
                     else if (second.charAt(p) > highest.charAt(p)) {
                        track = 0;
                     }
                  }
                  String temp2 = "";
                  if (track == 1) {
                     temp2 = highest;
                     highest = second;
                     second = temp2;
                  }
               }
            }	
            order.add(highest);
            middle.remove(highest);
            if (!second.equals("")) {
               order.add(second);
               middle.remove(second);
            }
         }	
         while (!lower.isEmpty()) {
            String[] values = lower.keySet().toArray(new String[lower.size()]);
            String highest = values[0];
            String second = "";
            for (int z = 1; z < values.length; z++) {
               String[] one = lower.get(highest);
               String[] two = lower.get(values[z]);
               int comp = 0;
               int index1 = one.length-1;
               int index2 = two.length-1;
               do {
                  String comp1 = "";
                  String comp2 = "";
                  if (index1 < 0 && index2 > -1) {
                     comp1 = "middle";
                     comp2 = two[index2];
                     comp = compare(comp1, comp2);
                     break;
                  }
                  else if (index2 < 0 && index1 > -1) {
                     comp2 = "middle";
                     comp1 = one[index1];
                     comp = compare(comp1, comp2);
                     break;
                  }
                  else if (index2 < 0 && index1 < 0) {
                     break;
                  }
                  else if (index1 < 0 && index2 < 0) {
                     break;
                  }
                  comp1 = one[index1];
                  comp2 = two[index2];
                  comp = compare(comp1, comp2);
                  index1--;
                  index2--;
               } while (comp == 0);
               if (comp == -1) {
                  highest = values[z]; 
               }
               else if (comp == 0) {
                  String temp = "";
                  if (highest.length() < values[z].length()) {
                     temp = highest;
                     highest = values[z];
                     second = temp;
                  	
                  }
                  else {
                     second = values[z];
                  }
                  int track = -1;
                  for (int p = 0; p < second.length(); p++) {
                     if (second.charAt(p) < highest.charAt(p)) {
                        track = 1;
                     }
                     else if (second.charAt(p) > highest.charAt(p)) {
                        track = 0;
                     }
                  }
                  String temp2 = "";
                  if (track == 1) {
                     temp2 = highest;
                     highest = second;
                     second = temp2;
                  }
               }
            }	
            order.add(highest);
            lower.remove(highest);
            if (!second.equals("")) {
               order.add(second);
               lower.remove(second);
            }
         }
         for (String here: order) {
            System.out.println(here.substring(0, here.length()-1));
         }
         System.out.println("==============================");
      }
   }
	
   public static int compare(String ths, String here) {
      if (ths.equals(here)) {
         return 0;
      }
      if (ths.equals("upper")) {
         return 1;
      }
      if (ths.equals("lower")) {
         return -1;
      }
      if (here.equals("lower")) {
         return 1;
      }
      if (here.equals("upper")) {
         return -1;
      }
      return -5;
   }
}
