import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;

public class C {
    static void solve() {
        int t = readInt();
        while (t-- > 0) {
            int a = readInt();
            int b = readInt();
            String s = readString();
            doSolve(a, b, new StringBuilder(s));
        }
    }

    private static void doSolve(int a, int b, StringBuilder s) {
        int n = s.length();
        int left = 0;
        int right = n - 1;
        while (left <= right) {
            char left_char = s.charAt(left);
            char right_char = s.charAt(right);
            if (left_char != '?' && right_char != '?' && left_char != right_char) {
                out.println(-1);
                return;
            }
            if (left_char != '?' || right_char != '?') {
                char ch = left_char;
                if (left_char == '?') {
                    ch = right_char;
                }
                s.setCharAt(left, ch);
                s.setCharAt(right, ch);
                if (ch == '0') {
                    a -= (left != right) ? 2 : 1;
                } else {
                    b -= (left != right) ? 2 : 1;
                }
            }
            left++;
            right--;
        }

        left = 0;
        right = n - 1;
        while (left <= right) {
            char left_char = s.charAt(left);
            char right_char = s.charAt(right);
            if (left_char == '?' && right_char == '?') {
                char ch = '1';
                int needed = (left != right) ? 2 : 1;
                if (b < needed) {
                    if (a < needed) {
                        out.println(-1);
                        return;
                    }
                    ch = '0';
                }
                s.setCharAt(left, ch);
                s.setCharAt(right, ch);
                if (ch == '0') {
                    a -= needed;
                } else {
                    b -= needed;
                }
            }
            left++;
            right--;
        }
        
        if (a < 0 || b < 0) {
            out.println(-1);
        } else {
            out.println(s);
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
