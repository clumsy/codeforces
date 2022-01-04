use std::cmp::min;
use std::io::stdin;

fn solve(a: Vec<String>) -> String {
    let mut s = String::with_capacity(a.len() + 1);
    let mut found = false;
    for (i, c) in a.iter().enumerate() {
        let a_chars = a[i].chars().collect::<Vec<char>>();
        s.push(a_chars[0]);
        if i == a.len() - 1 {
            s.push(a_chars[1]);
        } else if a_chars[1] != a[i + 1].chars().collect::<Vec<char>>()[0] {
            s.push(a_chars[1]);
            found = true;
        }
    }
    if !found {
        s.push('a');
    }
    s
}

fn main() {
    let mut input = Scanner::default();
    let t = input.read_int();
    for _ in 0..t {
        let n = input.read_int() as usize;
        let mut a = Vec::with_capacity(n);
        for _ in 0..(n - 2) {
            a.push(input.read_next());
        }
        println!("{}", solve(a));
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
        let input =
            vec!["ab", "bb", "ba", "aa", "ba"].iter()
                .map(|it| it.to_string())
                .collect();
        assert_eq!(solve(input), "abbaaba");
    }

    #[test]
    fn example2() {
        let input =
            vec!["ab", "ba", "aa", "ab", "ba"].iter()
                .map(|it| it.to_string())
                .collect();
        assert_eq!(solve(input), "abaabaa");
    }

    #[test]
    fn example3() {
        let input =
            vec!["aa"].iter()
                .map(|it| it.to_string())
                .collect();
        assert_eq!(solve(input), "aaa");
    }

    #[test]
    fn example4() {
        let input =
            vec!["bb", "ab", "bb"].iter()
                .map(|it| it.to_string())
                .collect();
        assert_eq!(solve(input), "bbabb");
    }
}
