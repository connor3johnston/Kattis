import java.util.Scanner;

public class Stocks {
   public static void main(String[] args) {
      Scanner scan = new Scanner(System.in);
      int days = scan.nextInt();
      long[] values = new long[days];
      long[] check = new long[days + 1];
      for (int x = 0; x < days; x++) {
         values[x] = scan.nextLong();
      }
      int p = 1;
      int index = 0;
      while (p < days) { 
         while (p < days && values[p-1] >= values[p]) {
            p++;
         }
         if (p < days) {
            check[index] = values[p-1];
            index++;
         }
         while (p < days && values[p-1] <= values[p]) {
            p++;
         }
         if (p < days) {
            check[index] = values[p-1];
            index++;
         }
      }
      check[index++] = values[p-1];
      long money = 100;
      long shares = 0;
      if (check[0] > check[1]) {
         int h = 1;
         while (check[h] != 0) {
            if (check[h+1] == 0) {
               if (check[h-1] > check[h]) {
                  money += shares * check[h-1];
                  shares = 0;
                  break;
               }
            }
            if (h%2 == 1) {
               if (shares == 100000) {
                  h++;
                  continue;
               }
               else if (shares + money/check[h] > 100000) {
                  shares += 100000;
                  money -= shares * check[h];
               }
               else {
                  shares += money/check[h];
                  money -= shares * check[h];
               }
               h++;
            }
            else {
               money += shares * check[h];
               shares = 0;
               h++;
            }
         }
      }
      else {
         int h = 0;
         while (check[h] != 0) {
            if (check[h+1] == 0) {
               if (check[h-1] > check[h]) {
                  money += shares * check[h-1];
                  shares = 0;
                  break;
               }
            }
            if (h%2 == 0) {
               if (shares == 100000) {
                  h++;
                  continue;
               }
               else if (shares + money/check[h] > 100000) {
                  shares += 100000;
                  money -= shares * check[h];
               }
               else {
                  shares += money/check[h];
                  money -= shares * check[h];
               }
               h++;
            }
            else {
               money += shares * check[h];
               shares = 0;
               h++;
            }
         }
      }
      System.out.println(money);
   }
}