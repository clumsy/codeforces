import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;

public class A {
    static void solve() {
        int n = readInt();
        String[] commands = new String[n];
        for (int i = 0; i < n; i++) {
            commands[i] = readString();
        }
        doSolve(commands);
    }

    private static void doSolve(String[] commands) {
        String color = "blue";
        boolean unlocked = true;
        for (String command : commands) {
            switch (command) {
                case "lock":
                    unlocked = false;
                    break;
                case "unlock":
                    unlocked = true;
                    break;
                default:
                    if (unlocked) {
                        color = command;
                    }
            }
        }
        out.println(color);
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
