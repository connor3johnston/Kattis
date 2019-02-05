import java.util.*;

public class Apaxiaaaaaaaaaaaans {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		String name = scan.nextLine();
		String out = "";
		for (int x = 1; x < name.length(); x++) {
			if (name.charAt(x - 1) != name.charAt(x)) {
				out += name.charAt(x-1);
			}
		}
		out += name.charAt(name.length() - 1);
		System.out.println(out);
	}
}