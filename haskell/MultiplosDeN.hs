module MultiplosDeN where 
multiplosDeN :: Integer -> [Integer] -> [Integer]
multiplosDeN _ [] = []
multiplosDeN n (x:xs) | (mod x n) == 0 = x:multiplosDeN n xs
                      | otherwise = multiplosDeN n xs
