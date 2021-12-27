use std::io::stdin;

fn solve(s: String) -> &'static str {
    let count_n = s.chars().filter(|c| *c == 'N').count();
    if count_n == 1 { "NO" } else { "YES" }
}

fn main() {
    let mut input = Scanner::default();
    let t = input.read_int();
    for _ in 0..t {
        println!("{}", solve(input.read_str()));
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

    fn read_str(&mut self) -> String {
        self.read_next::<String>()
    }
}

/// TESTS
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example1() {
        assert_eq!(solve("EEE".to_string()), "YES");
    }

    #[test]
    fn example2() {
        assert_eq!(solve("EEN".to_string()), "NO");
    }

    #[test]
    fn example3() {
        assert_eq!(solve("ENNEENE".to_string()), "YES");
    }

    #[test]
    fn example4() {
        assert_eq!(solve("NENN".to_string()), "YES");
    }
}
