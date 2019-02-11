/*
Rating: ~ 3.5 / 10
Link: https://open.kattis.com/problems/averagespeed
*/

import java.util.*;
import java.text.DecimalFormat;

public class averagespeed {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		String[] line;
		DecimalFormat df = new DecimalFormat("##0.00");
		double distanceT = 0;
		int timeSLast = 0;
		int speed = 0;
		while (scan.hasNextLine()) {
			line = scan.nextLine().split(" ");
			String[] time = line[0].split(":");
			int timeSCurrent = Integer.parseInt(time[0]) * 3600 + Integer.parseInt(time[1]) * 60 + Integer.parseInt(time[2]);
			double addDistance = 0;
			if (line.length == 2) {
				addDistance = speed * (timeSCurrent - timeSLast)/3600.0;
				distanceT += addDistance;
				timeSLast = timeSCurrent;
				speed = Integer.parseInt(line[1]);

			}
			else  {
				addDistance = speed * (timeSCurrent - timeSLast)/3600.0;
				distanceT += addDistance;
				System.out.println(line[0] + " " + df.format(distanceT) + " " + "km");
				timeSLast = timeSCurrent;

			}
		}
	}
}
