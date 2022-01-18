use std::io::stdin;

fn solve(s: String) -> String {
    let mut count = [0; 26];
    for c in s.chars().map(|c| c as usize) {
        count[c - 'a' as usize] += 1;
    }
    let mut result = String::with_capacity(s.len());
    for mut i in 0..count.len() {
        while count[i] > 0 {
            result.push(char::from(b'a' + i as u8));
            count[i] -= 1;
        }
    }
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
        assert_eq!(solve("oelhl".to_string()), "ehllo");
    }

    #[test]
    fn example2() {
        assert_eq!(solve("abcdcba".to_string()), "aabbccd");
    }

    #[test]
    fn example3() {
        assert_eq!(solve("ac".to_string()), "ac");
    }
}
