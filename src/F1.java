import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;

public class F1 {
    static void solve() {
        int n = readInt();
        int t = readInt();
        while (t-- > 0) {
            int k = readInt();
            doSolve(n, k);
        }
    }

    private static void doSolve(int n, int k) {
        int left = 1;
        int right = n;
        while (left < right) {
            int middle = left + (right - left)/2;
            int current_sum = query(left, middle);
            int current_zeroes = (middle - left + 1) - current_sum;
            if (k > current_zeroes) {
                k -= current_zeroes;
                left = middle + 1;
            } else {
                right = middle;
            }
        }
        out.println("! " + left);
        out.flush();
    }
    
    private static int query(int left, int right) {
        out.println("? " + left + " " + right);
        out.flush();
        int result = readInt();
        if (result == -1) {
            System.exit(0);
        }
        return result;
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
