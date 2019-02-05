import java.util.*;

public class Candies {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int cases = Integer.parseInt(scan.nextLine());
		scan.nextLine();
		for (int x = 0; x < cases; x++) {
			int kids = Integer.parseInt(scan.nextLine());
			double total = 0;
			for (int y = 0; y < kids; y++) {
				total += Double.parseDouble(scan.nextLine());
			}
			if (total%kids == 0) {
				System.out.println("YES");
			}
			else {
				System.out.println("NO");
			}
			if (scan.hasNextLine()) {
				scan.nextLine();
			}
		}
	}
}