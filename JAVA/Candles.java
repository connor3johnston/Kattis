import java.util.*;

public class Candles {
   public static void main(String[] args) {
      Scanner scan = new Scanner(System.in);
      int dif = scan.nextInt();
      int rita = scan.nextInt();
      int theo = scan.nextInt();
      int track = 0;
      int ageRita = 4;
      while (track <= rita) {
         if (track + ageRita > rita) {
            break;
         }
         track += ageRita;
         ageRita++;
      }
      int leftover = rita - track;
      rita -= leftover;
      theo += leftover;
      track = 0;
      int ageTheo = 3;
      while (ageTheo <= theo) {
         if (track + ageTheo > theo) {
            break;
         }
         track += ageTheo;
         ageTheo++;
      }
      int leftover2 = theo - track;
      while (ageRita - ageTheo != dif) {
         leftover += ageRita;
         leftover2 += ageRita;
         ageRita--;
         ageTheo++;
      }
      System.out.println(leftover);
   }
}
