import java.util.*;

public class ICPC {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int m = scan.nextInt();
		int n = scan.nextInt();
		int t = scan.nextInt();
		
		double calc = 0;	
		switch(t) {
			case 1:
				calc = 1;
				for (int x = n; x > 1; x--) {
					calc *= x;
					if (calc > m) {
						break;
					}
				}	
				break;		
			case 2:
				calc = Math.pow(2, n);
				break;		
			case 3:
				calc = Math.pow(n, 4);
				break;		
			case 4:
				calc = Math.pow(n, 3);
				break;		
			case 5:
				calc = Math.pow(n, 2);
				break;		
			case 6:
				calc = n * (Math.log(n)/Math.log(2));
				break;		
			case 7:
				calc = n;
				break;		

		}
		if (calc > m) {
			System.out.println("TLE");
		}
		else {
			System.out.println("AC");
		}
	}
}
