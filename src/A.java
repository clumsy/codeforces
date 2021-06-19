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
            doSolve(a);
        }
    }

    private static void doSolve(int[] a) {
        int min_i = 0;
        int max_i = 0;
        int n = a.length;
        for (int i = 1; i < n; i++) {
            if (a[i] > a[max_i]) {
                max_i = i;
            } else if (a[i] < a[min_i]) {
                min_i = i;
            }
        }
        int from_left = Math.max(min_i + 1, max_i + 1);
        int from_right = Math.max(n - min_i, n - max_i);
        int from_both = Math.min(min_i + 1 + (n - max_i), max_i + 1 + (n - min_i));
        out.println(Math.min(Math.min(from_left, from_right), from_both));
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

    static int gcd(int a, int b) {
        while (b > 0) {
            a %= b;
            b = swap(a, a = b);
        }
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
