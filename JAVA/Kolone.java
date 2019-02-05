import java.util.*;

public class Kolone {
   public static void main(String[] args) {
      Scanner scan = new Scanner(System.in);
      int row1 = scan.nextInt();
      int row2 = scan.nextInt();
      String ants1 = scan.next();
      String ants2 = scan.next();
      int secs = scan.nextInt();
      char[] both = new char[row1+row2];
      int index = row1-1;
      for (int a = 0; a < ants1.length(); a++) {
         both[index] = ants1.charAt(a);
         index--;
      }
      index = row1;
      for (int b = 0; b < ants2.length(); b++) {
         both[index] = ants2.charAt(b);
         index++;
      }
      if (secs > Math.min(row1, row2)) {
	System.out.print(ants2);
	for (int x = row1-1; x > -1; x--) {
		System.out.print(ants1.charAt(x));
	}
	System.out.println();
	return;
      }
      int count = 0;
      int move = secs;
      char[] both2 = new char[row1+row2];
      while (count < secs) {
         char left = both[row1-1-count];
         char right = both[row1+count];
         if (row1+count-move < 0) {
            int in = 0;
            while (both2[in] == '\0') {
               in++;
            }
            both2[in] = right;
         }
         if (row1-1-count-move >= both2.length) {
            int in = both2.length;
            while (both2[in] == '\0') {
               in--;
            }
            both2[in] = left;
         }
         both2[row1-1-count+move] = left;
         both2[row1+count-move] = right;
         count++;
         move--;
      }	
      for (int x = 0; x < both2.length; x++) {
         if (both2[x] == '\0') {
            both2[x] = both[x];
         
         }
      }
      for (char here: both2) {
         System.out.print(here);
      }
      System.out.println();
   }
}
