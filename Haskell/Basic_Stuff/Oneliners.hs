module Oneliners where

fun24 = map (+ 1)
fun25 = filter (not . even)
fun26 = map (`div` 2) . filter ((== 0) . (`mod` 2))
fun27 = map (`div` 2) . filter (even . (`div` 2))



