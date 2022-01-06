use std::io::stdin;

fn solve(x: String) -> String {
    let x_chars = x.chars().map(|c| c as i32 - '0' as i32).collect::<Vec<i32>>();
    if x_chars[x.len() - 1] & 1 == 0 {
        return "0".to_string();
    }
    if x_chars[0] & 1 == 0 {
        return "1".to_string();
    }
    if x_chars.iter().any(|d| d & 1 == 0) {
        return "2".to_string();
    }
    "-1".to_string()
}

fn main() {
    let mut input = Scanner::default();
    let t = input.read_int();
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
        assert_eq!(solve("3876".to_string()), "0".to_string());
    }

    #[test]
    fn example2() {
        assert_eq!(solve("387".to_string()), "2".to_string());
    }

    #[test]
    fn example3() {
        assert_eq!(solve("4489".to_string()), "1".to_string());
    }

    #[test]
    fn example4() {
        assert_eq!(solve("3".to_string()), "-1".to_string());
    }
}
