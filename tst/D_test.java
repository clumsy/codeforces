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
    public void example5() {
        test("./tst/D.5.in", "./tst/D.5.out");
    }
}
