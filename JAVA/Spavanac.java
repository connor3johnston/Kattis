import java.util.*;

public class Spavanac {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		String[] line = scan.nextLine().split(" ");
		int hours = Integer.parseInt(line[0]);
		int minutes = Integer.parseInt(line[1]);

		if (minutes > 45) {
			minutes -= 45;
			System.out.println(hours + " " + minutes);
		}
		else {
			if (hours == 0) {
				hours = 23;
			}
			else {
				hours--;
			}
			minutes+= 15;
			System.out.println(hours + " " + minutes);
		}
	}
}