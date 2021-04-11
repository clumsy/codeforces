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
            int[] a = new int[n];
            for (int i = 0; i < n; i++) {
                a[i] = readInt();
            }
            doSolve(n, a);
        }
    }

    private static void doSolve(int n, int[] a) {
        int first = -1;
        int second = -1;
        for (int i = 0; i < n; i++) {
            if (first >= 0 && second >= 0) {
                out.println(a[i] == a[first] ? second + 1 : first + 1);
                return;
            }
            if (first < 0) {
                first = i;
            } else if (a[first] != a[i]) {
                second = i;
            }
        }
        out.println(n);
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
