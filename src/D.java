import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.*;

public class D {
    static void solve() {
        int t = readInt();
        while (t-- > 0) {
            doSolve(readInt(), readInt(), readInt());
        }
    }

    private static void doSolve(int a, int b, int k) {
        int gcd = gcd(a, b);
        int min_moves = 2;
        if (a == b) {
            min_moves = 0;
        } else if (a == gcd || b == gcd) {
            min_moves = 1;
        }
        int max_moves = factors(a).size() + factors(b).size();
        if (k == 1 && min_moves == 1 && k <= max_moves) { // only one move has to be done and it's possible
            out.println("YES");
        } else if (k != 1 && k >= min_moves && k <= max_moves) { // more than one move, but we got enough factors
            out.println("YES");
        } else {
            out.println("NO");
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

    static int gcd(int a, int b) {
        while (b > 0) {
            a %= b;
            b = swap(a, a = b);
        }
        return a;
    }

    static int lcm(int a, int b) {
        return a / gcd(a, b) * b;
    }
    
    static List<Integer> factors(int n) {
        List<Integer> factors = new ArrayList<>();
        while (n % 2 == 0) {
            factors.add(2);
            n /= 2;
        }
        for (int i = 3, sqrt = (int) Math.sqrt(n); i <= sqrt; i += 2) {
            while (n % i == 0) {
                factors.add(i);
                n /= i;
            }
        }
        if (n > 1) {
            factors.add(n);
        }
        return factors;
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
