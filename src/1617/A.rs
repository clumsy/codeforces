use std::io::stdin;

fn solve(x: String, y: String) -> String {
    let mut count = [0; 26];
    let a = 'a' as usize;
    for c in x.chars() {
        count[c as usize - a] += 1;
    }
    let mut result = String::with_capacity(x.len());

    // always starts with all 'a's
    for _ in 0..count[0] {
        result.push('a');
    }
    
    // next is all 'b's or 'c's
    if count[0] > 0 && count[1] > 0 && count[2] > 0 && y == "abc" { // the only case where 'c's would precede 'b's
        for _ in 0..count[2] {
            result.push('c');
        }
        for _ in 0..count[1] {
            result.push('b');
        }
    } else {
        for _ in 0..count[1] {
            result.push('b');
        }
        for _ in 0..count[2] {
            result.push('c');
        }
    }

    // ends with the rest in lexicographical order
    for (i, c) in count.iter().enumerate() {
        if i < 3 {
            continue;
        }
        for _ in 0..*c {
            result.push(((a + i) as u8) as char);
        }
    }
    result
}

fn main() {
    let mut input = Scanner::default();
    let t = input.read_int();
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
        assert_eq!(solve("abacaba".to_string(), "abc".to_string()), "aaaacbb".to_string());
    }

    #[test]
    fn example2() {
        assert_eq!(solve("cccba".to_string(), "acb".to_string()), "abccc".to_string());
    }

    #[test]
    fn example3() {
        assert_eq!(solve("dbsic".to_string(), "bac".to_string()), "bcdis".to_string());
    }

    #[test]
    fn example4() {
        assert_eq!(solve("abracadabra".to_string(), "abc".to_string()), "aaaaacbbdrr".to_string());
    }

    #[test]
    fn example5() {
        assert_eq!(solve("dddddddddddd".to_string(), "cba".to_string()), "dddddddddddd".to_string());
    }

    #[test]
    fn example6() {
        assert_eq!(solve("bbc".to_string(), "abc".to_string()), "bbc".to_string());
    }

    #[test]
    fn example7() {
        assert_eq!(solve("ac".to_string(), "abc".to_string()), "ac".to_string());
    }
}
