fn solve(n: i32, m: i32, a: i32) -> i64 {
    let width  = n/a + (if n % a != 0 {1} else {0});
    let height = m/a + (if m % a != 0 {1} else {0});
    (width as i64)*(height as i64)
}

fn main() {
    let mut input = Scanner::default();
    let m = input.read_int();
    let n = input.read_int();
    let a = input.read_int();
    println!("{}", solve(n, m, a));
}

/// TEMPLATE
use std::io::stdin;

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
        assert_eq!(solve(6, 6,4), 4);
    }
}
