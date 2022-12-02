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
   X : Rock, Y : Paper, Z : scissors
 *)

exception UnknownValue of string;;


let rec parse l =
  let score round = match round with
    |"A X" -> 1 + 3
    |"A Y" -> 2 + 6
    |"A Z" -> 3 + 0
    |"B X" -> 1 + 0
    |"B Y" -> 2 + 3
    |"B Z" -> 3 + 6
    |"C X" -> 1 + 6
    |"C Y" -> 2 + 0 
    |"C Z" -> 3 + 3
    |_ -> raise (UnknownValue "Oui") in
  match l with
  |[] -> 0
  |hd::tl -> (score hd) + (parse tl);;

parse (readfile "input.txt");;
