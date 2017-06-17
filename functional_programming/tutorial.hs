import Data.List
import System.IO

maxInt = maxBound :: Int
minInt = minBound :: Int

sumOfNums = sum[1..1000]

modEx = mod 5 4 -- here mod is prefix operator
modEx2 = 5 `mod` 4 -- here mod is infix operator

{-
:t sqrt
-}

num9 = 9 :: Int

sqrtOf9 = sqrt (fromIntegral num9)

primeNumbers = [3, 5, 7, 11]
morePrimeNumbers = primeNumbers ++ [13, 17]


-- create a list

myList = 2 : 4 : 6: 7 : []

multList = [[3, 5, 6], [12,23,16]]

morePrimes2 = 2 : morePrimeNumbers

lenPrime = length morePrimes2

revPrime = reverse morePrimes2

isListEmpty = null morePrimes2

-- get index 2

secondPrime = morePrimes2 !! 2

lastPrime = last morePrimes2

-- get everything except the last value in the list

primeInit = init morePrimes2

-- get first 3 values

first3Primes = take 3 morePrimes2

removePrimes = drop 3 morePrimes2

is7InList = 7 `elem` morePrimes2

newList = [2,3,4]

prodlists = product newList

zeroToTen = [0..10]

evenList = [2, 4..20]

letterList = ['A', 'C'..'Z']

infinPow10 = [10,20..]

many2s = take 10 (repeat 2)

cycleList = take 10 (cycle [1,2,3,4,5])

listTimes2 = [x * 2 | x <- [1..10]]

listTimes3 = [x * 3 | x <- [1..10], x * 3 <= 20]

divisBy9N13 = [x | x <- [1..500], x `mod` 13 == 0, x `mod` 9 == 0]

sortedList = sort [4,2,6,2,1,7,3]

sumOfLists = zipWith (+) [1,2,4,5] [123,234,1234]

listBiggerThan5 = filter (>5) morePrimes2

evensUpTo20 = takeWhile (<=20) [2,4..]

multOfList = foldl (*) 1 [2,3,4,5] --foldl left to right


pow3List = [3^n | n <- [1..10]]

multTable = [ [x * y | y <- [1..10]] | x <- [1..10] ]

randTuple = (1, "Random string")


bobSmith = ("Bob Smith", 52)

bobsNames =  fst bobSmith
bobsAge = snd bobSmith

names = ["bob", "mary"]
addresses = ["124 main", "234 north"]

namesNAddress = zip names addresses

{-
main = do
  putStrLn "what's your name"
  name <- getLine
  putStrLn("hello " ++ name)

-}

-- declare type

addMe :: Int -> Int -> Int

-- funcName param1 param2 = operations (returned value)

addMe x y = x + y

sumMe x y = x + y

addTuples :: (Int, Int) -> (Int, Int) -> (Int, Int)

addTuples (x, y) (x2, y2) = (x+x2, y+y2)

whatAge :: Int -> String

whatAge 16 = "you can drive"
whatAge 21 = "you can vote"

whatAge _ = "Nothing Important"

factorial :: Int -> Int

factorial 0 = 1
factorial n = n * factorial (n - 1)



prodFact n = product [1..n]

isOdd :: Int -> Bool

isOdd n
  | n `mod` 2 == 0 = False
  | otherwise = True

isEven n = n `mod` 2 == 0

whatGrade :: Int -> String

whatGrade age
  | (age >= 5) && (age <= 6) = "Kindergarden"
  | (age> 6) && (age<10) = "Elementary School"
  | otherwise = "Go somewhere else"


getListItems :: [Int] -> String

getListItems [] = "Your list is empty"
getListItems (x:[]) = "Your list starts with " ++ show x
getListItems (x:y:[]) = "Your list contains " ++ show x ++ show y
getListItems (x:xs) = "Your list has " ++ show x ++ show xs

getFirstItem :: String -> String

getFirstItem [] = "Empty String"
getFirstItem all@(x:xs) = "The first letter in " ++ all ++ "is "++ [x]
