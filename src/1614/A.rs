use std::io::stdin;

fn solve(l: i32, r: i32, k: i32, a: Vec<i32>) -> String {
    let mut k = k;
    let mut a = a;
    a.sort();
    let mut count = 0;
    for i in 0..a.len() {
        if a[i] >= l {
            k -= a[i];
            if k < 0 || a[i] > r {
                break;
            }
            count += 1
        }
    }
    format!("{}", count)
}

fn main() {
    let mut input = Scanner::default();
    let t = input.read_int();
    for _ in 0..t {
        let n = input.read_int();
        let l = input.read_int();
        let r = input.read_int();
        let k = input.read_int();
        let mut a = Vec::with_capacity(n as usize);
        for _ in 0..n {
            a.push(input.read_int())
        }
        println!("{}", solve(l, r, k, a));
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
        assert_eq!(solve(1,100,100,vec![50,100,50]), "2");
    }

    #[test]
    fn example2() {
        assert_eq!(solve(3,5,10,vec![1,2,3,4,5,6]), "2");
    }

    #[test]
    fn example3() {
        assert_eq!(solve(3,5,21,vec![1,2,3,4,5,6]), "3");
    }

    #[test]
    fn example4() {
        assert_eq!(solve(50,69,100,vec![20,30,40,77,1,1,12,4,70,10000]), "0");
    }

    #[test]
    fn example5() {
        assert_eq!(solve(50,80,30,vec![20,60,70]), "0");
    }

    #[test]
    fn example6() {
        assert_eq!(solve(2,7,100,vec![2,2,2,2,2,7,7,7,7,7]), "10");
    }

    #[test]
    fn example7() {
        assert_eq!(solve(1000000000,1000000000,1000000000,
                         vec![1000000000,1000000000,1000000000,1000000000]), "1");
    }

    #[test]
    fn example8() {
        assert_eq!(solve(1,1,1,vec![1]), "1");
    }
}
