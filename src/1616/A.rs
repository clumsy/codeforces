use std::cmp::{max, min};
use std::io::stdin;

fn solve(a: Vec<i32>) -> i32 {
    let mut count = [0; 201];
    for x in a {
        count[(100 + x) as usize] += 1;
    }
    let mut result = min(1, count[100]);
    for i in 1..101 {
        result += min(2, count[100 + i] + count[100 - i]);
    }
    result
}

fn main() {
    let mut input = Scanner::default();
    let t = input.read_int();
    for _ in 0..t {
        let n = input.read_int() as usize;
        let mut a = Vec::with_capacity(n);
        for _ in 0..n {
            a.push(input.read_next());
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

    fn read_int(&mut self) -> i32 {
        self.read_next::<i32>()
    }
}

/// TESTS
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example1() {
        assert_eq!(solve(vec![1, 1, 2, 2]), 4);
    }

    #[test]
    fn example2() {
        assert_eq!(solve(vec![1, 2, 3]), 3);
    }

    #[test]
    fn example3() {
        assert_eq!(solve(vec![0, 0]), 1);
    }

    #[test]
    fn example4() {
        assert_eq!(solve(vec![0, 0, 0, 1, -1, 1, 2, 2, 2, 3, -3, 3, 4, 4, 4, 5, -5, 5]), 11);
    }
}
