use std::io::stdin;

fn solve(n: usize) -> String {
    let result: Vec<String> = (2..=(n + 1)).map(|i| i.to_string()).collect();
    let result = result.join(" ");
    format!("{result}")
}

fn main() {
    let mut input = Scanner::default();
    let t = input.read_next();
    for _ in 0..t {
        println!("{}", solve(input.read_next()));
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
}

/// TESTS
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example1() {
        assert_eq!(solve(1), "2");
    }

    #[test]
    fn example2() {
        assert_eq!(solve(2), "2 3");
    }

    #[test]
    fn example3() {
        assert_eq!(solve(7), "2 3 4 5 6 7 8");
    }
}
