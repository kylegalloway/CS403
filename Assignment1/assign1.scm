; Password for Submit: 16andcounting

(define (author)
    (println "AUTHOR: Kyle Galloway ckgalloway@crimson.ua.edu")
)

(define (exprTest # $expr target)
    (define result (catch (eval $expr #)))
    (if (error? result)
        (println $expr " is EXCEPTION: " (result'value)
            " (it should be " target ")")
        (println $expr " is " result
            " (it should be " target ")")
    )
)

; Task 1
(define (my-if a b c)
    (if (true? a)
        b
        c
    )
)

; Task 2
(define (zeno_cost d c f)
    (if (<= d (/ 1.0 9600))
        7.0
        (if (<= c (/ 1.0 12))
            (/ 1.0 12)
            (+ c (zeno_cost (/ d 2.0)
                            (* c f)
                            f
                 )
            )
        )
    )
)

; Task 3
(define (mandelbrot-iter threshold)
    (define (mandelbrot x y r s count)
        (if (> (+ (* r r) (* s s)) 4)
            count
            (if (> count threshold)
                0
                (mandelbrot x y (+ (- (* r r) (* s s)) x) (+ (* 2 r s) y) (+ count 1))
            )
        )
    )
    (lambda (x y) (mandelbrot x y 0.0 0.0 0))
)

; Task 4
(define (cube n) (* n n n))

(define (good-enough? guess improved-guess)
    (<= (abs (- guess improved-guess)) 0.00000001)
)

(define (root3 x)
    (define (improve guess)
        (/ (+ (/ x (* guess guess)) (* 2 guess)) 3) ;Newton's method for cube roots
    )
    (define (root3-iter guess)
            (if (good-enough? guess (improve guess))
                guess
                (root3-iter (improve guess))
            )
    )
    (if (> x 0)
        (root3-iter 1.0)
        0.0
    )
)

; Task 5
(define (crazyTriangle left right levels)

)

; Task 6
(define (oppy op)
    (lambda (num)
        (lambda (op1)
            (lambda (num1)
                (lambda (num2)
                    (op num (op1 num1 num2))
                )
            )
        )
    )
)

; Task 7
(define (w f i)
    (define A (S f (+ i 1) 0.0))
    (define B (S f (- i 1) 0.0))
    (define C (S f i 0.0))
    (if (= i 0)
        (f i)
        (/ (- (* A B) (* C C))
           (+ (- A (* 2 C)) B)
        )
    )
)
(define (S f n total)
    (if (= n 0)
        (f n)
        (S f (- n 1) (+ total (w f n)))
    )
)

; Task 8
(define (halve x)
    (define (halve-iter x num)
        (if (= (+ num num) x)
            num
            (halve-iter x (+ num 1))
        )
    )
    (halve-iter x 1)
)

(define (egypt* b c)
    (define (egypt*-iter2 a b c d)
        (if (= b 0)
            d
            (if (<= a b)
                (egypt*-iter2 (halve a) (- b a) (halve c) (+ c d))
                (egypt*-iter2 (halve a) b (halve c) d)
            )
        )
    )
    (define (egypt*-iter a b c)
        (if (<= a b)
          (egypt*-iter (+ a a) b (+ c c))
          (egypt*-iter2 a b c 0)
        )
    )
    (egypt*-iter 1 b c)
)

; Task 9
(define (mystery n)
    (println "Equivalent to sqrt(3) - 1 as it approaches infinity")
    (define (myst-rec total c)
        (if (= n 0)
            0
        )
        (if (< c n)
            (begin
                (if (= (% (- n c) 2) 0)
                    (myst-rec (/ 1 (+ 2 total)) (+ c 1))
                    (myst-rec (/ 1 (+ 1 total)) (+ c 1))
                )
            )
            (+ 1 total)
        )
    )
    (myst-rec 0.0 0)
)

; Task 10
(define (ramanujan d x)
    (define (ram-rec c)
        (if (< c d)
            (sqrt (+ 1 (* (+ x c) (ram-rec (+ c 1)))))
            1
        )
    )
    (if (= d 0)
        0
        (ram-rec 0)
    )
)

(define (iramanujan d x)
    (define (iram c total)
        (if (< c d)
            (iram (+ c 1) (sqrt (+ 1 (* (+ x (- d c) -1) total))))
            total
        )
    )

    (if (= d 0)
        0
        (iram 0 1.0)
    )
)


(define (run1)
    (inspect (if (= 0 0) (println "true") (println "false")))
    (inspect (my-if (= 0 0) (println "true") (println "false")))
    (println "     The my-if function evaluates it's arguments in applicative order.
     The if function evaluates them in normal order."
    )
)

(define (run2)
    (exprTest (zeno_cost 0.000001 55 .25) 7)
    (exprTest (zeno_cost 1 1 2) 16390)
    (exprTest (zeno_cost 0.0002 10 3) 17)
    (exprTest (zeno_cost 2 10 3) 7.174454e07)
    (exprTest (zeno_cost 128 2 0.5) 3.9583333333)
    (exprTest (zeno_cost 8 10 2) 1310717)
    (exprTest (zeno_cost 16 10 0.5) 19.927083333)
    (exprTest (zeno_cost 0.0008 10 2) 77)
)

(define (run3)
    (exprTest ((mandelbrot-iter 100) 0 0) 0)
	(exprTest ((mandelbrot-iter 100) 1 1) 2)
	(exprTest ((mandelbrot-iter 100) 2 2) 1)
	(exprTest ((mandelbrot-iter 100) -2 -2) 1)
	(exprTest ((mandelbrot-iter 100) -1 -1) 3)
	(exprTest ((mandelbrot-iter 100) .5 .5) 5)
    (exprTest ((mandelbrot-iter 100) 2 3) 1)
)

(define (run4)
    (exprTest (root3 64) 4)
    (exprTest (root3 8) 2)
    (exprTest (root3 27) 3)
    (exprTest (root3 216) 6)
    (exprTest (root3 42) 3.476026645)
    (exprTest (root3 4) 1.587401052)
)

(define (run5)
    (crazyTriangle 1 2 6)
)

(define (run6)
    (exprTest (((((oppy +) 1) *) 2) 3) (+ 1 (* 2 3)))
    (exprTest (((((oppy -) 1) -) 2) 3) (- 1 (- 2 3)))
    (exprTest (((((oppy /) 1) +) 2) 3) (/ 1 (+ 2 3)))
    (exprTest (((((oppy *) 1) /) 2) 3) (* 1 (/ 2 3)))
)

(define (run7)
    (define (f x) (* (** -1 x) (/ 1 (+ (* 2 x) 1))))
    (exprTest (S f 3 0.0) 3.1415)
)

(define (run8)
    (exprTest (egypt* 56 1960) 109760)
    (exprTest (egypt* 64 64) 4096)
    (exprTest (egypt* 100 100) 10000)
    (exprTest (egypt* 280 1240) 347200)
)

(define (run9)
	(exprTest (mystery 0) 1)
	(exprTest (mystery 1) 2.0)
	(exprTest (mystery 2) 1.6666666667)
	(exprTest (mystery 3) 1.7500000000)
	(exprTest (mystery 4) 1.7272727273)
	(exprTest (mystery 5) 1.7333333333)
	(exprTest (mystery 10) 1.7320490368)
	(exprTest (mystery 25) 1.7320508076)
	(exprTest (mystery 100) 1.7320508076)
	(exprTest (mystery 1000) 1.7320508076)
	(exprTest (mystery 10000) 1.7320508076)
)

(define (run10)
	(exprTest (ramanujan 0 0) 0)
	(exprTest (ramanujan 0 1) 0)
	(exprTest (ramanujan 1 0) 1.0)
	(exprTest (ramanujan 1 1) 1.4142135624)
	(exprTest (ramanujan 2 1) 1.6528916503)
	(exprTest (ramanujan 1 2) 1.7320508076)
	(exprTest (ramanujan 2 2) 2.2360679775)
	(exprTest (ramanujan 3 3) 3.2951592364)
	(exprTest (ramanujan 7 4) 4.9198021247)
	(exprTest (ramanujan 6 11) 11.497813243)
	(exprTest (ramanujan 116 87) 88.000000000)
	(exprTest (ramanujan 116 11793) 11794.000000)
	(exprTest (iramanujan 0 0) 0)
	(exprTest (iramanujan 0 1) 0)
	(exprTest (iramanujan 1 0) 1.0)
	(exprTest (iramanujan 1 1) 1.4142135624)
	(exprTest (iramanujan 2 1) 1.6528916503)
	(exprTest (iramanujan 1 2) 1.7320508076)
	(exprTest (iramanujan 2 2) 2.2360679775)
	(exprTest (iramanujan 3 3) 3.2951592364)
	(exprTest (iramanujan 7 4) 4.9198021247)
	(exprTest (iramanujan 6 11) 11.497813243)
	(exprTest (iramanujan 116 87) 88.000000000)
	(exprTest (iramanujan 116 11793) 11794.000000)
	(exprTest (iramanujan 1000 11793) 11794.000000)
	(exprTest (iramanujan 1000 503403) 503404.00000)
)

; ; Done (run1)
; ; Done (run2)
; ; Done (run3)
; ; Done (run4)
; (run5)
; ; Done (run6)
(run7)
; ; Done (run8)
; ; Done (run9)
; ; Done (run10)
(println "assignment 1 loaded!")
