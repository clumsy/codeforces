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
            int[] a = new int[n];
            for (int i = 0; i < n; i++) {
                a[i] = readInt();
            }
            doSolve(n, a);
        }
    }

    private static void doSolve(int n, int[] a) {
        boolean increasing = true;
        int prev = Integer.MIN_VALUE;
        for (int num : a) {
            if (num < prev) {
                increasing = false;
            }
            prev = num;
        }
        boolean min_first = a[0] == 1;
        boolean max_last = a[n - 1] == n;
        if (min_first && max_last && increasing) {
            out.println(0);
            return;
        }
        boolean max_first = a[0] == n;
        boolean min_last = a[n - 1] == 1;
        if (max_first && min_last) {
            out.println(3);
            return;
        }
        if (min_first || max_last) {
            out.println(1);
            return;
        }
        out.println(2);
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
