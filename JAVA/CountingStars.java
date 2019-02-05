import java.util.*;

public class CountingStars {
	public static void main (String[] args) {
		Scanner scan = new Scanner(System.in);
		while (scan.hasNextLine()) {
			int lines = scan.nextInt();
			int stars = scan.nextInt();
			scan.nextLine();
			char[][] sky = new char[lines][stars];
			for (int x = 0; x < lines; x++) {
				String[] line = scan.nextLine().split("");
				for (int y = 0; y < stars; y++) {
					sky[x][y] = line[y].charAt(0);
				}	
			}
			for (int x = 0; x < lines; x++) {
				for (int y = 0; y < stars; y++) {
					char here = sky[x][y];
					if (here == '#') {
						continue;
					}
					neighbors(sky, x, y);
				}	
			}


		}
	}

	public static void union() {

	}

	public static void find() {

	}

	public static void neighbors(char[][] sky, int x, int y) {
		int count = 0;
		while (count < 4) {
			int tempX = x;
			int tempY = y;
			//left
			if (count == 0) {
				tempY--;
				if (tempY > -1) {
					union(sky, x, y, -1, tempY);
				}	
			}
			//right
			else if (count == 1) {
				tempY++;
				tempY--;
				if (tempY < ) {
					union(sky, x, y, -1, tempY);
				}	
			}
			//up
			else if (count == 2) {
				tempX--;
			}
			//down
			else {
				tempX++;
			}
			count++;
		}
	}
}
