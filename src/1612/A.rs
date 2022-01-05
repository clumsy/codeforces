use std::io::stdin;

fn solve(x_b: i32, y_b: i32) -> String {
    let sum = x_b + y_b; 
    if sum & 1 != 0 {
        format!("-1 -1")
    } else {
        if x_b >= y_b {
            format!("{} {}", sum/2, 0)
        } else {
            format!("{} {}", 0, sum/2)
        }
    }
}

fn main() {
    let mut input = Scanner::default();
    let t = input.read_int();
    for _ in 0..t {
        println!("{}", solve(input.read_int(), input.read_int()));
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
        assert_eq!(solve(13, 0), "-1 -1");
    }

    #[test]
    fn example2() {
        assert_eq!(solve(42, 0), "21 0");
    }

    #[test]
    fn example3() {
        assert_eq!(solve(49, 3), "26 0");
    }

    #[test]
    fn example4() {
        assert_eq!(solve(2, 50), "0 26");
    }
}
