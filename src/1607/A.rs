use std::io::stdin;

fn solve(k: String, s: String) -> String {
    let c2i = |c: char| c as usize - 'a' as usize;
    let mut m = [0; 26];
    for (i, c) in k.chars().enumerate() {
        m[c2i(c)] = i as i32;
    }
    let result: i32 = s.chars()
        .skip(1)
        .zip(s.chars())
        .map(|(s_i, s_j)| (m[c2i(s_i)] - m[c2i(s_j)]).abs())
        .sum();
    format!("{result}")
}

fn main() {
    let mut input = Scanner::default();
    let t = input.read_next();
    for _ in 0..t {
        println!("{}", solve(input.read_next(), input.read_next()));
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
        assert_eq!(solve("abcdefghijklmnopqrstuvwxyz".to_string(), "hello".to_string()), "13");
    }

    #[test]
    fn example2() {
        assert_eq!(solve("abcdefghijklmnopqrstuvwxyz".to_string(), "i".to_string()), "0");
    }

    #[test]
    fn example3() {
        assert_eq!(solve("abcdefghijklmnopqrstuvwxyz".to_string(), "codeforces".to_string()), "68");
    }

    #[test]
    fn example4() {
        assert_eq!(solve("qwertyuiopasdfghjklzxcvbnm".to_string(), "qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq".to_string()), "0");
    }

    #[test]
    fn example5() {
        assert_eq!(solve("qwertyuiopasdfghjklzxcvbnm".to_string(), "abacaba".to_string()), "74");
    }
}
