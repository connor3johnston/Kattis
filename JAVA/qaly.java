import java.io.*;

public class qaly {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int cases = Integer.parseInt(br.readLine());
    double sum = 0;
    for (int x = 0; x < cases; x++) {
      String[] line = br.readLine().split(" ");
      sum += (Double.parseDouble(line[0])*Double.parseDouble(line[1]));
    }
    System.out.println(sum);
  }
}

