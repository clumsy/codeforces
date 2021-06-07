import org.junit.jupiter.api.Test;

import java.io.*;
import java.nio.file.Files;
import java.nio.file.Paths;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class B1_test {
    private void test(String input, String output) {
        StringWriter out = new StringWriter();
        try {
            B1.in = new BufferedReader(new FileReader(input));
            B1.out = new PrintWriter(out);
            B1.solve();
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
}
