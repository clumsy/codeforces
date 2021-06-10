import org.junit.jupiter.api.Test;

import java.io.*;
import java.nio.file.Files;
import java.nio.file.Paths;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class C_test {
    private void test(String input, String output) {
        StringWriter out = new StringWriter();
        try {
            C.in = new BufferedReader(new FileReader(input));
            C.out = new PrintWriter(out);
            C.solve();
            assertEquals(new String(Files.readAllBytes(Paths.get(output))), out.toString());
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    @Test
    public void example1() {
        test("./tst/C.1.in", "./tst/C.1.out");
    }

    @Test
    public void example2() {
        test("./tst/C.2.in", "./tst/C.2.out");
    }

    @Test
    public void example3() {
        test("./tst/C.3.in", "./tst/C.3.out");
    }

    @Test
    public void example4() {
        test("./tst/C.4.in", "./tst/C.4.out");
    }
}
