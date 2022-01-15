use std::io::stdin;

fn solve(l: usize, x: Vec<usize>) -> String {
    let mut count = vec![0; l];
    let n = x.len();
    for x_i in x {
        for k in 0..l {
            count[k] += if x_i & (1 << k) == (1 << k) { 1 } else { 0 };
        }
    }
    let mut answer = 0;
    for i in 0..l {
        answer |= if count[i] >= (n + 1)/2 { 1 << i } else { 0 };
    }
    format!("{answer}")
}

fn main() {
    let mut input = Scanner::default();
    let t = input.read_usize();
    for _ in 0..t {
        let mut x = vec![0; input.read_usize()];
        let l = input.read_usize();
        for i in 0..x.len() {
            x[i] = input.read_usize();
        }
        println!("{}", solve(l, x));
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
        assert_eq!(solve(5, vec![18, 9, 21]), "17");
    }

    #[test]
    fn example2() {
        assert_eq!(solve(5, vec![18, 18, 18]), "18");
    }

    #[test]
    fn example3() {
        assert_eq!(solve(1, vec![1]), "1");
    }

    #[test]
    fn example4() {
        assert_eq!(solve(30, vec![1, 2, 3, 4, 5]), "1");
    }

    #[test]
    fn example5() {
        assert_eq!(solve(10, vec![99, 35, 85, 46, 78, 55]), "103");
    }

    #[test]
    fn example6() {
        assert_eq!(solve(1, vec![0, 1]), "1");
    }

    #[test]
    fn example7() {
        assert_eq!(solve(8, vec![5, 16, 42, 15, 83, 65, 78, 42]), "11");
    }
}
