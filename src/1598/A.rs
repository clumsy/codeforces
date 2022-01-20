use std::io::stdin;

fn solve(n: usize, grid: Vec<Vec<char>>) -> String {
    for c in 0..(n - 1) {
        if grid[0][c + 1] == '1' && grid[1][c + 1] == '1' {
            return format!("NO");
        }
    }
    format!("YES")
}

fn main() {
    let mut input = Scanner::default();
    for _ in 0..input.next() {
        let n = input.next();
        let grid = vec![
            input.next::<String>().chars().collect(),
            input.next::<String>().chars().collect()
        ];
        println!("{}", solve(n, grid));
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
        assert_eq!(solve(3, vec![
            "000".chars().collect(),
            "000".chars().collect()
        ]), "YES");
    }

    #[test]
    fn example2() {
        assert_eq!(solve(4, vec![
            "0011".chars().collect(),
            "1100".chars().collect()
        ]), "YES");
    }

    #[test]
    fn example3() {
        assert_eq!(solve(4, vec![
            "0111".chars().collect(),
            "1110".chars().collect()
        ]), "NO");
    }

    #[test]
    fn example4() {
        assert_eq!(solve(6, vec![
            "010101".chars().collect(),
            "101010".chars().collect()
        ]), "YES");
    }

    #[test]
    fn example5() {
        assert_eq!(solve(3, vec![
            "010".chars().collect(),
            "010".chars().collect()
        ]), "NO");
    }
}
