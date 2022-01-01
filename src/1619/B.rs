use std::collections::HashSet;
use std::io::stdin;

fn solve(n: i32) -> i32 {
    let mut set = HashSet::new();
    let mut i = 1;
    while i*i <= n {
        set.insert(i*i);
        i += 1;
    }
    let mut i = 1;
    while i*i*i <= n {
        set.insert(i*i*i);
        i += 1;
    }
    set.len() as i32
}

fn main() {
    let mut input = Scanner::default();
    let t = input.read_int();
    for _ in 0..t {
        println!("{}", solve(input.read_int()));
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
        assert_eq!(solve(10), 4);
    }

    #[test]
    fn example2() {
        assert_eq!(solve(1), 1);
    }

    #[test]
    fn example3() {
        assert_eq!(solve(25), 6);
    }

    #[test]
    fn example4() {
        assert_eq!(solve(1000000000), 32591);
    }

    #[test]
    fn example5() {
        assert_eq!(solve(999999999), 32590);
    }

    #[test]
    fn example6() {
        assert_eq!(solve(500000000), 23125);
    }

    #[test]
    fn example7() {
        assert_eq!(solve(2), 1);
    }

    #[test]
    fn example8() {
        assert_eq!(solve(3), 1);
    }

    #[test]
    fn example9() {
        assert_eq!(solve(4), 2);
    }

    #[test]
    fn example10() {
        assert_eq!(solve(5), 2);
    }

    #[test]
    fn example11() {
        assert_eq!(solve(6), 2);
    }
}
