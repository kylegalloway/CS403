(define (author)
    (println "AUTHOR: Kyle Galloway ckgalloway@crimson.ua.edu")
)

(define tolerance 0.0001)
(define (close-enough? a b) (< (abs (- a b)) tolerance))

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
    (define (mandelbrot x y)

    )
)

; Task 4
(define (root3 x)
    (define (improve guess)
        (/ (+ guess (/ x guess)) 2.0)
    )
    (define (root3-iter guess)
        (if (close-enough? (expt guess 3) x)
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
(define (crazyTriangle left right levels))

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


; Task 8
(define (egypt* b c))
(define (halve x))

; Task 9
(define (mystery n))

; Task 10
(define (ramanujan d x))
(define (iramanujan d x))


(define (run1)
    (inspect (if (= 0 0) (println "true") (println "false")))
    (inspect (my-if (= 0 0) (println "true") (println "false")))
    (println "     The my-if function evaluates it's arguments in applicative order.
     The if function evaluates them in normal order."
    )
)

(define (run2)
    (exprTest (zeno_cost 0.000001 55 .25) 7.0)
    (exprTest (zeno_cost 1 1 2) 16390.000000)
    (exprTest (zeno_cost 2 10 3) 7.174454e07)
    (exprTest (zeno_cost 8 10 2) 1310717.0000)
    (exprTest (zeno_cost 16 10 0.5000000000) 19.927083333)
    (exprTest (zeno_cost 128 2 0.5000000000) 3.9583333333)
    (exprTest (zeno_cost 0.0002000000 10 3) 17.000000000)
    (exprTest (zeno_cost 128 2 0.5000000000) 3.9583333333)
    (exprTest (zeno_cost 0.0008000000 10 2) 77.000000000)
    (exprTest (zeno_cost 16 10 0.5000000000) 19.927083333)
)

(define (run3)
    (define mandelbrot-tester (mandelbrot-iter 100))
    (if (= (mandelbrot-tester 2 3) 0)
        (print "point (2,3) is in the Mandelbrot set!\n")
        (print "point (2,3) is not in the Mandelbrot set.\n")
    )
)

(define (run4)
)

(define (run5)
)

(define (run6)
)

(define (run7)
)

(define (run8)
)

(define (run9)
)

(define (run10)
)

; ; Done (run1)
; ; Done (run2)
; (run3)
; ; Done (run4)
; (run5)
; ; Done (run6)
; (run7)
; (run8)
; (run9)
; (run10)
(println "assignment 1 loaded!")
