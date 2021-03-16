import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.*;

public class D {
    static void solve() {
        int n = readInt();
        int[] widths = new int[n + 1]; // reading w, h as envelope #0
        int[] heights = new int[n + 1];
        for (int i = 0; i < widths.length; i++) {
            widths[i] = readInt();
            heights[i] = readInt();
        }
        doSolve(n, widths, heights);
    }

    private static void doSolve(int n, int[] widths, int[] heights) {
        int[] to = new int[n + 1]; // next envelope
        Arrays.fill(to, -1);
        int[] dp = new int[n + 1]; // max chain starting from i
        dp(dp, 0, widths, heights, to);
        out.println(--dp[0]);
        for (int i = to[0]; i != -1; i = to[i]) {
            out.print(i);
            out.print(' ');
        }
    }
    
    private static int dp(int[] dp, int k, int[] widths, int[] heights, int[] to) {
        if (dp[k] > 0) {
            return dp[k];
        }
        dp[k] = 1;
        for (int i = 0; i < dp.length; i++) {
            if (widths[i] > widths[k] && heights[i] > heights[k]) { // verify eligible
                if (dp(dp, i, widths, heights, to) + 1 > dp[k]) { // verify makes the chain longer
                    to[k] = i;
                    dp[k] = dp[i] + 1;
                }
            }
        }
        return dp[k];
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
