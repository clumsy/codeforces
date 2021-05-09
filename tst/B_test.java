import org.junit.jupiter.api.Test;

import java.io.*;
import java.nio.file.Files;
import java.nio.file.Paths;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class B_test {
    private void test(String input, String output) {
        StringWriter out = new StringWriter();
        try {
            B.in = new BufferedReader(new FileReader(input));
            B.out = new PrintWriter(out);
            B.solve();
            assertEquals(new String(Files.readAllBytes(Paths.get(output))), out.toString());
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    @Test
    public void example1() {
        test("./tst/B.1.in", "./tst/B.1.out");
    }

    @Test
    public void example2() {
        test("./tst/B.2.in", "./tst/B.2.out");
    }

    @Test
    public void example3() {
        test("./tst/B.3.in", "./tst/B.3.out");
    }
}
