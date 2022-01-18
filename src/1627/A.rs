use std::io::stdin;

fn solve(grid: Vec<Vec<bool>>, r: usize, c: usize) -> String {
    if grid[r][c] {
        "0"
    } else if (0..grid[r].len()).any(|c| grid[r][c]) || (0..grid.len()).any(|r| grid[r][c]) {
        "1"
    } else if (0..grid.len()).any(|r| (0..grid[r].len()).any(|c| grid[r][c])) {
        "2"
    } else {
        "-1"
    }.to_string()
}

fn main() {
    let mut input = Scanner::default();
    let t = input.read_next();
    for _ in 0..t {
        let n = input.read_next();
        let m: usize = input.read_next();
        let r: usize = input.read_next();
        let c: usize = input.read_next();
        let grid = (0..n)
            .map(|_|
                input.read_next::<String>().chars()
                    .map(|c| c == 'B')
                    .collect())
            .collect();
        println!("{}", solve(grid, r - 1, c - 1));
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
}

/// TESTS
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example1() {
        let grid = vec![
            vec![false, true,  false, false, false],
            vec![true,  true,  true,  false, true],
            vec![false, false, true,  true,  true],
        ];
        assert_eq!(solve(grid, 0, 3), "1");
    }

    #[test]
    fn example2() {
        let grid = vec![
            vec![true, false,  false],
            vec![true,  true,  false],
            vec![false, true, true],
            vec![false, false, true],
        ];
        assert_eq!(solve(grid, 1, 0), "0");
    }

    #[test]
    fn example3() {
        let grid = vec![
            vec![false, false, false],
            vec![false, false, false],
        ];
        assert_eq!(solve(grid, 1, 0), "-1");
    }

    #[test]
    fn example4() {
        let grid = vec![
            vec![false, false],
            vec![false, true],
        ];
        assert_eq!(solve(grid, 0, 0), "2");
    }
}
