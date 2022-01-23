use std::io::stdin;

fn solve(a: i32, b: i32, c: i32) -> String {
    let sum = a + 2*b + 3*c;
    let result = if sum & 1 == 0 { 0 } else { 1 };
    format!("{result}")
}

fn main() {
    let mut input = Scanner::default();
    for _ in 0..input.next() {
        println!("{}", solve(input.next(), input.next(), input.next()));
    }
}

/// TEMPLATE
#[derive(Default)]
struct Scanner {
    buffer: Vec<String>
}
impl Scanner {
    fn next<T: std::str::FromStr>(&mut self) -> T {
        loop {
            if let Some(token) = self.buffer.pop() {
                return token.parse().ok().expect("Failed parse");
            }
            let mut input = String::new();
            stdin().read_line(&mut input).expect("Failed read");
            self.buffer = input.split_whitespace().rev().map(String::from).collect();
        }
    }
}

/// TESTS
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example1() {
        assert_eq!(solve(1, 1, 1), "0");
    }

    #[test]
    fn example2() {
        assert_eq!(solve(2, 1, 3), "1");
    }

    #[test]
    fn example3() {
        assert_eq!(solve(5, 5, 5), "0");
    }

    #[test]
    fn example4() {
        assert_eq!(solve(1, 1, 2), "1");
    }
}
