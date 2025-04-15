import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int tc = sc.nextInt();
		
		for(int i = 0; i<tc; i++) {
			String s = sc.next();
			System.out.print(s.charAt(0));
			System.out.print(s.charAt(s.length()-1) + "\n");
		}
		
	}
}
