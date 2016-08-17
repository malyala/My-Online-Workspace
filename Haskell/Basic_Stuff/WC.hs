-- files ch01/WC.hs
--  these are comments

main = interact wordCount
    where wordCount input = show (length (words input)) ++ "\n"

