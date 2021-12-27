fn solve(a: Vec<i32>) -> i64 {
    let sum: i32 = a.iter().sum();
    if sum % a.len() as i32 == 0 { 0 } else { 1 }
}

fn main() {
    let mut input = Scanner::default();
    let t = input.read_int();
    for _ in 0..t {
        let n = input.read_int() as usize;
        let mut a = Vec::with_capacity(n);
        for _ in 0..n {
            a.push(input.read_int());
        }
        println!("{}", solve(a));
    }
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
        assert_eq!(solve(vec![10,10,10]), 0);
    }
    
    #[test]
    fn example2() {
        assert_eq!(solve(vec![3,2,1,2]), 0);
    }
    
    #[test]
    fn example3() {
        assert_eq!(solve(vec![1,2,3,1,5]), 1);
    }
}
