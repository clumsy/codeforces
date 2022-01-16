use std::io::{repeat, stdin};

fn solve(n: usize, k: usize) -> String {
    if k > (n + 1)/2 {
        return format!("-1");
    }
    let mut result = Vec::with_capacity(n);
    for i in 0..n {
        let string = if i & 1 == 0 && i < 2*k {
            ".".repeat(i) + "R" + ".".repeat(n - i - 1).as_str()
        } else {
            ".".repeat(n)
        };
        result.push(string);
    }
    result.join("\n")
}

fn main() {
    let mut input = Scanner::default();
    let t = input.read_usize();
    for _ in 0..t {
        println!("{}", solve(input.read_usize(), input.read_usize()));
    }
}

/// TEMPLATE
#[derive(Default)]
struct Scanner {
    buffer: Vec<String>
}
impl Scanner {
    fn read_next<T: std::str::FromStr>(&mut self) -> T {
        loop {
            if let Some(token) = self.buffer.pop() {
                return token.parse().ok().expect("Failed parse");
            }
            let mut input = String::new();
            stdin().read_line(&mut input).expect("Failed read");
            self.buffer = input.split_whitespace().rev().map(String::from).collect();
        }
    }

    fn read_usize(&mut self) -> usize {
        self.read_next::<usize>()
    }
}

/// TESTS
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example1() {
        assert_eq!(solve(3, 2), "R..\n...\n..R");
    }

    #[test]
    fn example2() {
        assert_eq!(solve(3, 3), "-1");
    }

    #[test]
    fn example3() {
        assert_eq!(solve(1, 1), "R");
    }

    #[test]
    fn example4() {
        assert_eq!(solve(5, 2), "R....\n.....\n..R..\n.....\n.....");
    }

    #[test]
    fn example5() {
        assert_eq!(solve(40, 33), "-1");
    }
}
