module Heap where

data HeapT prio val

data May a = Noth | Jus a
  deriving (Eq, Show)



