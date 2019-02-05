import java.util.Scanner;

public class Alphabet {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		String[] line = scan.nextLine().split("");
		char letter = 'a';
		int until = 0;
		int count = 26;
		while (until < line.length) {
			if (line[until].charAt(0) == letter) {
				count--;
				letter++;
			}
			until++;
		}
		System.out.println(count);
	}
}