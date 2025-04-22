import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
    public static void solve(BufferedReader br, int tc) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int lastNBit = (1 << (N)) - 1;
        if(lastNBit == (M & lastNBit)){
            System.out.println("#" + tc + " " + "ON");
        }else{
            System.out.println("#" + tc + " " + "OFF");
        }
    } // solve

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for(int tc = 1; tc <= T; ++tc){
            solve(br, tc);
        }
        br.close();
    } // main
} // class
