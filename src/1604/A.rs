use std::cmp::max;
use std::io::stdin;

fn solve(a: Vec<i32>) -> String {
    let mut result = 0;
    for i in 0..a.len() {
        result += max(0, a[i] - (i as i32 + 1) - result);
    }
    format!("{result}")
}

fn main() {
    let mut input = Scanner::default();
    for _ in 0..input.next() {
        let mut a = vec![0; input.next()];
        for i in 0..a.len() {
            a[i] = input.next();
        }
        println!("{}", solve(a));
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
        assert_eq!(solve(vec![1, 3, 4]), "1");
    }

    #[test]
    fn example2() {
        assert_eq!(solve(vec![1, 2, 5, 7, 4]), "3");
    }

    #[test]
    fn example3() {
        assert_eq!(solve(vec![1]), "0");
    }

    #[test]
    fn example4() {
        assert_eq!(solve(vec![69, 6969, 696969]), "696966");
    }
}
