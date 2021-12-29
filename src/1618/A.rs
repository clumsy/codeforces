use std::io::stdin;

fn solve(b: [i32; 7]) -> String {
    format!("{} {} {}", b[0], b[1], b[6] - b[0] - b[1])
}

fn main() {
    let mut input = Scanner::default();
    let t = input.read_int();
    for _ in 0..t {
        let mut b = [0; 7];
        for i in 0..7 {
            b[i] = input.read_int();
        }
        println!("{}", solve(b));
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
        assert_eq!(solve([1,3,4,4,5,7,8]), "1 3 4");
    }

    #[test]
    fn example2() {
        assert_eq!(solve([1,2,3,4,5,6,7]), "1 2 4");
    }
    
    #[test]
    fn example3() {
        assert_eq!(solve([300000000,300000000,300000000,600000000,600000000,600000000,900000000]),
            "300000000 300000000 300000000");
    }
    
    #[test]
    fn example4() {
        assert_eq!(solve([1,1,2,999999998,999999999,999999999,1000000000]), "1 1 999999998");
    }
    
    #[test]
    fn example5() {
        assert_eq!(solve([1,2,2,3,3,4,5]), "1 2 2");
    }
}
