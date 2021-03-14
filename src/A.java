import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;

public class A {
    static void solve() {
        int t = readInt();
        while (t-- > 0) {
            int n = readInt();
            int[] arrival = new int[n];
            int[] departure = new int[n];
            for (int i = 0; i < n; i++) {
                arrival[i] = readInt();
                departure[i] = readInt();
            }
            int[] extra = new int[n];
            for (int i = 0; i < n; i++) {
                extra[i] = readInt();
            }
            doSolve(n, arrival, departure, extra);
        }
    }

    private static void doSolve(int n, int[] arrival, int[] departure, int[] extra) {
        int currentTime = arrival[0] + extra[0];
        for (int i = 1; i < n; i++) {
            int waitTimeOnPreviousStation = (departure[i - 1] - arrival[i - 1] + 1) / 2;
            int departureFromPreviousStation = Math.max(currentTime + waitTimeOnPreviousStation, departure[i - 1]);
            int travelTime = arrival[i] - departure[i - 1] + extra[i];
            currentTime = departureFromPreviousStation + travelTime;
        }
        out.println(currentTime);
    }

    //////////////////////// Template ////////////////////////
    static int readInt() {
        return Integer.parseInt(readString());
    }

    static long readLong() {
        return Long.parseLong(readString());
    }

    static String readString() {
        while (tok == null || !tok.hasMoreTokens()) {
            try {
                tok = new StringTokenizer(in.readLine());
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }
        return tok.nextToken();
    }

    static BufferedReader in;
    static PrintWriter out;
    static StringTokenizer tok;

    public static void main(String[] arg) {
        in = new BufferedReader(new InputStreamReader(System.in));
        out = new PrintWriter(System.out);
        solve();
        out.close();
    }
}
