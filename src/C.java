import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class C {
    static void solve() {
        int t = readInt();
        while (t-- > 0) {
            int n = readInt();
            int l = readInt();
            int r = readInt();
            int[] a = new int[n];
            for (int i = 0; i < n; i++) {
                a[i] = readInt();
            }
            doSolve(a, l, r);
        }
    }

    private static void doSolve(int[] a, int l, int r) {
        Arrays.sort(a);
        long answer = 0;
        for (int i = 0, max = a.length - 1; i < max; i++) {
            int left = l - a[i];
            int left_i = lower_bound(a, i + 1, max, left);
            if (a[left_i] < left) { // no valid pairs left
                continue;
            }
            int right = r - a[i];
            int right_i = upper_bound(a, left_i, max, right);
            if (a[right_i] > right) { // no valid pairs left
                continue;
            }
            answer += right_i - left_i + 1;
        }
        out.println(answer);
    }

    private static int lower_bound(int[] a, int lo, int hi, int pivot) {
        while (lo < hi) {
            int mid = lo + (hi - lo)/2;
            if (a[mid] >= pivot) {
                hi = mid;
            } else {
                lo = mid + 1;
            }   
        }
        return lo;
    }

    private static int upper_bound(int[] a, int lo, int hi, int pivot) {
        while (lo < hi) {
            int mid = hi - (hi - lo)/2;
            if (a[mid] <= pivot) {
                lo = mid;
            } else {
                hi = mid - 1;
            }
        }
        return lo;
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
