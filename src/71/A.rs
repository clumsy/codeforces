use std::io::stdin;

fn solve(s: String) -> String {
    if s.len() <= 10 {
        return s;
    }
    let mut chars = s.chars().into_iter();
    format!("{}{}{}", chars.next().unwrap(), s.len() - 2, chars.last().unwrap())
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
        assert_eq!(solve("word".to_string()), "word");
    }

    #[test]
    fn example2() {
        assert_eq!(solve("localization".to_string()), "l10n");
    }

    #[test]
    fn example3() {
        assert_eq!(solve("internationalization".to_string()), "i18n");
    }

    #[test]
    fn example4() {
        assert_eq!(solve("pneumonoultramicroscopicsilicovolcanoconiosis".to_string()), "p43s");
    }
}
