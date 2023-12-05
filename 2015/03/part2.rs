use std::env;
use std::fs;

fn main() {
    let directions = fs::read_to_string("input")
        .expect("Should have been able to read the file");
    let direction_length = directions.len();
    let mut grid = vec![vec![0; direction_length]; direction_length];     
    let mut i_santa = direction_length/2;
    let mut j_santa = direction_length/2;
    let mut i_robo = direction_length/2;
    let mut j_robo = direction_length/2;

    let mut k = 0;
    for d in directions.chars() {
        if k % 2 == 0 {
            match d {
                '^' => i_santa -= 1,
                'v' => i_santa += 1,
                '<' => j_santa -= 1,
                '>' => j_santa += 1,
                _ => println!("Invalid direction"),
            }
            grid[i_santa][j_santa] = 1;
        } else {
            match d {
                '^' => i_robo -= 1,
                'v' => i_robo += 1,
                '<' => j_robo -= 1,
                '>' => j_robo += 1,
                _ => println!("Invalid direction"),
            }
            grid[i_robo][j_robo] = 1;
        }
        k += 1;
    }
    let N_houses = grid.iter().flatten().sum::<i32>();
    println!("Houses visited: {}", N_houses); 
}
