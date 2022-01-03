use std::io::stdin;

fn solve(l1: i32, l2: i32, l3: i32) -> String {
    // can split one to match other two
    if     l1 - l3 == l2
        || l2 - l3 == l1
        || l1 - l2 == l3
        || l3 - l1 == l2 
        || l3 - l2 == l1
        || l2 - l1 == l3 {
        return "YES".to_string();
    }
    // can split one in half, when two others match
    if     (l1 == l2 && l3 & 1 == 0)
        || (l1 == l3 && l2 & 1 == 0)
        || (l2 == l3 && l1 & 1 == 0) {
        return "YES".to_string();
    }
    return "NO".to_string();
}

fn main() {
    let mut input = Scanner::default();
    let t = input.read_int();
    for _ in 0..t {
        println!("{}", solve(input.read_next(), input.read_int(), input.read_int()));
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
        assert_eq!(solve(6, 1,5), "YES");
    }

    #[test]
    fn example2() {
        assert_eq!(solve(2, 5, 2), "NO");
    }

    #[test]
    fn example3() {
        assert_eq!(solve(2, 4, 2), "YES");
    }

    #[test]
    fn example4() {
        assert_eq!(solve(5, 5, 4), "YES");
    }
}
