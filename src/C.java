import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;

public class C {
    static void solve() {
        int t = readInt();
        while (t-- > 0) {
            int n = readInt();
            doSolve(n);
        }
    }

    private static void doSolve(int n) {
        if (n == 1) {
            out.println(1);
            return;
        }
        if (n == 2) { // the only -1 scenario
            out.println(-1);
            return;
        }
        int white = 1;
        int black = (n*n + 1)/2 + 1; // the range after all white cells
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (((i + j)&1) == 0) { // even -> white
                    out.print(white++);
                } else {
                    out.print(black++);
                }
                out.print(' ');
            }
            out.println();
        }
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

    static int swap(int a, int b) { // usage: y = swap(x, x=y);
        return a;
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
