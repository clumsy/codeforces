import org.junit.jupiter.api.Test;

import java.io.*;
import java.nio.file.Files;
import java.nio.file.Paths;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class A_test {
    private void test(String input, String output) {
        StringWriter out = new StringWriter();
        try {
            A.in = new BufferedReader(new FileReader(input));
            A.out = new PrintWriter(out);
            A.solve();
            assertEquals(new String(Files.readAllBytes(Paths.get(output))), out.toString());
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    @Test
    public void example1() {
        test("./tst/A.1.in", "./tst/A.1.out");
    }
}
