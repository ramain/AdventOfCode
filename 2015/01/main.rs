use std::env;
use std::fs;

fn main() {
    println!("In file {}", "input");

    let contents = fs::read_to_string("input")
        .expect("Should have been able to read the file");

    println!("With text:\n{contents}");
    let mut num: i32;
    let mut i: i32 = 1;
    let mut switch: i32 = 0;

    num = 0;
    for c in contents.chars() {
        if c == '(' {
            num += 1;
        } else if c == ')' {
            num -= 1;
        } else {
            println!("Unexpected character {}", c);
            break;
        }
        if num == -1 && switch == 0 {
            println!("First basement at {}", i);
            switch = 1;
        }
        i += 1;
    }
    println!("Final floor: {}", num);

}
