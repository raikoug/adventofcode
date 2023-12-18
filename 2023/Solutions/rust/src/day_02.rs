use std::collections::HashMap;


pub fn part_1(input: Vec<String>, cards: HashMap<&'static str, i32>) -> u32 {
    input
      .iter()
        .map(|line| {
            // each line is in the forma
            // Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
            // take game number and treat the string after : as a new input.
            
            // split line with character ":"
            let mut line_split = line.split(":");
            // the first element is now "Game X:", get X as u32
            let game_number: u32 = line_split.next().unwrap().split(" ").nth(1).unwrap().parse().unwrap();

            // second element is a list of games separated by ";",. loop through them returning a u32
            // if all the games are valid return 1 else 0.
            let mut moltipl: u32 = line_split.next().unwrap().split(";")
              .into_iter()
                .map(|game|{
                    // game now is list ho hands separated by ","
                    //     hands must be matched with variable 'cards'
                   
                    let mut res: u32 = game.split(",").into_iter()
                     .map(|hand|{
                           // if hand has a color with a value higher than cards[color] return 0
                           // else return 1, problem is that some hand starts witha a space
                           // need to clean it
                            let hand = hand.trim();
                            let color = hand.split(" ").nth(1).unwrap();
                            let value = hand.split(" ").nth(0).unwrap().parse::<i32>().unwrap();
                            if value > *cards.get(color).unwrap() {
                                return 0
                            }

                           1

                     }).product();
                    return res;
                    
                }).product();

            return game_number*moltipl;

        })
        .sum()
}
pub fn part_2(input: Vec<String>) -> u32 {
    input.iter()
    .map(|line| {
        // each line is in the forma
        // Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        // take game number and treat the string after : as a new input.
        
        // split line with character ":"
        let mut line_split = line.split(":");
        // the first element is now "Game X:", get X as u32
        let game_number: u32 = line_split.next().unwrap().split(" ").nth(1).unwrap().parse().unwrap();

        // second element is a list of games separated by ";",. loop through them making the sum of results.
        // TODO
        1


    }).sum()
}


pub fn solve(input: Vec<String>) {

    let mut cards: HashMap<&str, i32> = HashMap::new();
    cards.insert("red", 12);
    cards.insert("green", 13);
    cards.insert("blue", 14);
    
    
    // PART 1
    println!("part 1: {}", part_1(input.clone(), cards));

    // PART 2
    println!("part 2: {}", part_2(input));

}