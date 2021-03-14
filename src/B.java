import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;

public class B {
    static void solve() {
        int t = readInt();
        while (t-- > 0) {
            int n = readInt();
            int[] cream = new int[n];
            for (int i = 0; i < n; i++) {
                cream[i] = readInt();
            }
            doSolve(n, cream);
        }
    }

    private static void doSolve(int n, int[] cream) {
        for (int i = n - 2; i >= 0; i--) {
            cream[i] = Math.max(cream[i], cream[i + 1] - 1);
        }
        for (int i = 0; i < n; i++) {
            if (i > 0) {
                out.print(' ');
            }
            out.print(cream[i] > 0 ? 1 : 0);
        }
        out.println();
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
