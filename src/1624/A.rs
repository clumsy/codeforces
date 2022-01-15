use std::io::stdin;

fn solve(a: Vec<usize>) -> String {
    let mut min = usize::MAX;
    let mut max = usize::MIN;
    for a_i in a {
        min = min.min(a_i);
        max = max.max(a_i);
    }
    let answer = max - min;
    format!("{answer}")
}

fn main() {
    let mut input = Scanner::default();
    let t = input.read_usize();
    for _ in 0..t {
        let mut a = vec![0; input.read_usize()];
        for i in 0..a.len() {
            a[i] = input.read_usize();
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

    fn read_usize(&mut self) -> usize {
        self.read_next::<usize>()
    }
}

/// TESTS
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example1() {
        assert_eq!(solve(vec![3, 4, 2, 4, 1, 2]), "3");
    }

    #[test]
    fn example2() {
        assert_eq!(solve(vec![1000, 1002, 998]), "4");
    }

    #[test]
    fn example3() {
        assert_eq!(solve(vec![12, 11]), "1");
    }
}
