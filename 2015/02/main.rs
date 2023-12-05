use std::env;
use std::fs;

fn main() {
    let contents = fs::read_to_string("input")
        .expect("Should have been able to read the file");

    let mut total_area: i32 = 0;
    let mut total_ribbon: i32 = 0;
    for line in contents.lines() {
        println!("{}", line);
        let linesplit = line.split("x");
        let mut dims: Vec<i32> = Vec::new();
        let mut area: i32 = 1;
        for dim in linesplit {
            let dim_int: i32 = dim.parse().unwrap();
            dims.push(dim_int);
        }
        dims.sort();
        let side1 = dims[0]*dims[1];
        let side2 = dims[1]*dims[2];
        let side3 = dims[2]*dims[0];

        let area = 2*side1 + 2*side2 + 2*side3 + side1;
        total_area += area;

        let volume = dims[0]*dims[1]*dims[2];
        let smallest_perimeter = 2*dims[0] + 2*dims[1];
        let ribbon = volume + smallest_perimeter;
        total_ribbon += ribbon;
    }
    println!("Total area: {}", total_area);
    println!("Total ribbon: {}", total_ribbon);
}
