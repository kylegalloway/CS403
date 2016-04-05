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

; Rational Numbers

(define (make-rat n d)
    (cond
        ((= d 0) (print "Error denom is 0"))
        ((and (= n 0))
            (cons n d)
        )
        ((and (> n 0) (> d 0))
            (cons n d)
        )
        ((and (> n 0) (< d 0))
            (cons (- 0 n) (- 0 d))
        )
        ((and (< n 0) (> d 0))
            (cons n d)
        )
        ((and (< n 0) (< d 0))
            (cons (- 0 n) (- 0 d))
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