import org.junit.jupiter.api.Test;

import java.io.BufferedReader;
import java.io.PrintWriter;
import java.io.StringReader;
import java.io.StringWriter;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class A_test {
    private void test(String input, String output) {
        StringWriter out = new StringWriter();
        A.in = new BufferedReader(new StringReader((input)));
        A.out = new PrintWriter(out);
        A.solve();
        assertEquals(out.toString().trim(), output);
    }

    @Test
    public void example1() {
        test("6 6 4", "4");
    }

    @Test
    public void example2() {
        test("1000000000 1000000000 1", "1000000000000000000");
    }
}
