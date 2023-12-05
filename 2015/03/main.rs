use std::env;
use std::fs;

fn main() {
    let directions = fs::read_to_string("input")
        .expect("Should have been able to read the file");
    let direction_length = directions.len();
    let mut grid = vec![vec![0; direction_length]; direction_length];     
    let mut i_start = direction_length/2;
    let mut j_start = direction_length/2;
    for d in directions.chars() {
        match d {
            '^' => i_start -= 1,
            'v' => i_start += 1,
            '<' => j_start -= 1,
            '>' => j_start += 1,
            _ => println!("Invalid direction"),
        }
        grid[i_start][j_start] = 1;
    }
    let N_houses = grid.iter().flatten().sum::<i32>();
    println!("Houses visited: {}", N_houses); 
}
