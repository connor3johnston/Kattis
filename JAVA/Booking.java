import java.util.*;

public class Booking {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int rooms = scan.nextInt();
		int booked = scan.nextInt();
		HashSet<Integer> un = new HashSet<Integer>();
		for (int x = 0; x < booked; x++) {
			un.add(scan.nextInt());
		}
		int save = 0;
		for (int x = 1; x <= rooms; x++) {
			if (!un.contains(x)) {
				save = x;
				break;
			}
		}
		if (save == 0) {
			System.out.println("too late");
		}
		else {
			System.out.println(save);
		}
	}
}	
