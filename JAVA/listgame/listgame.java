/*
Rating: ~ 3.0 / 10
Link: https://open.kattis.com/problems/listgame
*/

import java.io.*;
import java.util.*;

public class listgame {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int num = scan.nextInt();
		int count = 0;
		int here = 2;
		while (Math.pow(here, 2) <= num) {
				if (num%here == 0) {
					count++;
					num /= here;
				}
				else {
					here++;
			}
		}
		count++;
		System.out.println(count);
	}
}
