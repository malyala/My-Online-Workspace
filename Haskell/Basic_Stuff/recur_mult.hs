
recur_mult :: Int -> Int -> Int
recur_mult a b = case b of
                      1 -> a
                      _ ->a + recur_mult a (b -1)
    

















