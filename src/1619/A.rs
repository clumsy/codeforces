use std::io::stdin;

fn solve(s: String) -> String {
    if s.len() & 1 != 0 {
        return "NO".to_string();
    }
    let chars: Vec<_> = s.chars().collect();
    let half = chars.len()/2;
    for i in 0..half {
        if chars[i] != chars[i + half] {
            return "NO".to_string();
        }
    }
    return "YES".to_string();
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
        assert_eq!(solve("a".to_string()), "NO");
    }

    #[test]
    fn example2() {
        assert_eq!(solve("aa".to_string()), "YES");
    }

    #[test]
    fn example3() {
        assert_eq!(solve("aaa".to_string()), "NO");
    }

    #[test]
    fn example4() {
        assert_eq!(solve("aaaa".to_string()), "YES");
    }

    #[test]
    fn example5() {
        assert_eq!(solve("abab".to_string()), "YES");
    }

    #[test]
    fn example6() {
        assert_eq!(solve("abcabc".to_string()), "YES");
    }

    #[test]
    fn example7() {
        assert_eq!(solve("abacaba".to_string()), "NO");
    }

    #[test]
    fn example8() {
        assert_eq!(solve("xxyy".to_string()), "NO");
    }

    #[test]
    fn example9() {
        assert_eq!(solve("xyyx".to_string()), "NO");
    }

    #[test]
    fn example10() {
        assert_eq!(solve("xyxy".to_string()), "YES");
    }
}
