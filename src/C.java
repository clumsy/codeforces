import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;

public class C {
    static void solve() {
        int n = readInt();
        doSolve(n);
    }

    private static void doSolve(int n) {
        if (n == 2) {
            out.println(-1);
            return;
        }
        int root_n = (int) Math.ceil(Math.sqrt(n));
        if (n == root_n * root_n) {
            out.println(root_n);
            for (int i = 0; i < root_n; i++) {
                for (int j = 0; j < root_n; j++) {
                    out.print('o');
                }
                out.println();
            }
            return;
        }
        if (n == root_n * root_n - 2) {
            root_n++;
        }
        char[][] answer = new char[root_n][root_n];
        for (int i = 0; i < root_n; i++) {
            for (int j = 0; j < root_n; j++) {
                answer[i][j] = '.';
            }
        }
        doSolve(answer, n, root_n, root_n - 1, 0);
    }
    
    private static void doSolve(char[][] answer, int n, int root_n, int row, int col) {
        if (n == 0) {
            int size = answer.length;
            out.println(size);
            for (int i = 0; i < size; i++) {
                for (int j = 0; j < size; j++) {
                    out.print(answer[i][j]);
                }
                out.println();
            }
            return;
        }
        for (int k = 0; k < root_n; k++) {
            answer[row - k][col] = 'o';
            answer[row][col + k] = 'o';
        }
        int next_n = n - 2 * root_n + 1;
        int next_root_n = (int) Math.ceil(Math.sqrt(next_n));
        doSolve(answer, next_n, next_root_n, row - 1, col + 1);
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
