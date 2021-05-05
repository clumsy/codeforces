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
            int k = readInt();
            doSolve(n, k);
        }
    }

    private static void doSolve(int n, int k) {
        if (n < 1 + 2*k) {
            out.println(-1);
            return;
        }
        // construct peak: 1,3,2,5,4,7,6,...
        int i = 1;
        out.print(i++);
        out.print(' ');
        while (k-- > 0) {
            out.print(i + 1);
            out.print(' ');
            out.print(i);
            out.print(' ');
            i += 2;
        }
        // print the rest in increasing order (no peaks)
        while (i <= n) {
            out.print(i++);
            out.print(' ');
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
