import org.junit.jupiter.api.Test;

import java.io.*;
import java.nio.file.Files;
import java.nio.file.Paths;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class F1_test {
    private void test(String input, String output) {
        StringWriter out = new StringWriter();
        try {
            F1.in = new BufferedReader(new FileReader(input));
            F1.out = new PrintWriter(out);
            F1.solve();
            assertEquals(new String(Files.readAllBytes(Paths.get(output))), out.toString());
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    @Test
    public void example1() {
        test("./tst/F1.1.in", "./tst/F1.1.out");
    }
}
