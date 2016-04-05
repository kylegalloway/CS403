; Expr Test
; Use: (exprTest (+ 1 1) 2)
(define (exprTest # $expr target)
    (define result (catch (eval $expr #)))
    (println)
    (cond
        ((error? result)
            (println $expr " is EXCEPTION:")
            (println (result'value))
            (println "It should be:")
            (println target))
        (else
            (println $expr " is: ")
            (println result ", it should be: ")
            (println target)
        )
    )
)

; GCD
(define (gcd a b)
    (if (= b 0)
        a
        (gcd b (remainder a b))
    )
)

; 2.1 Rational Numbers

(define (make-rat n d)
    (define g (gcd n d))
    (cond
        ((= d 0) (print "Error denom is 0"))
        ((and (= n 0))
            (cons (/ n g) (/ d g))
        )
        ((and (> n 0) (> d 0))
            (cons (/ n g) (/ d g))
        )
        ((and (> n 0) (< d 0))
            (cons (/ (- 0 n) g) (/ (- 0 d) g))
        )
        ((and (< n 0) (> d 0))
            (cons (/ n g) (/ d g))
        )
        ((and (< n 0) (< d 0))
            (cons (/ (- 0 n) g) (/ (- 0 d) g))
        )
    )
)

(define (numer x) (car x))

(define (denom x) (cdr x))

(define (print-rat x)
    (newline)
    (display (numer x))
    (display "/")
    (display (denom x))
    (newline)
)

(define (add-rat x y)
    (make-rat
        (+
           (* (numer x) (denom y))
           (* (numer y) (denom x))
        )
        (* (denom x) (denom y))
    )
)

(define (sub-rat x y)
    (make-rat
        (-
            (* (numer x) (denom y))
            (* (numer y) (denom x))
        )
        (* (denom x) (denom y))
    )
)

(define (mult-rat x y)
    (make-rat
        (* (numer x) (numer y))
        (* (denom x) (denom y))
    )
)

(define (div-rat x y)
    (make-rat
        (* (numer x) (denom y))
        (* (denom x) (numer y))
    )
)

(define (equal-rat? x y)
    (=
        (* (numer x) (denom y))
        (* (numer y) (denom x))
    )
)

; Ex 2.2 Line Segments
(define (make-segment a b) (cons a b))
(define (start-segment s) (car s))
(define (end-segment s) (cdr s))

(define (make-point x y) (cons x y))
(define (x-point p) (car p))
(define (y-point p) (cdr p))

(define (midpoint-segment s)
    (define x1 (x-point (start-segment s)))
    (define x2 (x-point (end-segment s)))
    (define y1 (y-point (start-segment s)))
    (define y2 (y-point (end-segment s)))
    (make-point (- x2 x1) (- y2 y1))
)

(define (print-point p)
  (display "(")
  (display (x-point p))
  (display ",")
  (display (y-point p))
  (display ")")
  (newline)
)

; Tests
(define a (make-rat 1 2))
(define b (make-rat 3 4))
(define c (make-rat -1 2))
(define d (make-rat 1 -2))
(define e (make-rat -1 -2))

; Tests that make-value works
; (exprTest a (cons 1 2))
; (exprTest b (cons 3 4))
; (exprTest c (cons -1 2))
; (exprTest d (cons -1 2))
; (exprTest e (cons 1 2))

; Tests reduced make-value
; (exprTest (mult-rat a b) (cons 3 8))
; (exprTest (div-rat a b) (cons 2 3))
; (exprTest (div-rat b a) (cons 3 2))

(define a (make-point 1 1))
(define b (make-point 3 3))
(define s (make-segment a b))
(print-point (midpoint-segment s))