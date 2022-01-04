use std::cmp::min;
use std::io::stdin;

fn solve(n: i32, m: i32, rb: i32, cb: i32, rd: i32, cd: i32) -> String {
    let r_steps = if rd >= rb {
        rd - rb
    } else {
        n - rb + n - rd
    };
    let c_steps = if cd >= cb {
        cd - cb
    } else {
        m - cb + m - cd
    };
    min(r_steps, c_steps).to_string()
}

fn main() {
    let mut input = Scanner::default();
    let t = input.read_int();
    for _ in 0..t {
        let n = input.read_int();
        let m = input.read_int();
        let rb = input.read_int();
        let cb = input.read_int();
        let rd = input.read_int();
        let cd = input.read_int();
        println!("{}", solve(n, m, rb, cb, rd, cd));
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
        assert_eq!(solve(10, 10, 6, 1, 2, 8), "7");
    }

    #[test]
    fn example2() {
        assert_eq!(solve(10, 10, 9, 9, 1, 1), "10");
    }

    #[test]
    fn example3() {
        assert_eq!(solve(9, 8, 5, 6, 2, 1), "9");
    }

    #[test]
    fn example4() {
        assert_eq!(solve(6, 9, 2, 2, 5, 8), "3");
    }

    #[test]
    fn example5() {
        assert_eq!(solve(2, 2, 1, 1, 2, 1), "0");
    }
}
