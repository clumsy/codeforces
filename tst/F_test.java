import org.junit.jupiter.api.Test;

import java.io.*;
import java.nio.file.Files;
import java.nio.file.Paths;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class F_test {
    private void test(String input, String output) {
        StringWriter out = new StringWriter();
        try {
            F.in = new BufferedReader(new FileReader(input));
            F.out = new PrintWriter(out);
            F.solve();
            assertEquals(new String(Files.readAllBytes(Paths.get(output))), out.toString());
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    @Test
    public void example1() {
        test("./tst/F.1.in", "./tst/F.1.out");
    }
}
