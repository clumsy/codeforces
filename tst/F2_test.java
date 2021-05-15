import org.junit.jupiter.api.Test;

import java.io.*;
import java.nio.file.Files;
import java.nio.file.Paths;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class F2_test {
    private void test(String input, String output) {
        StringWriter out = new StringWriter();
        try {
            F2.in = new BufferedReader(new FileReader(input));
            F2.out = new PrintWriter(out);
            F2.solve();
            assertEquals(new String(Files.readAllBytes(Paths.get(output))), out.toString());
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    @Test
    public void example1() {
        test("./tst/F2.1.in", "./tst/F2.1.out");
    }

    @Test
    public void example2() {
        test("./tst/F2.2.in", "./tst/F2.2.out");
    }
}
