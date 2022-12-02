let readfile path =
  let lines = ref [] in
  let ic = open_in path in
  try
    while true; do
      lines := input_line ic :: !lines
    done; !lines
  with End_of_file ->
    close_in ic;
    List.rev !lines
;;


(* 
   A : Opp Rock, B: Opp Paper, C: Opp scissors
   X : Lose, Y : Draw, Z : Win
 *)

exception UnknownValue of string;;


let rec parse l =
  let score round = match round with
    |"A X" -> 3 + 0
    |"A Y" -> 1 + 3
    |"A Z" -> 2 + 6
    |"B X" -> 1 + 0
    |"B Y" -> 2 + 3
    |"B Z" -> 3 + 6
    |"C X" -> 2 + 0
    |"C Y" -> 3 + 3 
    |"C Z" -> 1 + 6
    |_ -> raise (UnknownValue "Oui") in
  match l with
  |[] -> 0
  |hd::tl -> (score hd) + (parse tl);;

parse (readfile "input.txt");;
