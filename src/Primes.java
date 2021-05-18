import java.util.ArrayList;
import java.util.List;

public class Primes {

    /**
     * Linear Prime Sieve: https://cp-algorithms.com/algebra/prime-sieve-linear.html
     */
    public static List<Integer> primesBelow(int n) {
        int[] lp = new int[n + 1];
        List<Integer> primes = new ArrayList<>();
        for (int i = 2; i < n; i++) {
            if (lp[i] == 0) {
                lp[i] = i;
                primes.add(i);
            }
            for (int j = 0; j < primes.size() && j <= lp[i] && i*primes.get(j) < n; j++) {
                lp[i*primes.get(j)] = primes.get(j);
            }
        }
        return primes;
    }
}
