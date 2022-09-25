# gradle test -PmainClass=com.fra.leetcode.p01.ProblemTest

mkdir -p javacode/src/main/java/com/fra/hackerrank/triplets

cat ../data/triplets/data01.txt | gradle execute_problem
cat ../data/triplets/data02.txt | gradle execute_problem

cat ../data/candles/data01.txt | gradle execute_problem

gradle test -PmainClass=com.fra.hackerrank.candles.ProblemTest