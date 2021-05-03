import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class F {
    static void solve() {
        int t = readInt();
        while (t-- > 0) {
            int n = readInt();
            int c = readInt();
            int[] a = new int[n];
            for (int i = 0; i < n; i++) {
                a[i] = readInt();
            }
            int[] b = new int[n - 1];
            for (int i = 0; i < n - 1; i++) {
                b[i] = readInt();
            }
            doSolve(n, c, a, b);
        }
    }

    private static void doSolve(int n, int c, int[] a, int[] b) {
        long days = Integer.MAX_VALUE;
        long[] positionDays = new long[n];
        long[] positionMoney = new long[n];
        for (int pos = 0; pos < n; pos++) {
            long daysToGetRemainingMoney = (long) Math.ceil((double) (c - positionMoney[pos]) / a[pos]);
            days = Math.min(days, positionDays[pos] + daysToGetRemainingMoney); // days needed for current position
            if (pos < n - 1) {
                long daysToGetMoneyForPromotion = (long) Math.ceil((double) (b[pos] - positionMoney[pos]) / a[pos]);
                positionDays[pos + 1] = positionDays[pos] + daysToGetMoneyForPromotion + 1;
                positionMoney[pos + 1] = (positionDays[pos + 1] - positionDays[pos] - 1)*a[pos] - b[pos] + positionMoney[pos];
            }
        }
        out.println(days);
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
