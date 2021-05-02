import org.junit.jupiter.api.Test;

import java.io.*;
import java.nio.file.Files;
import java.nio.file.Paths;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class E_test {
    private void test(String input, String output) {
        StringWriter out = new StringWriter();
        try {
            E.in = new BufferedReader(new FileReader(input));
            E.out = new PrintWriter(out);
            E.solve();
            assertEquals(new String(Files.readAllBytes(Paths.get(output))), out.toString());
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    @Test
    public void example1() {
        test("./tst/E.1.in", "./tst/E.1.out");
    }

    @Test
    public void example2() {
        test("./tst/E.2.in", "./tst/E.2.out");
    }

    @Test
    public void example3() {
        test("./tst/E.3.in", "./tst/E.3.out");
    }
}
