use std::cmp::{max, min};
use std::io::stdin;

fn solve(mut a: i32, mut b: i32) -> String {
    let result = if a == b {
        a/2
    } else {
        let (a, b) = (max(a, b), min(a, b));
        let n = (a - b)/2; // x + 3n = a, x + n = b => b + 2n = a => n = a - b/2
        min(n, b) + max(0, (b - n)/2) // x/2 from a and x/2 from b
    };
    format!("{result}")
}

fn main() {
    let mut input = Scanner::default();
    for _ in 0..input.next() {
        println!("{}", solve(input.next(), input.next()));
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
        assert_eq!(solve(5, 5), "2");
    }

    #[test]
    fn example2() {
        assert_eq!(solve(10, 1), "1");
    }

    #[test]
    fn example3() {
        assert_eq!(solve(2, 3), "1");
    }

    #[test]
    fn example4() {
        assert_eq!(solve(0, 0), "0");
    }

    #[test]
    fn example5() {
        assert_eq!(solve(17, 2), "2");
    }

    #[test]
    fn example6() {
        assert_eq!(solve(1000000000, 1000000000), "500000000");
    }

    #[test]
    fn example7() {
        assert_eq!(solve(29, 11), "10");
    }

    #[test]
    fn example8() {
        assert_eq!(solve(9, 3), "3");
    }

    #[test]
    fn example9() {
        assert_eq!(solve(13, 17), "7");
    }
}
