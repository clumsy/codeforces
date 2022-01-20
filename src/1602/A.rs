use std::cmp::max;
use std::io::stdin;

fn solve(mut s: String) -> String {
    let (i, c) = s.chars().enumerate()
        .min_by(|(_, a), (_, b)| a.cmp(b))
        .unwrap();
    s.remove(i);
    format!("{c} {s}")
}

fn main() {
    let mut input = Scanner::default();
    for _ in 0..input.next() {
        println!("{}", solve(input.next()));
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
        assert_eq!(solve("fc".to_string()), "c f");
    }

    #[test]
    fn example2() {
        assert_eq!(solve("aaaa".to_string()), "a aaa");
    }

    #[test]
    fn example3() {
        assert_eq!(solve("thebrightboiler".to_string()), "b therightboiler");
    }
}
