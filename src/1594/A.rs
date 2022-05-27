use std::io::stdin;

fn solve(n: i64) -> String {
    for x in 0..100 {
        let l_square = 1 - 4*(2*n - x*x);
        let l_root = (l_square as f64).sqrt() as i64;
        if l_square == l_root * l_root && l_root & 1 == 1 {
            let l = (1 - l_root) / 2;
            let r_square = 1 - 4*(l - 2*n - l*l);
            let r_root = (r_square as f64).sqrt() as i64;
            if r_square == r_root * r_root && r_root & 1 == 1 {
                let r1 = (1 - r_root) / 2;
                if (l + r1)*(r1 - l + 1) == 2*n {
                    return format!("{l} {r1}");
                }
                let r2 = (1 + r_root) / 2;
                return format!("{l} {r2}");
            }
        }
    }
    format!("NOT POSSIBLE")
}

fn main() {
    let mut input = Scanner::default();
    for _ in 0..input.next() {
        println!("{}", solve(input.next()));
    }
}

/// TEMPLATE
#[derive(Default)]
struct Scanner {
    buffer: Vec<String>
}
impl Scanner {
    fn next<T: std::str::FromStr>(&mut self) -> T {
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
        assert_eq!(solve(1), "YES");
    }

    #[test]
    fn example2() {
        assert_eq!(solve(2), "YES");
    }

    #[test]
    fn example3() {
        assert_eq!(solve(3), "NO");
    }

    #[test]
    fn example4() {
        assert_eq!(solve(6), "NO");
    }
}
