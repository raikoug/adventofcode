use regex::Regex;
use lazy_static::lazy_static;


fn str_strip_numbers(s: &str) -> Vec<i64> {
    lazy_static! {
        static ref RE: Regex = Regex::new(r"\d").unwrap();
    }
    // iterate over all matches
    RE.find_iter(s)
        // try to parse the string matches as i64 (inferred from fn type signature)
        // and filter out the matches that can't be parsed (e.g. if there are too many digits to store in an i64).
        .filter_map(|digits| digits.as_str().parse().ok())
        // collect the results in to a Vec<i64> (inferred from fn type signature)
        .collect()
}

pub fn join_first_and_last_numbers(s: &str) -> i64 {
    let numbers: Vec<i64> = str_strip_numbers(s);
    let first: char = numbers.first().unwrap().to_string().chars().next().unwrap();
    let last: char = numbers.last().unwrap().to_string().chars().next().unwrap();
    let merged: i64 = format!("{}{}", first, last).parse().unwrap();

    return merged
    
}

pub fn solve(input: Vec<String>) {
    // TODO: Solve the problem
    let mut result: i64 = 0;
    for line in input {
        result += join_first_and_last_numbers(&line);
    }
    println!("Result: {}", result);
}