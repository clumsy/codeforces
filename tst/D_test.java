import org.junit.jupiter.api.Test;

import java.io.*;
import java.nio.file.Files;
import java.nio.file.Paths;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class D_test {
    private void test(String input, String output) {
        StringWriter out = new StringWriter();
        try {
            D.in = new BufferedReader(new FileReader(input));
            D.out = new PrintWriter(out);
            D.solve();
            assertEquals(new String(Files.readAllBytes(Paths.get(output))), out.toString());
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    @Test
    public void example1() {
        test("./tst/D.1.in", "./tst/D.1.out");
    }

    @Test
    public void example2() {
        test("./tst/D.2.in", "./tst/D.2.out");
    }

    @Test
    public void example3() {
        test("./tst/D.3.in", "./tst/D.3.out");
    }
}
