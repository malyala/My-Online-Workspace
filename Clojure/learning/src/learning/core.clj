(ns learning.core
  (:gen-class))

(defn -main
  "I don't do a whole lot ... yet."
  [& args]
  (println "I'm a little tea pot, short and stout!"))


(defn my-reduce
  "my implementation of reduce"
  ([f init xs]
   (if (empty? xs)
     init
     (my-reduce f (f init (first xs)) (rest xs))))
  ([f [head & tail]]
   (my-reduce f head tail)))




(def consecdup #(reduce (fn [a b] (if (= (last a) b)
                                    a
                                    (conj a b))) '() %))


;; exercises: implement map using reduce, then filter

(defn my-map
  "implementing map with reduce"
  [f xs]
  (reduce (fn [seq-so-far item]
            (cons (f item) seq-so-far))
          (list)
          (seq xs)))


(defn my-filter
  "implementing map with reduce"
  [f xs]
  (reduce (fn [seq-so-far item]
            (if (f item)
              (cons item seq-so-far)
              seq-so-far))
          (list)
          (seq xs)))







